"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session

sqlite_database = 'sqlite:///persons.db'
engine = create_engine(sqlite_database)
class Base(DeclarativeBase): pass
class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date = Column(Integer)
    janr = Column(String)
    rate = Column(String)

Base.metadata.create_all(bind=engine)

def create(f_name, f_date, f_janr, f_rate):
    with Session(autoflush=False, bind=engine) as db:
        film = Films(name=f_name, date=f_date, janr=f_janr, rate=f_rate)
        db.add(film)
        db.commit()

def all_films():
    with Session(autoflush=False, bind=engine) as db:
        all_films = db.query(Films)
        for k in all_films:
            print(f'{k.name}')

create('Бегом по Вене', 2004, 'Хоррор, Трагедия, Комедия', '4.3')
all_films()