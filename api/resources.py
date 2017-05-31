from flask_restplus import Namespace, Resource, fields, abort
from models import MultipleChoiceQuestionM, Metatag, Choice, User
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_conn_str
from logger import log


api = Namespace("main", description='SmartEFL API')

multi_choice = api.model('MultipleChoice', {
    'question_id': fields.Integer(readOnly=True, description="The question's unique identifier"),
    'body': fields.String(required=True, description='Body of the question'),
    'choices': fields.List(fields.String),
    'metatags': fields.List(fields.String),
    'user_id': fields.String(required=True)
})

engine = create_engine(db_conn_str)
session = Session(bind=engine)


@api.route('/multi_choice/<id>')
class MultiChoiceQuestionGet(Resource):
    @api.marshal_with(multi_choice)
    @api.param('id', 'The cat identifier')
    def get(self, id):
        log.debug("Getting question id %s", id)
        question = session.query(MultipleChoiceQuestionM).\
            filter_by(question_id=id).first()

        log.debug("Question returned: %s", question)
        if question.count() == 0:
            abort(404, "No question found with ID %s" % question_id)
        return question


@api.route('multi_choice/')
class MultiChoiceQuestionInsert(Resource):
    def post(self):

        question_dict = self.api.payload

        log.debug("Question data posted: %s", question_dict)

        body = question_dict['body']
        metatags = question_dict['metatags']
        choices = question_dict['choices']
        user_id = question_dict['user_id']

        question = MultipleChoiceQuestionM(body=body)

        user_result = session.query(User).\
            filter_by(user_id=user_id).first()

        question.creator = user_result.user_id

        for m in metatags:
            question.metatags.append(Metatag(tag_name=m, question=question))

        for c in choices:
            question.choices.append(Choice(choice_text=c, question=question))

        session.add(question)
        session.commit()
        return self.api.payload
