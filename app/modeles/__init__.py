from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .country import Country
from .student import Student
from .student_vacation import StudentVacation