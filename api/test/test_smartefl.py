from flask import Flask
from flask_restplus import Api
import resources as main_resources
import json
from logger import log

import pytest


@pytest.fixture
def app():
    api = Api(title="SmartEFL")
    api.add_namespace(main_resources.api, '/api')
    flask_app = Flask(__name__)
    api.init_app(flask_app)
    return flask_app.test_client()


def test_get_question(app):
    r = app.post("/api/multi_choice/2")
    print(r)


def test_post_question(app):
    question_payload = {
        "body": "This app was ____ in 2014.",
        "choices": [ "conceive", "conceived", "conceiving"],
        "metatags": ["preterit"]
    }
    r = app.post("/api/multi_choice/",
                 data=json.dumps(question_payload),
                 content_type='application/json')
    print(r)
