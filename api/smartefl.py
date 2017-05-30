from flask import Flask
from flask_restplus import Api, Resource, fields, abort
from config import db_conn_str
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from autogen_models import MultipleChoice
from logger import log


app = Flask(__name__)
api = Api(app, version='1.0', title='SmartEFL',
    description='SmartEFL API',
)
ns = api.namespace('smartefl', description='SmartEFL ops')

multi_choice = api.model('MultipleChoice', {
    'question_id': fields.Integer(readOnly=True, description="The question's unique identifier"),
    'body': fields.String(required=True, description='Body of the question'),
    'choices': fields.List(fields.String),
    'creator': fields.String(required=True)
})

engine = create_engine(db_conn_str)
session = Session(bind=engine)


class MultiChoiceQuestion(Resource):

    @ns.marshal_with(multi_choice)
    def get(self, question_id):
        log.debug("Getting question id %s", question_id)
        question = session.query(MultipleChoice).filter_by(question_id=question_id)

        if question.count() == 0:
            abort(404, "No question found with ID %s" % question_id)

        return {'hello': 'world' + question_id}, 200

    @ns.expect(multi_choice)
    def post(self, question):
        


api.add_resource(MultiChoiceQuestion, '/multi_choice/<string:question_id>')

if __name__ == '__main__':
    app.run(port=5999)
