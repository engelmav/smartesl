from flask import Flask
from flask_restplus import Api
import resources as main_resources
import json
from logger import log
from services import create_user, find_user_by_id, create_multi_choice
import pytest


@pytest.fixture
def app():
    api = Api(title="SmartEFL")
    api.add_namespace(main_resources.api, '/api')
    flask_app = Flask(__name__)
    api.init_app(flask_app)
    return flask_app.test_client()


@pytest.fixture
def question():
    return {
        "body": "This app was ____ in 2014.",
        "choices": [ "conceive", "conceived", "conceiving"],
        "metatags": ["preterit"],
        "user_id": "108"
    }


def test_get_question_404(app):
    r = app.get("/api/multi_choice/45454545")
    log.debug(r)
    assert r.status_code == 404


def test_get_question_200(app):
    r = app.get("/api/multi_choice/1")
    log.debug(r)
    assert r.status_code == 200


def test_post_question(app, question):
    r = app.post("/api/multi_choice/",
                 data=json.dumps(question),
                 content_type='application/json')
    response = r.data.decode('utf8')
    question_data = json.loads(response)
    log.info("Question data in  test_post_question: %s", response)
    assert question_data['metatags'][0]['tag_name'] == 'preterit'
    assert question_data['choices'][0]['choice_text'] == 'conceive'
    assert r.status_code == 200


def test_find_user_by_id():
    user_result = find_user_by_id(108)
    assert user_result.user_id == 108


def test_create_question(question):
    q = create_multi_choice(question)
    assert q is not None


def test_create_user():
    user = {
        'first_name': 'Vincent',
        'last_name': 'Engelmann',
        'username': 'vengelmann',
        'password': 'tryAgain',
        'email': 'someemail@email.com',
        'role': 'student',
    }
    u = create_user(user)
    assert u is not None

