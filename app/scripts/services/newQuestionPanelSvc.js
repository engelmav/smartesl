'use strict';


function NewQuestionSvc(appserver,$http){
	// This service is duplicating some of what createQuestionDirective
	// already does. We need to find the code that isn't used here and
	// remove it. We can also control the question directive without a
	// service...

	this.questionData = {}

	this.getStarted = 'OK';
	this.showNewQuestion = false;
	this.fromOutline = false;

}

angular.module('smarteslApp')
.factory('newQuestionPanelSvc', function(appserver,$http){
	return new NewQuestionSvc(appserver,$http);
});

