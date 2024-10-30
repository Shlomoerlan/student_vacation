import csv
import os
from app.modeles import Student

def get_students_from_csv():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'db', 'data.csv')
    students = []
    for row in read_csv(file_path):
        student = Student(
            name=row['Name'],
            age=row['Age'],
            favorite_language=row['Favorite_Language'],
            favorite_framework=row['Favorite_Framework']
        )
        students.append(student)
    return students

def read_csv(path: str):
    with open(path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            yield row

