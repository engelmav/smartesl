from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class MultipleChoiceQuestion(Resource):
    def get(self, question_id):
        return {'hello': 'world'}, 200

    def post(self):
        pass


api.add_resource(MultipleChoiceQuestion, '/multiple_choice')

if __name__ == '__main__':
    app.run(port=5999)
    