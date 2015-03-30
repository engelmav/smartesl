'use strict';


function NewQuestionSvc(appserver,$http){

	this.questionData = {}

	this.getStarted = 'OK';
	this.fromOutline = false;


	this.questionBody = 'Enter the question to ask in this field.';
	this.inputs = [{field:'choice text'}];

	this.addInput = function(){
		this.inputs.push({field:'', value:''});
	};

	this.removeInput = function(index){
		this.inputs.splice(index,1);
	};

	this.metainputs = [{field:'metatag'}];

	this.addMetaInput = function(){
		this.metainputs.push({field:'', value:''});
	};

	this.removeMetaInput = function(index){
		this.metainputs.splice(index,1);
	};
	this.submitQuestion = function(questionBody,choices,metatags){
		var choicesArr = [];
		for (var i=0; i<choices.length; i++){
			choicesArr.push(choices[i]['field'])
		}
		var metaTagsArr = [];
			for (var i=0; i<metatags.length; i++){
		metaTagsArr.push(metatags[i]['field'])
		}

		//console.log('Submitted question.');
		var question = {};
		question.body = questionBody;
		//question.choices = [];
		question.choices = choicesArr;
		//question.metatags = [];
		question.metatags= metaTagsArr;

		console.log('Submitting the following question: ' + question);

		$http.post(appserver + '/question/submit_question', question ).
		success(function(results){
		console.log('submitAnswer success response: ' + results);
		});
	};

}

angular.module('smarteslApp')
.factory('newQuestionPanelSvc', function(appserver,$http){
	return new NewQuestionSvc(appserver,$http);
});

