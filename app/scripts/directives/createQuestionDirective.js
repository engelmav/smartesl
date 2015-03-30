'use strict';

angular.module('smarteslApp')
  .directive('newquestion', function(){

        return {
            restrict: 'E',
            scope: {
                progress: '=newquestion'
            },
            templateUrl: '/views/create_question.html',
            
            controller: function($scope,$http,$timeout,appserver,newQuestionPanelSvc){

              $scope.questionSvc = newQuestionPanelSvc;

              console.log('Called from outline: ' + $scope.questionSvc.fromOutline);
              
              $scope.$watch('questionSvc.showNewQuestion', function(newVal,oldVal){
                console.log('Show new question panel : ' + newVal);
              });

              //console.log('Inside the controller of the new question directive.');

              //console.log('From Service: ' + $scope.questionSvc.getStarted);

              $scope.questionBody = 'Enter the question to ask in this field.';



              $scope.inputs = [{field:'choice text'}];

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
                var choicesArr = [];
                for (var i=0; i<choices.length; i++){
                  choicesArr.push(choices[i]['field']);
                }
                var metaTagsArr = [];
                for (var i=0; i<metatags.length; i++){
                  metaTagsArr.push(metatags[i]['field']);
                }

                //console.log('Submitted question.');
                var question = {};
                question.body = questionBody;
                //question.choices = [];
                question.choices = choicesArr;
                //question.metatags = [];
                question.metatags = metaTagsArr;

                console.log('Submitting the following question: ' + question);

                $http.post(appserver + '/question/submit_question', question ).
                  success(function(results){
                    console.log('submitAnswer success response: ' + results);
                });
              };
            },
            controllerAs: 'CreateQuestionCtrl'
        };


    });
