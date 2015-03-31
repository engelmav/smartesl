'use strict';


function QuestionOutlineSvc(appserver,$http){
	this.questionPreviewList = [];
	this.addQuestion = function(question){
		this.questionPreviewList.push(question);
		console.log('questionOutlineSvc added: ' + JSON.stringify(question));
	};
}

angular.module('smarteslApp')
.factory('questionOutlineSvc', function(appserver,$http){
	return new QuestionOutlineSvc(appserver,$http);
});