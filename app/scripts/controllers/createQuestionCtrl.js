'use strict';

angular.module('smarteslApp')
  .controller('CreateQuestionCtrl', function (appserver,$scope,$http) {
  	$scope.submitQuestion = function(questionBody,choice1,choice2,choice3){
        console.log('Submitted question.');
        var question = {};
        question.body = questionBody;
        question.choices = [];
        question.choices.push(choice1, choice2, choice3);

        console.log('Submitting the following question: ' + question);

        $http.post(appserver + '/question/submit_question', question ).
          success(function(results){
            console.log('submitAnswer success response: ' + results);
          });

  	};
  });