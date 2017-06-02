from flask import Flask
from flask_restplus import Api
import resources as main_resources
import json
from logger import log
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_conn_str
from models import User, MultipleChoiceQuestionM, Metatag, Choice
import pytest


@pytest.fixture
def app():
    api = Api(title="SmartEFL")
    api.add_namespace(main_resources.api, '/api')
    flask_app = Flask(__name__)
    api.init_app(flask_app)
    return flask_app.test_client()

@pytest.fixture
def sqla_session():
    engine = create_engine(db_conn_str)
    return Session(bind=engine)


def test_get_question_404(app):
    r = app.get("/api/multi_choice/45454545")
    log.debug(r)
    assert r.status_code == 404


def test_get_question_200(app):
    r = app.get("/api/multi_choice/1")
    log.debug(r)
    assert r.status_code == 200


def test_post_question(app):
    question_payload = {
        "body": "This app was ____ in 2014.",
        "choices": [ "conceive", "conceived", "conceiving"],
        "metatags": ["preterit"],
        "user_id": "108"
    }
    r = app.post("/api/multi_choice/",
                 data=json.dumps(question_payload),
                 content_type='application/json')
    response = r.data.decode('utf8')
    question_data = json.loads(response)
    log.info("Question data in  test_post_question: %s", response)
    assert question_data['metatags'][0]['tag_name'] == 'preterit'
    assert question_data['choices'][0]['choice_text'] == 'conceive'
    assert r.status_code == 200


def test_find_user_by_id(sqla_session):
    user_result = sqla_session.query(User).filter_by(user_id=108).first()
    log.debug(user_result.user_id)
    assert user_result.user_id == 108


def test_add_question_with_creator(sqla_session):
    user_result = sqla_session.query(User).filter_by(user_id=108).first()
    question = MultipleChoiceQuestionM(body="body of question")

    question.creator = user_result.user_id

    sqla_session.add(question)

    for m in ["tag1", "tag2", "tag2"]:
        question.metatags.append(Metatag(tag_name=m, question=question))

    for c in ["choice1", "choice2", "choice3"]:
        question.choices.append(Choice(choice_text=c, question=question))

    sqla_session.add(question)
    sqla_session.commit()

