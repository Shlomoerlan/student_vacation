from graphene import ObjectType, List, Field, Int, String
from app.gql.types import StudentType, StudentVacationType, CountryType
from app.repository.country_repository import get_all_countries, get_country_by_id
from app.repository.student_repository import get_all_students, get_student_by_id
from app.repository.student_vacation_repository import get_student_vacation_by_id, find_students_vacationed_in_country, \
    get_vacation_of_student, get_all_students_vacations, get_students_vacations_between_dates, \
    get_students_vacation_greater_than_10_days
from graphene.types.datetime import Date


class Query(ObjectType):
    countries = List(CountryType)
    students = List(StudentType)
    students_vacations = List(StudentVacationType)
    student_by_id = Field(StudentType, student_id=Int(required=True))
    country_by_id = Field(CountryType, country_id=Int(required=True))
    student_vacation_by_id = Field(StudentVacationType, student_id=Int(required=True))
    students_on_specific_vacation = List(StudentVacationType, country_name=String(required=True))
    get_vacation_of_student_by_id = List(StudentVacationType, student_id=Int(required=True))
    get_students_vacations_between_dates = List(StudentVacationType, start_date=Date(required=True), end_date=Date(required=True))
    get_students_vacations_more_than_10_days = List(StudentVacationType)

    @staticmethod
    def resolve_countries(root, info):
        return get_all_countries()

    @staticmethod
    def resolve_students(root, info):
        return get_all_students()

    @staticmethod
    def resolve_students_vacations(root, info):
        return get_all_students_vacations()

    @staticmethod
    def resolve_student_by_id(root, info, student_id):
        return get_student_by_id(student_id)


    @staticmethod
    def resolve_country_by_id(root, info, country_id):
        return get_country_by_id(country_id)

    @staticmethod
    def resolve_student_vacation_by_id(root, info, student_id):
        return get_student_vacation_by_id(student_id)

    @staticmethod
    def resolve_students_on_specific_vacation(root, info, country_name):
        find_students_vacationed_in_country(country_name)

    @staticmethod
    def resolve_get_vacation_of_student_by_id(root, info, student_id):
        return get_vacation_of_student(student_id)

    @staticmethod
    def resolve_get_students_vacations_between_dates(root, info, start_date, end_date):
        return get_students_vacations_between_dates(start_date, end_date)

    @staticmethod
    def resolve_get_students_vacations_more_than_10_days(root, info):
        return get_students_vacation_greater_than_10_days()