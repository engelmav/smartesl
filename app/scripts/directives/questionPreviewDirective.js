'use strict';

angular.module('smarteslApp')
  .directive('questionpreview', function(appserver,questionTimelineSvc){

    return {
      restrict: 'E',
      scope: {
        question: '=' // inherit from parent
      },
      templateUrl: '/views/question_preview.html',
      controller: function($scope,$http,$timeout,questionTimelineSvc){

        $scope.removeQuestion = function(index){
          questionTimelineSvc.questionPreviewList.splice(index,1);
        };

      }
    }
});
