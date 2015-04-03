'use strict';

angular.module('smarteslApp')
  .controller('QuestionTimelineCtrl', function (appserver,$scope,$http,newQuestionPanelSvc,questionTimelineSvc) {

  	//$scope.showNewQuestion = false;
    // expecting this to act like a reference
    $scope.showNewQuestion = newQuestionPanelSvc.showNewQuestion;

  	$scope.questionSvc = newQuestionPanelSvc;

  	$scope.createNewQuestion = function() {
  		if ($scope.questionSvc.showNewQuestion === false){

  			//$scope.questionSvc.showNewQuestion = true;
  			//$scope.showNewQuestion = $scope.questionSvc.showNewQuestion;
        $scope.showNewQuestion = true;
  			console.log('Opening new question panel.');

  		} else {

  			//$scope.questionSvc.showNewQuestion = false;
  			//$scope.showNewQuestion = $scope.questionSvc.showNewQuestion;
        $scope.showNewQuestion = false;
  			console.log('Closing new question panel.');

      }
  	}

  	$scope.$watch('questionSvc.questionData', function(){
  		console.log('questioOutlineCtrl now sees question data');
  	});
    $scope.questionsInTimeline = questionTimelineSvc.questionPreviewList;
    var collectIds = function(questions){
      var questionIds = [];
      for (var i=0; i<questions.length; i++){
        questionIds.push(questions[i]['questionId'])
      }
      return questionIds;
    };
    


    $scope.submitTimeline = function(){
      var questionIds = collectIds(questionTimelineSvc.questionPreviewList);
      $http.post(appserver + '/instructor/submit_timeline', questionIds ).
        success(function(results){
          console.log('submitTimeline success response: ' + JSON.stringify(results));
        });
    }


 
  });