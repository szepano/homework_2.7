from sqlalchemy import create_engine, String, ForeignKey, Column, Integer, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



db_url = 'url bazy danych'
engine = create_engine(db_url)
DBsession = sessionmaker(bind=engine)
session = DBsession()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    name = Column(String(), nullable=False)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), nullable=False)
    stud_id = Column(Integer(), ForeignKey('students.id'), primary_key=True)

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    name = Column(String())

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    subject = Column(String(), unique=True)
    teaches = Column(Integer(), ForeignKey('teachers.id'))

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer(), autoincrement=True, primary_key=True)
    stud_id = Column(Integer(), ForeignKey('students.id'))
    grade = Column(Integer())
    subject = Column(String(), ForeignKey('subjects.subject'))
    given_at = Column(DateTime(), default=func.now())

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)