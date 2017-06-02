from flask_restplus import Model, fields

choice_fields = Model('Choice', {
    'choice_id': fields.Integer,
    'choice_text': fields.String,
})

metatags_fields = Model('Metatags', {
    'metatag_id': fields.Integer,
    'tag_name': fields.String,
})

multi_choice_json_schema = Model('MultipleChoiceQuestionM', {
    'question_id': fields.Integer(readOnly=True, description="The question's unique identifier"),
    'body': fields.String(required=True, description='Body of the question'),
    'choices': fields.List(fields.Nested(choice_fields)),
    'metatags': fields.List(fields.Nested(metatags_fields)),
    'user_id': fields.String
})

user = None


