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


t_instructor_classes = Table(
    'instructor_classes', metadata,
    Column('instructor_id', Integer),
    Column('class_id', Integer)
)


class Metatag(Base):
    __tablename__ = 'metatags'

    metatag_id = Column(Integer, primary_key=True)
    tag_name = Column(Text)
    question_id = Column(Integer, ForeignKey('questions.question_id'))

t_question_set_list = Table(
    'question_set_list', metadata,
    Column('set_list_id', Integer, nullable=False),
    Column('set_id', Integer),
    Column('question_id', Integer)
)


t_question_sets = Table(
    'question_sets', metadata,
    Column('set_id', Integer, nullable=False),
    Column('creator_id', Integer),
    Column('vote_score', Integer),
    Column('set_name', Text)
)


class MultipleChoiceQuestionM(Base):
    __tablename__ = 'questions'

    creator = Column(Integer, ForeignKey('users.user_id'))
    question_id = Column(Integer, primary_key=True)
    body = Column(Text)
    metatags = relationship('Metatag', backref='question', lazy='dynamic')
    choices = relationship('Choice', backref='question', lazy='dynamic')

    def __repr__(self):
        return "<MultipleChoiceQuestionM(%r, %r)>" % (
                self.question_id, self.body
            )


t_student_classes = Table(
    'student_classes', metadata,
    Column('student_id', Integer),
    Column('class_id', Integer)
)


class User(Base):
    __tablename__ = 'users'

    questions = relationship('MultipleChoiceQuestionM', backref='question', lazy='dynamic')
    user_id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    email = Column(Text)
    phone_number = Column(Text)
    timestamp = Column(DateTime, server_default=text("now()"))
    role = Column(Text)
    username = Column(Text)

#     __mapper_args__ = {
#         'polymorphic_on':type,
#         'polymorphic_identity': 'users'
#     }
#
#
# class Student(User):
#     __mapper_args__ = {
#         'polymorphic_identity': 'users'
#     }
#
#
# class Instructor(User):
#     __mapper_args__ = {
#         'polymorphic_identity': 'users'
#     }