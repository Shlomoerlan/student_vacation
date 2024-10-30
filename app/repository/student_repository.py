from app.db.database import session_maker
from app.modeles import Student


def get_all_students():
    with session_maker() as session:
        return session.query(Student).all()

def get_student_by_id(student_id):
    with session_maker() as session:
        return session.query(Student).filter(Student.id == student_id).first()