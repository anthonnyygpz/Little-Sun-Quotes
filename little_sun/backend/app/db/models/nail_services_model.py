from sqlalchemy import Column, Integer, String
from little_sun.backend.app.db.database import Base


class Services(Base):
    __tablename__ = "services"

    service_id = Column(
        Integer(), nullable=False, primary_key=True, autoincrement=True
    )
    service_name = Column(String(), nullable=False)
    description = Column(String(), nullable=True)
    price = Column(Integer(), nullable=False)
