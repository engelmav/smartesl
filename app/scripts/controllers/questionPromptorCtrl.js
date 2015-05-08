'use strict';

angular.module('smarteslApp')
  .controller('QuestionPromptorCtrl', function (appserver,Session,$scope,$http) {

  	$scope.instructorClasses = [];
	  $http.post(appserver + '/instructor/get_classes', { 'instructorId': Session.userId }).
		success(function(results){
		console.log('Loading instructor classes: ' + JSON.stringify(results));
		$scope.instructorClasses = results.classes;
	});

	$scope.searchTimelines = function(){
		//stuff
	};

	$scope.useSelectedTimeline = function(){
		//stuff
	};

	$scope.nextQuestion = function(){
		//stuff
	};

	$scope.prevQuestion = function(){
		//stuff
	};

	$scope.broadcastQuestion = function(questionId,classId){
		$http.post(appserver + '/instructor/broadcast_question', { 'question': [ questionId, classId ] }).
			success(function(results){
				console.log('Broadcasted question: ' + JSON.stringify(results));
		});
	};
});
