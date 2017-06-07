from flask_restplus import Model, fields as f

choice_fields = Model('Choice', {
    'choice_id': f.Integer,
    'choice_text': f.String,
})

metatags_fields = Model('Metatags', {
    'metatag_id': f.Integer,
    'tag_name': f.String,
})

multi_choice = Model('Question', {
    'question_id': f.Integer(readOnly=True, description="The question's unique identifier"),
    'body': f.String(required=True, description='Body of the question'),
    'choices': f.List(f.Nested(choice_fields)),
    'metatags': f.List(f.Nested(metatags_fields)),
    'user_id': f.String,
    'evaluation_type': f.String
})

user = Model('User', {
    'first_name': f.String,
    'last_name': f.String,
    'username': f.String,
    # TODO: restrict when marshalling response
    'password': f.String,
    'user_id': f.Integer,
    'role': f.String
})

question_list = Model

question_set = Model('QuestionSet', {

})

