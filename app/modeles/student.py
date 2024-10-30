from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.modeles import Base


class Student(Base):
   __tablename__ = "student"
   id = Column(Integer, primary_key=True, autoincrement=True)
   name = Column(String)
   age = Column(Integer)
   favorite_language = Column(String)
   favorite_framework = Column(String)
   students_vacations = relationship("StudentVacation", back_populates="student")
