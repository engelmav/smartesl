from flask_restplus import Namespace, Resource, fields, abort, marshal
from models import MultipleChoiceQuestionM, Metatag, Choice, User
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_conn_str
from logger import log


api = Namespace("main", description='SmartEFL API')

choice_fields = api.model('Choice', {
    'choice_id': fields.Integer,
    'choice_text': fields.String,
})

metatags_fields = api.model('Metatags', {
    'metatag_id': fields.Integer,
    'tag_name': fields.String,
})

multi_choice_json_schema = api.model('MultipleChoiceQuestionM', {
    'question_id': fields.Integer(readOnly=True, description="The question's unique identifier"),
    'body': fields.String(required=True, description='Body of the question'),
    'choices': fields.List(fields.Nested(choice_fields)),
    'metatags':fields.List(fields.Nested(metatags_fields)),
    'user_id': fields.String
})

engine = create_engine(db_conn_str)
session = Session(bind=engine)


@api.route('/multi_choice/<id>')
class MultiChoiceQuestionGet(Resource):
    @api.marshal_with(multi_choice_json_schema)
    @api.param('id', 'The cat identifier')
    def get(self, id):
        log.debug("Getting question id %s", id)
        question = session.query(MultipleChoiceQuestionM).\
            filter_by(question_id=id).first()

        log.debug("Question returned: %s", question)
        if question is None:
            abort(404, "No question found with ID %s" % id)
        return question


@api.route('/multi_choice/')
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

        log.debug("Committed new question with ID %s", question.question_id)
        question_dict['question_id'] = question.question_id
        return marshal(question, multi_choice_json_schema)