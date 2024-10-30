import requests
from app.db.database import session_maker, engine
from app.modeles import Country
from app.modeles import *
from app.modeles import Base
from app.repository.csv_repository import get_students_from_csv


def get_data():
    base_url = 'https://restcountries.com/v3.1/all'
    response = []
    response.extend(requests.get(base_url).json())
    return response


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    country_data = get_data()
    with session_maker() as session:
        for data in country_data:
           name = data["name"]["common"]
           region = data.get("region", None)
           capital = ', '.join(data.get("capital", [])) if "capital" in data else None
           country = Country(
              name=name,
              region=region,
              capital=capital
           )
           session.add(country)
        session.commit()

        for s in get_students_from_csv():
            name = s.name
            age = s.age
            favorite_language = s.favorite_language
            favorite_framework = s.favorite_framework
            student = Student(
                name=name,
                age=age,
                favorite_language=favorite_language,
                favorite_framework=favorite_framework
            )
            session.add(student)
        session.commit()