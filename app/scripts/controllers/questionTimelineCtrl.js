'use strict';

angular.module('smarteslApp')
  .controller('QuestionTimelineCtrl', function (appserver,$scope,$http,newQuestionPanelSvc,questionTimelineSvc) {
      $scope.nqps = newQuestionPanelSvc;
    	$scope.createNewQuestion = function() {
        newQuestionPanelSvc.showNewQuestion.visibility = true;
        $scope.showNewQuestion = {'visible':true};
  	}

  	$scope.$watch('questionSvc.questionData', function(){
  		console.log('questioOutlineCtrl now sees question data');
  	});
    $scope.$watch('nqps.showNewQuestion', function(){
      console.log('nqps.showNewQuestion changed');
    });
    $scope.questionsInTimeline = questionTimelineSvc.questionPreviewList;
    var collectIds = function(questions){
      var questionIds = [];
      for (var i=0; i<questions.length; i++){
        questionIds.push(questions[i]['questionId'])
      }
      return questionIds;
    };
    
    $scope.addExistingQuestion = function(){
      console.log('Toggling questionsearch component');
      $scope.showSearchPanel = true;
    };

    $scope.submitTimeline = function(){
      var questionIds = collectIds(questionTimelineSvc.questionPreviewList);
      $http.post(appserver + '/instructor/submit_timeline', questionIds ).
        success(function(results){
          console.log('submitTimeline success response: ' + JSON.stringify(results));
      });
    };
     
  });