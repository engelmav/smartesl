angular.module('smarteslApp')
  .directive('newquestion', function(appserver){

        return {
            restrict: 'E',
            scope: {
                progress: '=newquestion'
            },
            templateUrl: '/views/create_question.html',
            
            controller: function($scope,$http,$timeout){

              console.log('Inside the controller of the new question directive.');


            },
            controllerAs: 'CreateQuestionCtrl'
        };


    });
