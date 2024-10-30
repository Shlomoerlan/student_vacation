from app.db.database import session_maker
from app.modeles import Student, Country
from sqlalchemy import func, text
from app.modeles import StudentVacation


def get_all_students_vacations():
    with session_maker() as session:
        return session.query(StudentVacation).all()

def get_student_vacation_by_id(student_vacation_id):
    with session_maker() as session:
        return session.query(StudentVacation).filter_by(id=student_vacation_id).first()

def find_students_vacationed_in_country(country_name: str):
    with session_maker() as session:
        country = session.query(Country).filter_by(name=country_name).first()
        if not country:
            return []

        student_vacations = session.query(StudentVacation).filter_by(country_id=country.id).all()
        student_ids = [vacation.student_id for vacation in student_vacations]
        students = session.query(Student).filter(Student.id.in_(student_ids)).all()
        return students

def get_vacation_of_student(student_id):
    with session_maker() as session:
        return session.query(StudentVacation).filter_by(student_id=student_id).all()

def get_students_vacations_between_dates(start_date, end_date):
    with (session_maker() as session):
        return (session.query(StudentVacation)
                .filter_by
                (StudentVacation.start_vacation<start_date
                and StudentVacation.end_vacation>end_date)
                ).all()

def get_students_vacation_greater_than_10_days():
    with session_maker() as session:
        vacations = (
            session.query(StudentVacation)
            .filter(
                func.age(StudentVacation.end_vacation, StudentVacation.start_vacation) > text('interval \'10 days\'')
            )
            .all()
        )
        return vacations

print(find_students_vacationed_in_country('South Georgia')[0].name)

