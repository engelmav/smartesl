'use strict';

angular.module('smarteslApp')
  .controller('CreateQuestionCtrl', function (appserver,$scope,$http) {

  	// I was oved into the createQuestionDirective
/*
  	// You can probably just create a scope variable and
  	// then use it in your ng-models. Then your submit won't
  	// need to explicitly pass in this huge set of variables

  	$scope.questionBody = 'Enter the question to ask in this field.'

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
  	$scope.submitQuestion = function(questionBody,choices,metatags){
  		var choicesArr = [];
  		for (var i=0; i<choices.length; i++){
  			choicesArr.push(choices[i]['field'])
  		}
  		var metaTagsArr = [];
  		for (var i=0; i<metatags.length; i++){
  			metaTagsArr.push(metatags[i]['field'])
  		}

        //console.log('Submitted question.');
        var question = {};
        question.body = questionBody;
        //question.choices = [];
        question.choices = choicesArr;
        //question.metatags = [];
        question.metatags= metaTagsArr;

        console.log('Submitting the following question: ' + question);

        $http.post(appserver + '/question/submit_question', question ).
          success(function(results){
            console.log('submitAnswer success response: ' + results);
          });

  	};
*/
  });