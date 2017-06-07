from flask_restplus import Namespace, Resource, abort, marshal

from logger import log
import serializer_schema as schema
import services

api = Namespace("main", description='SmartEFL API')


class GetQuestion(Resource):
    @api.param('question_id', 'Question ID')
    def get(self, question_id):
        log.debug("Getting question id %s", question_id)
        question = services.get_question_by_id(question_id)
        if question is None:
            abort(404, "No question found with ID %s" % question_id)
        return marshal(question, schema.multi_choice)


class PostQuestion(Resource):
    def post(self):
        question_dict = self.api.payload
        log.debug("Question data posted: %s", question_dict)
        question = services.create_multi_choice(question_dict)
        return marshal(question, schema.multi_choice)


class GetUser(Resource):
    @api.param('user_id', 'User ID')
    def get(self, user_id):
        log.debug("Getting question id %s", user_id)
        user = services.get_user_by_id(user_id)
        if user is None:
            abort(404, "No user found with ID %s" % user_id)
        return marshal(user, schema.user)


class PostUser(Resource):
    def post(self):
        user_dict = self.api.payload
        log.debug("User data posted: %s", user_dict)
        user = services.create_user(user_dict)
        return marshal(user, schema.user)


api.add_resource(GetQuestion, '/multi_choice/<question_id>')
api.add_resource(PostQuestion, '/multi_choice/')
api.add_resource(GetUser, '/user/<user_id>')
api.add_resource(PostUser, '/user/')
