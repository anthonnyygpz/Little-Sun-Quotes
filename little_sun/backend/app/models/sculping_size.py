from sqlalchemy import Column, Integer, String
from little_sun.backend.app.db.base import Base
from sqlalchemy.orm import relationship


class SculpingNailSize(Base):
    __tablename__ = "sculping_nail_sizes"

    size_id = Column(Integer, primary_key=True, autoincrement=True)
    size_name = Column(String, nullable=False)
    description = Column(String)
    base_price = Column(Integer, nullable=False)

    quotes = relationship("Quote", back_populates="sculping_sizes")
