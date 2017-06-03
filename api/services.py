from models import Question, Metatag, Choice, User
from logger import log
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_conn_str
from typing import Optional

engine = create_engine(db_conn_str)
session = Session(bind=engine)


def find_question_by_id(question_id: int) -> Optional[User]:
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
    user_result = find_user_by_id(user_id)
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


def find_user_by_id(user_id: int) -> Optional[User]:
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
