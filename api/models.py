# coding: utf-8
from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, Table, Text, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Choice(Base):
    __tablename__ = 'choices'

    choice_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'))
    tag_name = Column(Text)
    choice_text = Column(Text)
    iscorrect = Column(Boolean)


class Class(Base):
    __tablename__ = 'classes'

    class_id = Column(Integer, primary_key=True)
    class_name = Column(Text)


class UserClass(Base):
    # TODO: composite primary key with uniqueness constraint is required
    __tablename__ = 'user_classes'

    user_class_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    class_id = Column(Integer)


class Metatag(Base):
    __tablename__ = 'metatags'

    metatag_id = Column(Integer, primary_key=True)
    tag_name = Column(Text)
    question_id = Column(Integer, ForeignKey('questions.question_id'))


class QuestionSetList(Base):
    __tablename__ = 'question_set_list'

    question_set_list_id = Column(Integer, primary_key=True)
    question_set_id = Column(Integer, ForeignKey('question_sets.question_set_id'))
    question_id = Column(Integer, ForeignKey('questions.question_id'))


class QuestionSet(Base):
    __tablename__ = 'question_sets'

    question_set_id = Column(Integer, primary_key=True)
    creator_id = Column(Integer)
    vote_score = Column(Integer)
    set_name = Column(Text)
    questions = relationship('QuestionSetList', backref='question_sets', lazy='dynamic')


class Question(Base):
    __tablename__ = 'questions'

    creator = Column(Integer, ForeignKey('users.user_id'))
    question_id = Column(Integer, primary_key=True)
    body = Column(Text)
    metatags = relationship('Metatag', backref='question', lazy='dynamic')
    choices = relationship('Choice', backref='question', lazy='dynamic')

    def __repr__(self):
        return "<Question(%r, %r)>" % (
                self.question_id, self.body
            )


t_student_classes = Table(
    'student_classes', metadata,
    Column('student_id', Integer),
    Column('class_id', Integer)
)


class User(Base):
    __tablename__ = 'users'

    questions = relationship('Question', backref='question', lazy='dynamic')
    user_id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text)
    phone_number = Column(Text)
    timestamp = Column(DateTime, server_default=text("now()"))
    role = Column(Text)
    username = Column(Text)

