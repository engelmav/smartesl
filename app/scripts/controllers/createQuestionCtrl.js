'use strict';

angular.module('smarteslApp')
  .controller('CreateQuestionCtrl', function (appserver,$scope,$http) {

  	// You can probably just create a scope variable and
  	// then use it in your ng-models. Then your submit won't
  	// need to explicitly pass in this huge set of variables

  	console.log('Inside the CreateQuestionCtrl contoller');


	$scope.inputs = [{field:'choice text'}];

	$scope.addInput = function(){
	    $scope.inputs.push({field:'', value:''});
	}

	$scope.removeInput = function(index){
	    $scope.inputs.splice(index,1);
	}

	$scope.metainputs = [{field:'metatag'}];

	$scope.addMetaInput = function(){
	    $scope.metainputs.push({field:'', value:''});
	}

	$scope.removeMetaInput = function(index){
	    $scope.metainputs.splice(index,1);
	}
  	$scope.submitQuestion = function(choices,metatags){
  		console.log(choices);
  		console.log(metatags);
  		for (var key in choices){
  			console.log('choice: ' + choices['field'][key]);
  		}
        console.log('Submitted question.');
        var question = {};
        question.body = questionBody;
        question.choices = [];
        question.choices.push(choice1, choice2, choice3);
        question.metatags = [];
        question.metatags.push(metatag1,metatag2,metatag3);

        console.log('Submitting the following question: ' + question);

        $http.post(appserver + '/question/submit_question', question ).
          success(function(results){
            console.log('submitAnswer success response: ' + results);
          });

  	};
  });