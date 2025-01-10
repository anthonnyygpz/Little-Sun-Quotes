from typing import Optional, TypeVar, Generic, Dict, Any
from pydantic import BaseModel
from datetime import datetime, timedelta
import httpx
import json
import logging
from dataclasses import dataclass

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Modelos base
class BaseResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    timestamp: datetime = datetime.now()


T = TypeVar("T")


class DataResponse(BaseResponse, Generic[T]):
    data: Optional[T] = None


@dataclass
class CacheItem:
    data: str
    expires_at: datetime


class DataFetchError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class Cache:
    def __init__(self):
        self._cache: Dict[str, CacheItem] = {}

    def get(self, key: str) -> Optional[str]:
        if key in self._cache:
            item = self._cache[key]
            if datetime.now() < item.expires_at:
                logger.info(f"Cache hit for key: {key}")
                return item.data
            else:
                logger.info(f"Cache expired for key: {key}")
                del self._cache[key]
        return None

    def set(self, key: str, value: Any, ttl_seconds: int = 3600) -> None:
        try:
            if not isinstance(value, str):
                value = json.dumps(value)

            expires_at = datetime.now() + timedelta(seconds=ttl_seconds)
            self._cache[key] = CacheItem(data=value, expires_at=expires_at)
            logger.info(f"Cached data for key: {key}, expires in {ttl_seconds} seconds")
        except Exception as e:
            logger.error(f"Error caching data: {str(e)}")

    def update_list_cache(self, list_key: str, deleted_id: Any) -> None:
        """Actualiza el caché de una lista después de un DELETE"""
        try:
            cached_data = self.get(list_key)
            if cached_data:
                data_list = json.loads(cached_data)
                if isinstance(data_list, list):
                    # Filtra el elemento eliminado
                    updated_list = [
                        item
                        for item in data_list
                        if str(item.get("id")) != str(deleted_id)
                    ]
                    self.set(list_key, updated_list, self.get_ttl(list_key))
                    logger.info(f"Updated list cache after deleting id {deleted_id}")
        except Exception as e:
            logger.error(f"Error updating list cache: {str(e)}")

    def get_ttl(self, key: str) -> int:
        """Obtiene el TTL restante de un item en caché"""
        if key in self._cache:
            remaining = (self._cache[key].expires_at - datetime.now()).total_seconds()
            return max(int(remaining), 0)
        return 3600

    def invalidate_pattern(self, pattern: str) -> None:
        """Invalida todas las claves que coincidan con el patrón"""
        keys_to_delete = [k for k in self._cache.keys() if pattern in k]
        for key in keys_to_delete:
            del self._cache[key]
            logger.info(f"Invalidated cache for key: {key}")


class DataFetcher:
    def __init__(self, base_url: str, cache_ttl: int = 3600, timeout: float = 10.0):
        self.base_url = base_url
        self.cache = Cache()
        self.cache_ttl = cache_ttl
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            headers={"Content-Type": "application/json"},
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self._client.aclose()

    def _generate_cache_key(self, endpoint: str, params: Optional[Dict] = None) -> str:
        key = endpoint
        if params:
            sorted_params = sorted(params.items())
            key += "_" + "_".join(f"{k}:{v}" for k, v in sorted_params)
        return key

    async def fetch_data(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict] = None,
        data: Optional[Dict] = None,
        use_cache: bool = True,
        update_list_cache: bool = False,
        list_endpoint: Optional[str] = None,
    ) -> DataResponse:
        cache_key = (
            self._generate_cache_key(endpoint, params) if method == "GET" else None
        )

        # Solo usar caché para GET
        if method == "GET" and use_cache and cache_key:
            cached_data = self.cache.get(cache_key)
            if cached_data:
                try:
                    data = json.loads(cached_data)
                    return DataResponse(success=True, data=data)
                except json.JSONDecodeError:
                    logger.warning(f"Invalid JSON in cache for key: {cache_key}")

        try:
            # Realizamos la petición HTTP con el body cuando sea necesario
            if method == "POST":
                response = await self._client.post(endpoint, json=data)
            else:
                response = await getattr(self._client, method.lower())(
                    endpoint, params=params
                )

            response.raise_for_status()  # Para DELETE, manejar la respuesta y actualizar caché
            if method == "DELETE":
                if update_list_cache and list_endpoint:
                    # Obtener el ID del quote_id en los parámetros
                    quote_id = params.get("quote_id") if params else None
                    if quote_id:
                        list_cache_key = self._generate_cache_key(list_endpoint)
                        self.cache.update_list_cache(list_cache_key, quote_id)
                return DataResponse(success=True, message="Quote deleted successfully")

            # # Para otros métodos, procesar respuesta JSON
            data = response.json()

            # Almacenar en caché solo para GET
            if method == "GET" and use_cache and cache_key:
                self.cache.set(cache_key, data, self.cache_ttl)

            return DataResponse(success=True, data=data)

        except httpx.HTTPError as e:
            error_msg = f"HTTP error occurred: {str(e)}"
            logger.error(error_msg)
            raise DataFetchError(error_msg, getattr(e.response, "status_code", None))  # type: ignore

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg)
            raise DataFetchError(error_msg)
