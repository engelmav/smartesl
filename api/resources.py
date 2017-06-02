from flask_restplus import Namespace, Resource, abort, marshal

from logger import log
import serialization_schema as schema
import services

api = Namespace("main", description='SmartEFL API')


@api.route('/multi_choice/<question_id>')
class MultiChoiceQuestionGet(Resource):
    @api.marshal_with(schema.multi_choice_json_schema)
    @api.param('question_id', 'Question ID')
    def get(self, question_id):
        log.debug("Getting question id %s", question_id)
        question = services.find_question_by_id(question_id)
        if question is None:
            abort(404, "No question found with ID %s" % question_id)
        return question


@api.route('/multi_choice/')
class MultiChoiceQuestionInsert(Resource):
    def post(self):
        question_dict = self.api.payload
        log.debug("Question data posted: %s", question_dict)
        question = services.create_multi_choice(question_dict)
        return marshal(question, schema.multi_choice_json_schema)


@api.route('/user/<user_id>')
class GetUser(Resource):
    @api.marshal_with(schema.user)
    @api.param('user_id', 'User ID')
    def get(self, user_id):
        log.debug("Getting question id %s", user_id)
        user = services.find_user_by_id(user_id)
        if user is None:
            abort(404, "No user found with ID %s" % user_id)
        return user


@api.route('/user/')
class MultiChoiceQuestionInsert(Resource):
    def post(self):
        user_dict = self.api.payload
        log.debug("User data posted: %s", user_dict)
        user = services.create_user(user_dict)
        return marshal(user, schema.user)

