'use strict';

function QuestionTimelineSvc(appserver,$http){
	this.questionPreviewList = [];
	this.addQuestion = function(question){
		this.questionPreviewList.push(question);
		console.log('questionTimelineSvc added: ' + JSON.stringify(question));
		console.log('questionPreviewList in timeline service:')
		console.log(JSON.stringify(this.questionPreviewList));
	};
}

angular.module('smarteslApp')
.factory('questionTimelineSvc', function(appserver,$http){
	return new QuestionTimelineSvc(appserver,$http);
});
