from graphene import String, Int, ObjectType, List

from app.db.database import session_maker
from app.gql.types import StudentVacationType


class StudentType(ObjectType):
    id = Int()
    name = String()
    age = Int()
    favorite_language = String()
    favorite_framework = String()
    students_vacations = List('app.gql.types.StudentVacationType')

    @staticmethod
    def resolve_students_vacations(root, info):
        with session_maker() as session:
            return session.query(StudentVacationType).filter(StudentVacationType.student_id == root.id).all()
