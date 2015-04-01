'use strict';

angular.module('smarteslApp')
  .directive('newquestion', function(){

        return {
            restrict: 'E',
            scope: {
                progress: '=newquestion'
            },
            templateUrl: '/views/create_question.html',
            
            controller: function($scope,$http,$timeout,appserver,newQuestionPanelSvc,questionOutlineSvc){

              $scope.submitButtonText = 'test';

              $scope.questionSvc = newQuestionPanelSvc;
              
              $scope.$watch('questionSvc.showNewQuestion', function(){
                if ($scope.questionSvc.showNewQuestion == true){ // opening in NewQuestionTimeline
                  $scope.submitButtonText = 'Save to timeline!';
                } else {
                  $scope.submitButtonText = 'Save!';
                }
              });

              //console.log('Inside the controller of the new question directive.');

              //console.log('From Service: ' + $scope.questionSvc.getStarted);

              $scope.questionBody = 'Enter the question to ask in this field.';

              $scope.inputs = [{  field:'choice text', isCorrect:'false'  }];

              $scope.addInput = function(){
                  $scope.inputs.push({field:'', value:''});
              };

              $scope.removeInput = function(index){
                  $scope.inputs.splice(index,1);
              };

              $scope.metainputs = [{field:'metatag'}];

              $scope.addMetaInput = function(){
                  $scope.metainputs.push({field:'', value:''});
              };

              $scope.removeMetaInput = function(index){
                  $scope.metainputs.splice(index,1);
              };
              $scope.submitQuestion = function(questionBody,choices,metatags){
                console.log('choices data: ' + JSON.stringify(choices))
                var choicesArr = [];
                for (var i=0; i<choices.length; i++){
                  choicesArr.push( [ choices[i]['field'], choices[i]['isCorrect'] ] );
                }
                var metaTagsArr = [];
                for (var i=0; i<metatags.length; i++){
                  metaTagsArr.push(metatags[i]['field']);
                }

                var question = {};
                question.body = questionBody;
                question.choices = choicesArr;
                question.metatags = metaTagsArr;

                // Load everything into the the service so that it can be shared with other components
                // (like the timeline)

                $scope.questionSvc.questionData = question;

                console.log('Submitting the following question: ' + JSON.stringify(question));
                $http.post(appserver + '/question/submit_question', question ).
                  success(function(results){
                    console.log('submitAnswer success response: ' + results);
                });

                console.log('Storing in service for question outline preview');

                questionOutlineSvc.addQuestion(question);
              };
            },
            controllerAs: 'CreateQuestionCtrl'
        };


    });
