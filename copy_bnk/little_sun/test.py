from typing import Optional, TypeVar, Generic, Dict, Any
from pydantic import BaseModel
from datetime import datetime, timedelta
import httpx
import asyncio
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
            # Convertimos el valor a string si no lo es
            if not isinstance(value, str):
                value = json.dumps(value)

            expires_at = datetime.now() + timedelta(seconds=ttl_seconds)
            self._cache[key] = CacheItem(data=value, expires_at=expires_at)
            logger.info(
                f"Cached data for key: {key}, expires in {ttl_seconds} seconds"
            )
        except Exception as e:
            logger.error(f"Error caching data: {str(e)}")

    def clear(self) -> None:
        self._cache.clear()
        logger.info("Cache cleared")


class DataFetcher:
    def __init__(
        self, base_url: str, cache_ttl: int = 3600, timeout: float = 10.0
    ):
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

    def _generate_cache_key(
        self, endpoint: str, params: Optional[Dict] = None
    ) -> str:
        """Genera una clave única para el caché basada en el endpoint y parámetros"""
        key = endpoint
        if params:
            # Ordenamos los parámetros para asegurar consistencia en las claves
            sorted_params = sorted(params.items())
            key += "_" + "_".join(f"{k}:{v}" for k, v in sorted_params)
        return key

    async def fetch_data(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        use_cache: bool = True,
    ) -> DataResponse:
        cache_key = self._generate_cache_key(endpoint, params)

        # Intentar obtener datos del caché si use_cache es True
        if use_cache:
            cached_data = self.cache.get(cache_key)
            if cached_data:
                try:
                    data = json.loads(cached_data)
                    return DataResponse(success=True, data=data)
                except json.JSONDecodeError:
                    logger.warning(
                        f"Invalid JSON in cache for key: {cache_key}"
                    )

        try:
            # Realizar la petición HTTP
            response = await self._client.get(endpoint, params=params)
            response.raise_for_status()
            data = response.json()

            # Almacenar en caché si use_cache es True
            if use_cache:
                self.cache.set(cache_key, data, self.cache_ttl)

            return DataResponse(success=True, data=data)

        except httpx.HTTPError as e:
            error_msg = f"HTTP error occurred: {str(e)}"
            logger.error(error_msg)
            raise DataFetchError(
                error_msg, getattr(e.response, "status_code", None)
            )

        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            logger.error(error_msg)
            raise DataFetchError(error_msg)


# Ejemplo de uso con usuarios
class UserAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000/api/"):
        self.fetcher = DataFetcher(
            base_url, cache_ttl=1800
        )  # 30 minutos de caché

    async def get_user(self, user_id: int) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data("get_quotes_data")
            return response.data

    #
    # async def get_users(self) -> List[Dict]:
    #     async with self.fetcher as fetcher:
    #         response = await fetcher.fetch_data("/users")
    #         return response.data


# Ejemplo de uso
async def main():
    # Crear instancia de UserAPI
    user_api = UserAPI()

    try:
        # Primera llamada - debería hacer petición HTTP
        logger.info("Fetching user 1 (first time)...")
        user = await user_api.get_user(1)
        print("User 1 (from HTTP):", user[0]["name"])

        # Segunda llamada - debería usar caché
        logger.info("Fetching user 1 (second time)...")
        user = await user_api.get_user(1)
        print("User 1 (from cache):", user[0]["name"])

        # Obtener todos los usuarios
        # logger.info("Fetching all users...")
        # users = await user_api.get_users()
        # print(f"Total users fetched: {len(users)}")
        #
    except DataFetchError as e:
        print(f"Error: {e.message}")
        if e.status_code:
            print(f"Status code: {e.status_code}")


if __name__ == "__main__":
    asyncio.run(main())
