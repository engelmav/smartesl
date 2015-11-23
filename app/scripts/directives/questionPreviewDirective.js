'use strict';

angular.module('smarteslApp')
  .directive('questionpreview', function(appserver,questionTimelineSvc){

    return {
      restrict: 'E',
      scope: {
        question: '=' // inherit from parent
      },
      templateUrl: '../views/question_preview.html',
      controller: function($scope,$http,$timeout,questionTimelineSvc){
        /* make a object that acts like a cache of questions.
         * if the cache does not contain a question, fetch it from the server.
         * The questionpreview directive will then look to the cache for the
         * question list (and the question's content)
         */
        $scope.refreshQuestionCache = function(){

        };

        //var $scope.questionCache = {}; // questionId : { questionContent }
        if (!questionCache.hasOwnProperty(questionId)){
          $scope.questionCache[questionId] = $scope.getQuestionContent(questionId);
        }

        $scope.removeQuestion = function(index){
          questionTimelineSvc.questionPreviewList.splice(index,1);
        };
        $scope.getQuestionContent = function(qid){
          $http.post(appserver + '/services/get_question_content', {'id':qid}).
            success(function(results){
              console.log('submitTimeline success response: ' + JSON.stringify(results));
          });
        };


      }
    }
});
