from flask import Flask
from flask_restplus import Api
import resources as main_resources
import json
from logger import log
import pytest
from .seed_data import dummy_question, dummy_user


def resp_to_json(response):
    response_utf8 = response.data.decode('utf8')
    return json.loads(response_utf8)


@pytest.fixture
def app():
    api = Api(title="SmartEFL")
    api.add_namespace(main_resources.api, '/api')
    flask_app = Flask(__name__)
    api.init_app(flask_app)
    return flask_app.test_client()


def test_get_question_404(app):
    r = app.get("/api/multi_choice/45454545")
    log.debug(r)
    assert r.status_code == 404


def test_get_question_200(app):
    r = app.get("/api/multi_choice/1")
    log.debug(r)
    assert r.status_code == 200


def test_post_question(app):
    r = app.post("/api/multi_choice/",
                 data=json.dumps(dummy_question),
                 content_type='application/json')
    response = r.data.decode('utf8')
    question_data = json.loads(response)
    log.info("Question data in  test_post_question: %s", response)
    assert r.headers['Access-Control-Allow-Origin'] == '*'
    assert question_data['metatags'][0]['tag_name'] == 'preterit'
    assert question_data['choices'][0]['choice_text'] == 'conceive'
    assert r.status_code == 200
    print(headers)


def test_get_user(app):
    r = app.get("/api/user/108")
    resp_json = resp_to_json(r)
    log.debug(resp_json)
    assert resp_json['user_id'] == 108


def test_post_user(app):
    r = app.post("/api/user/",
                 data=json.dumps(dummy_user),
                 content_type='application/json')
    response = r.data.decode('utf8')
    user_data = json.loads(response)
    log.debug(user_data)
    assert user_data['username'] == 'vengelmann'

