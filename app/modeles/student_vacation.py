from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.modeles import Base

class StudentVacation(Base):
   __tablename__ = "student_vacation"
   start_vacation = Column(Date, nullable=False)
   end_vacation = Column(Date, nullable=False)
   id = Column(Integer, primary_key=True, autoincrement=True)
   student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
   country_id = Column(Integer, ForeignKey("country.id"), nullable=False)
   country = relationship("Country", back_populates="students_vacations")
   student = relationship("Student", back_populates="students_vacations")
