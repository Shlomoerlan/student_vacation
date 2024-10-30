from graphene import ObjectType, String, List, Int
from app.db.database import session_maker
from app.modeles import StudentVacation


class CountryType(ObjectType):
    id = Int()
    region = String()
    capital = String()
    name = String()
    students_vacations = List('app.gql.types.StudentVacationType')

    @staticmethod
    def resolve_students_vacations(root, info):
        with session_maker() as session:
            return session.query(StudentVacation).filter(StudentVacation.country_id == root.id).all()




