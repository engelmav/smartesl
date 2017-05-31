from flask_restplus import Namespace, Resource, fields, abort
from models import MultipleChoiceQuestionM, Metatag, Choice
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
    'creator': fields.String(required=True)
})

engine = create_engine(db_conn_str)
session = Session(bind=engine)


@api.route('/multi_choice/')
class MultiChoiceQuestion(Resource):
    # @api.marshal_with(multi_choice)
    # @api.route('/multi_choice/<string:question_id>')
    # @api.param('question_id', 'The cat identifier')
    def get(self, question_id):
        log.debug("Getting question id %s", question_id)
        question = session.query(MultipleChoice).filter_by(question_id=question_id)
        if question.count() == 0:
            abort(404, "No question found with ID %s" % question_id)
        return question

    @api.expect(multi_choice)
    @api.marshal_with(multi_choice)
    def post(self):
        question_dict = self.api.payload
        log.debug("Question data posted: %s", question_dict)
        log.debug(question_dict['metatags'])
        body = question_dict['body']
        metatags = question_dict['metatags']
        choices = question_dict['choices']
        question = MultipleChoiceQuestionM(body=body,
                                           # choices=choices,
                                           # metatags=metatags
                                           )
        session.add(question)
        session.commit()

        for m in metatags:
            question.metatags.append(Metatag(tag_name=m, question=question))

        for c in choices:
            question.choices.append(Choice(choice_text=c, question=question))

        session.add(question)
        session.commit()
        return self.api.payload
