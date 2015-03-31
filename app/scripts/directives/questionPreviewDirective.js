'use strict';

angular.module('smarteslApp')
  .directive('questionpreview', function(appserver,questionOutlineSvc){

    return {
        restrict: 'E',
        scope: {
            question: '=' // inherit from parent
        },
        templateUrl: '/views/question_preview.html',
        
        controller: function($scope,$http,$timeout,questionOutlineSvc){

          console.log('Inside the controller of the question preview directive.');
          /*
          $scope.$watch(questionOutlineSvc.questionPreviewList, function(){

          }*/

        }

    }
});
