from graphene.types.datetime import Date
from graphene import ObjectType, Int, Field
from app.db.database import session_maker
from app.modeles import Student, Country


class StudentVacationType(ObjectType):
   id = Int()
   student_id = Int()
   country_id = Int()
   start_vacation = Date()
   end_vacation = Date()
   student = Field('app.gql.types.StudentType')
   country = Field('app.gql.types.CountryType')

   @staticmethod
   def resolve_student(root, info):
      with session_maker() as session:
         return session.query(Student).filter(Student.id == root.student_id).one()

   @staticmethod
   def resolve_country(root, info):
      with session_maker() as session:
         return session.query(Country).filter(Country.id == root.country_id).one()

