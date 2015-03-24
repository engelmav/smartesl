from flask import Flask, jsonify
from flask.ext.cors import cross_origin
app = Flask(__name__)

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

@app.route('/submit_answer', methods=['POST'])
def submit_answer(answer):
    print "Received answer: " + answer


@app.route('/get_question', methods=['GET'])
# https://github.com/corydolphin/flask-cors/blob/master/examples/view_based_example.py
@cross_origin()
def get_question():
    # student client polls for currently set question
    # mock sending json question.

    return jsonify(getCurrentQuestion())


@app.route('/submit_answer', methods=['POST'])
def submit_answer(answer):
    # student answers question
    pass



if __name__ == '__main__':
    app.run(debug=True)

