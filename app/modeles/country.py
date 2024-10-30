from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.modeles import Base


class Country(Base):
   __tablename__ = "country"
   id = Column(Integer, primary_key=True, autoincrement=True)
   region = Column(String)
   capital = Column(String)
   name = Column(String)
   students_vacations = relationship("StudentVacation", back_populates="country")
