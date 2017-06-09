from models import Question, Metatag, Choice, User, QuestionSet, \
    QuestionSetList, Class, UserClass
from logger import log
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_conn_str
from typing import Optional, List

engine = create_engine(db_conn_str)
session = Session(bind=engine)


def _get_values(d: dict, *args: list):
    values = []
    for arg in args:
        values.append(d[arg])
    return values


def get_question_by_id(question_id: int) -> Optional[User]:
    result = session.query(Question).\
            filter_by(question_id=question_id).first()

    log.debug("Question returned: %s", question_id)
    return result


def create_multi_choice(question_dict: dict) -> Question:
    body = question_dict['body']
    metatags = question_dict['metatags']
    choices = question_dict['choices']
    user_id = question_dict['user_id']
    question = Question(body=body)
    user_result = get_user_by_id(user_id)
    question.creator = user_result.user_id
    for m in metatags:
        question.metatags.append(Metatag(tag_name=m, question=question))
    for c in choices:
        question.choices.append(Choice(choice_text=c, question=question))
    session.add(question)
    session.commit()
    log.debug("Committed new question with ID %s", question.question_id)
    question_dict['question_id'] = question.question_id
    return question


def get_user_by_id(user_id: int) -> Optional[User]:
    result = session.query(User).\
            filter_by(user_id=user_id).first()
    log.debug("User returned: %s", user_id)
    return result


def create_user(user_dict: dict) -> int:
    first_name = user_dict['first_name']
    last_name = user_dict['last_name']
    role = user_dict['role']
    email = user_dict['email']
    username = user_dict['username']

    user = User(first_name=first_name, last_name=last_name, role=role,
                username=username, email=email)
    session.add(user)
    session.commit()
    return user


def get_question_set_by_id(question_set_id: int) -> QuestionSet:
    qs = session.query(QuestionSet).\
        filter_by(question_set_id=question_set_id).first()
    return qs


def create_question_set(question_set_dict: dict) -> Optional[QuestionSet]:
    set_name, user_id, question_list = _get_values(
        question_set_dict, 'set_name', 'creator_id', 'questions')

    question_set = QuestionSet(set_name=set_name, creator_id=user_id)

    for question_id in question_list:
        question_set.questions.append(QuestionSetList(question_id=question_id))

    session.add(question_set)
    session.commit()

    return question_set


def get_class_by_id(class_id) -> Class:
    class_ = session.query(Class).filter_by(class_id=class_id).first()
    return class_


def create_class(class_dict: dict) -> Class:
    class_ = Class(class_name=class_dict['class_name'])
    session.add(class_)
    session.commit()
    return class_


def add_user_to_class(user_id: int, class_id: int) -> Class:
    user = get_user_by_id(user_id)
    class_ = get_class_by_id(class_id)
    if user_id is None or class_ is None:
        return None
    user_class = UserClass(user_id=user_id, class_id=class_id)
    session.add(user_class)
    session.commit()
    return user_class


def get_classes_by_instructor(instructor_id: int) -> List[Class]:
    pass


def get_classes_by_student():
    pass





