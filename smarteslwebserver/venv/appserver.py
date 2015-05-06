# what is the thing about samurais crafting their own weapons?

from flask import Flask, jsonify, json, request
from flask.ext.cors import CORS, cross_origin

from model import DBAccessor

app = Flask(__name__)

with app.app_context():
    dba = DBAccessor()

CORS(app, resources=r'/*', allow_headers='Content-Type')

def getCurrentQuestion():
# will need the following variables:
#     userId. Will look up class/session of userId and look up the
#     current question in the current_questions table
    question = {}
    question['id'] = 1
    question['type'] = 'MultipleChoice'
    question['body'] = "Twitter was __________ in March 2006 by Jack Dorsey, Evan Williams, Biz Stone and Noah Glass."
    question['choices'] = ['create','creating', 'created']
    question['metadata'] = ['passive voice', 'extra syllabic ending']
    return question

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data.decode())
    print data
# the below is a mockup object of a user with role 'admin'
    username = data['username']
    userName, firstName, lastName, role = dba.getUserData(username)
    # TODO: Id to be sessionId
    return jsonify( { 'sessionId':1234, 'username': userName, 'firstname': firstName,
        'lastname': lastName, 'role': role  } )


@app.route('/')
def root():
    return 'Smart ESL Application Server'

#@app.route('/submit_answer', methods=['POST'])
#def submit_answer(answer):
#    print "Received answer: " + answer


@app.route('/question/get_question', methods=['GET'])
def getQuestion():
    # student client polls for currently set question
    # mock sending json question.

    return jsonify(getCurrentQuestion())


@app.route('/question/submit_answer', methods=['POST'])
def submitAnswer():
    data = json.loads(request.data.decode())
    print data['username']
    # student answers question
    return jsonify({'oh':'jes'})

@app.route('/question/submit_question', methods=['POST'])
def submitQuestion():
    question = json.loads(request.data.decode())
    questionId = dba.addQuestion(question)

    return jsonify( { 'questionId': questionId } )

@app.route('/instructor/submit_timeline', methods=['POST'])
def submitTimeline():
    timelineData = json.loads(request.data.decode())
    print timelineData
    dba.addTimeline(timelineData)
    return jsonify({'oh':'jes'})

@app.route('/search/timelines', methods=['POST'])
def searchTimelines():
    searchPhrase = json.loads(request.data.decode())
    print searchPhrase
    results = dba.searchTimelines(searchPhrase['phrase'])
    print results
    return jsonify({'results':results})

@app.route('/search/questions', methods=['POST'])
def searchQuestions():
    searchPhrase = json.loads(request.data.decode())
    print searchPhrase
    results = dba.searchQuestions(searchPhrase['phrase'])
    print results
    return jsonify({'results':results})

@app.route('/instructor/get_classes', methods=['POST'])
def getInstructorClasses():
    data = json.loads(request.data.decode())
    instructorId = data['instructorId']
    instructor_classes = dba.getInstructorClasses(instructorId)
    return jsonify({'classes':instructor_classes})

if __name__ == '__main__':

    app.run(debug=True)
