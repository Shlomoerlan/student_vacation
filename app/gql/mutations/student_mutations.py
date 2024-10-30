from graphene import Mutation, Int, Date, Field, String, List
from graphql import GraphQLError

from app.db.database import session_maker
from app.gql.types import StudentVacationType, CountryType, StudentType
from app.modeles import StudentVacation, Country, Student


class AddStudentVacation(Mutation):
    class Arguments:
        student_id = Int()
        country_id = Int()
        start_vacation = Date()
        end_vacation = Date()

    student_vacation = Field(StudentVacationType)

    @staticmethod
    def mutate(root, info, student_id, country_id, start_vacation, end_vacation):
        with session_maker() as session:
            sv = StudentVacation(
                student_id=student_id,
                country_id=country_id,
                start_vacation=start_vacation,
                end_vacation=end_vacation
            )
            student_vacations = session.query(StudentVacation).filter_by(student_id=student_id).all()

            session.add(sv)
            session.commit()
            session.refresh(sv)
            return AddStudentVacation(student_vacation=sv)


class AddStudent(Mutation):
    class Arguments:
        name = String()
        age = Int()
        favorite_language = String()
        favorite_framework = String()

    student = Field(StudentType)

    @staticmethod
    def mutate(root, info, name, age, favorite_language, favorite_framework):
        with session_maker() as session:
            student = Student(
                name=name,
                age=age,
                favorite_language=favorite_language,
                favorite_framework=favorite_framework
            )
            session.add(student)
            session.commit()
            session.refresh(student)
            return AddStudent(student=student)


class AddCountry(Mutation):
    class Arguments:
        region = String()
        capital = String()
        name = String()

    country = Field(CountryType)

    @staticmethod
    def mutate(root, info, region, capital, name):
        with session_maker() as session:
            country = Country(region=region, capital=capital, name=name)
            session.add(country)
            session.commit()
            session.refresh(country)
            return AddCountry(country=country)

class UpdateStudent(Mutation):
    class Arguments:
        student_id = Int()
        name = String()
        age = Int()
        favorite_language = String()
        favorite_framework = String()

    student = Field(StudentType)
    @staticmethod
    def mutate(root, info, student_id, name, age, favorite_language, favorite_framework):
        with session_maker() as session:
            student = session.query(Student).filter_by(student_id=student_id).first()
            if not student:
                raise GraphQLError(f'no such student with id: {student_id}')
            student.name = name
            student.age = age
            student.favorite_language = favorite_language
            student.favorite_framework = favorite_framework
            session.commit()
            session.refresh(student)
            return UpdateStudent(student=student)

class UpdateCountry(Mutation):
    class Arguments:
        country_id = Int()
        name = String()
        capital = String()
        region = String()

    country = Field(CountryType)

    @staticmethod
    def mutate(root, info, country_id, name, capital, region):
        with session_maker() as session:
            country = session.query(Country).filter_by(country_id=country_id).first()
            if not country:
                raise GraphQLError(f'no such country with id: {country_id}')

            country.name = name
            country.capital = capital
            country.region = region
            session.commit()
            session.refresh(country)
            return UpdateCountry(country=country)

class UpdateStudentVacation(Mutation):
    class Arguments:
        student_vacation_id = Int()
        student_id = Int()
        country_id = Int()
        start_vacation = Date()
        end_vacation = Date()

    student_vacation = Field(StudentVacation)
    @staticmethod
    def mutate(root, info, start_vacation, end_vacation, student_vacation_id):
        with session_maker() as session:
            student_vacation = session.query(StudentVacation).filter_by(id=student_vacation_id).first()
            if not student_vacation:
                raise GraphQLError(f'no such vacation with id: {student_vacation_id}')
            student_vacation.start_vacation = start_vacation
            student_vacation.end_vacation = end_vacation
            session.commit()
            session.refresh(student_vacation)
            return UpdateStudentVacation(student_vacation=student_vacation)

class DeleteStudent(Mutation):
    class Arguments:
        student_id = Int()
        name = String()
        age = Int()
        favorite_language = String()
        favorite_framework = String()

    student = Field(StudentType)
    @staticmethod
    def mutate(root, info, student_id):
        with session_maker() as session:
            student = session.query(Student).filter_by(student_id=student_id).first()
            if not student:
                raise GraphQLError(f'no such student with id: {student_id}')
            student_vacation = session.query(StudentVacation).filter_by(student_id=student_id).first()
            if student_vacation:
                session.delete(student_vacation)
                session.delete(student)
            else:
                session.delete(student)
            session.commit()
            session.refresh(student)
            return DeleteStudent(student=student)

class DeleteAllSpecificCountry(Mutation):
    class Arguments:
        country_id = Int()
        name = String()
        capital = String()
        region = String()

    country_list = List(CountryType)
    @staticmethod
    def mutate(root, info, name):
        with session_maker() as session:
            country_list = session.query(CountryType).filter_by(name=name).all()
            session.delete_all(country_list)
            session.commit()
            session.refresh(country_list)
            return DeleteAllSpecificCountry(country_list=country_list)

class DeleteCountryWithNoAssociated(Mutation):
    class Arguments:
        country_id = Int()
        name = String()
        capital = String()
        region = String()

    country_list = List(CountryType)
    @staticmethod
    def mutate(root, info, country_id):
        with session_maker() as session:
            students_vacations = session.query(StudentVacation).filter_by(country_id=country_id).all()
            countries = session.query(Country).all()
            vacation_country_ids = {vacation.country_id for vacation in students_vacations}
            non_countries = [country for country in countries if country.id not in vacation_country_ids]
            session.delete_all(non_countries)
            session.commit()
            session.refresh(non_countries)
            return DeleteCountryWithNoAssociated(country_list=non_countries)
