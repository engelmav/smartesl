from flask import Flask, jsonify, json, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/question/*', allow_headers='Content-Type')

# use http://flask.pocoo.org/docs/0.10/appcontext/ to initialize stuff on the server
# if needed

def getCurrentQuestion():
    question = {}
    question['id'] = 1
    question['type'] = 'MultipleChoice'
    question['body'] = "Twitter was __________ in March 2006 by Jack Dorsey, Evan Williams, Biz Stone and Noah Glass."
    question['choices'] = ['create','creating', 'created']
    question['metadata'] = ['passive voice', 'extra syllabic ending']
    return question



@app.route('/')
def root():
    return 'Smart ESL Application Server'

#@app.route('/submit_answer', methods=['POST'])
#def submit_answer(answer):
#    print "Received answer: " + answer


@app.route('/question/get_question', methods=['GET'])
# https://github.com/corydolphin/flask-cors/blob/master/examples/view_based_example.py
#@cross_origin()
def get_question():
    # student client polls for currently set question
    # mock sending json question.

    return jsonify(getCurrentQuestion())


@app.route('/question/submit_answer', methods=['POST'])
def submit_answer():
    data = json.loads(request.data.decode())
    print data
    # student answers question
    return jsonify({'oh':'jes'})



if __name__ == '__main__':

    app.run(debug=True)

