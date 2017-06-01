'use strict';

angular.module('smarteslApp')
  .directive('newquestion', function(){

        return {
            restrict: 'E',
            scope: {
                someVar: '='
            },
            templateUrl: '../app/views/create_question.html',

            controller: function($scope,$http,$timeout,appserver,Session,newQuestionPanelSvc,questionTimelineSvc){

              console.log(JSON.stringify(newQuestionPanelSvc))
              $scope.questionSvc = newQuestionPanelSvc;

              $scope.submitQuestionWarnings = [];

              $scope.$watch('questionSvc.showNewQuestion', function(){
                if ($scope.questionSvc.showNewQuestion == true){ // opening in NewQuestionTimeline
                  $scope.submitButtonText = 'Save to timeline!';
                } else {
                  $scope.submitButtonText = 'Save!';
                }
              });

              $scope.questionBody = '';

              $scope.inputs = [{  field:'', isCorrect:'false'  }];

              $scope.addInput = function(){
                  $scope.inputs.push({field:'', value:''});
              };

              $scope.removeInput = function(index){
                  $scope.inputs.splice(index,1);
              };

              $scope.metainputs = [{field:''}];

              $scope.addMetaInput = function(){
                  $scope.metainputs.push({field:'', value:''});
              };

              $scope.removeMetaInput = function(index){
                  $scope.metainputs.splice(index,1);
              };
              $scope.submitQuestion = function(questionBody,choices,metatags){

                if(!Session.id || 0 === Session.id.length){
                  $scope.submitQuestionWarnings.push('You must be logged in to submit a question.');
                  return;
                }

                if (questionBody.length == 0){
                  $scope.submitQuestionWarnings.push('Please enter a question body.');
                }

                if (choices.length < 2){
                  $scope.submitQuestionWarnings.push('Please enter at least two choices.');
                }

                if ($scope.submitQuestionWarnings.length > 0){
                  return;
                }

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
                    console.log('submitQuestion success response: ' + JSON.stringify(results));
                    // you will need the ID for questions that are inserted into a timeline.
                    //if ($scope.questionSvc.showNewQuestion == true){
                      question['questionId'] = results['questionId'];
                      console.log('Question ID added to question object: ' + JSON.stringify(question));
                    //}

                });

                console.log('Storing in service for question timeline preview');
                /*  We are just dropping the question into the timeline list.
                    The questions are then actually added onto a timeline
                    when the user presses "Save Timeline in create_question_timeline"
                 */
                questionTimelineSvc.addQuestion(question);
                $scope.$emit('closeQuestionPanel');
              };
            },
            controllerAs: 'CreateQuestionCtrl'
        };


    });
