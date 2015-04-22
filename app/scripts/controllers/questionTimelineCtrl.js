'use strict';

angular.module('smarteslApp')
  .controller('QuestionTimelineCtrl', function (appserver,$scope,$http,Session,newQuestionPanelSvc,questionTimelineSvc) {

    $scope.showNewQuestion = newQuestionPanelSvc.showNewQuestion;


  	$scope.questionSvc = newQuestionPanelSvc;

    // initialize as HIDDEN
    $scope.questionSvc.showNewQuestion = false;

    $scope.timelineName = '';

    $scope.submitWarning = '';

  	$scope.toggleNewQuestionPanel = function() {
  		if ($scope.questionSvc.showNewQuestion === false){
        $scope.questionSvc.showNewQuestion = true;
  			console.log('Opening new question panel.');
  		} else {
        $scope.questionSvc.showNewQuestion = false;
  			console.log('Closing new question panel.');
      }
  	};

  	$scope.$watch('questionSvc.questionData', function(){
  		console.log('questioOutlineCtrl now sees question data');
  	});
    $scope.$on('closeQuestionPanel', function(){
      console.log('closeQuestionPanel emitted to controller.');
      $scope.questionSvc.showNewQuestion = false;
    });

    $scope.$on('closeSearchPanel', function(){
      console.log('closeQuestionPanel emitted to controller.');
      $scope.showSearchPanel = false;
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
      if (!Session.id || 0 ===  Session.id.length){
        console.log('No session ID!');
        $scope.submitWarning += 'You must be logged in to save a timeline';
        return;
      }

      if (questionIds.length === 0){
        $scope.submitWarning += 'Add at least one question for your timeline. ';
      }

      if (Session.id){
        var timelineData = { 'userId': Session.userId, 'questionIds': questionIds, 'timelineName': $scope.timelineName };
        $http.post(appserver + '/instructor/submit_timeline', timelineData).
          success(function(results){
            console.log('submitTimeline success response: ' + JSON.stringify(results));
        });
      }
    };
     
  });