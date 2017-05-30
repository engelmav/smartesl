from typing import List
from logger import log
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Question(db.Model):
    __table__ = 'questions'
    __primary_key__ = 'question_id'


class MultipleChoice(Question):
    __table__ = 'questions'

    def __init__(self):
        Question.__init__(self)
        self._choices = None
        self._body = None
        self._answer = None

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body: str):
        self._body = body

    @property
    def choices(self):
        return self._choices

    @choices.setter
    def choices(self, choices: List[str]):
        self._choices = choices

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, answer: str):
        self._answer = answer


class Course(object):
    pass


class CourseSession(object):
    def set_current_question(self, question: Question):
        pass


class ContactDetails(object):
    pass


class Address(object):
    pass


class User(db.Model):
    __primary_key__ = 'user_id'
    __table__ = 'users'

    user_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)



class Student(User):
    __table__ = 'users'


class Instructor(User):
    __table__ = 'users'

    def first_name(self):
        log.debug("Getting first name")
        first_name = self.get_raw_attribute('first_name')
        return first_name

    @has_many('creator', 'user_id')
    def questions(self):
        return Question


class Timeline(object):
    def get_next_question(self):
        pass


