'use strict';

angular.module('smarteslApp')
  .controller('QuestionOutlineCtrl', function (appserver,$scope,$http,newQuestionPanelSvc) {

  	$scope.showNewQuestion = false;

  	$scope.questionSvc = newQuestionPanelSvc;

  	$scope.createNewQuestion = function() {
  		if ($scope.questionSvc.showNewQuestion == false){

  			$scope.questionSvc.showNewQuestion = true;
  			$scope.showNewQuestion = $scope.questionSvc.showNewQuestion;
  			console.log('Opening new question panel.');

  		} else {

  			$scope.questionSvc.showNewQuestion = false;
  			$scope.showNewQuestion = $scope.questionSvc.showNewQuestion;
  			console.log('Closing new question panel.');

  		}
  	};

  	$scope.$watch('questionSvc.questionData', function(){
  		console.log('questioOutline now sees question data');
  	});


 
  });