'use strict';

angular.module('smarteslApp')
  .controller('QuestionPromptorCtrl', function (appserver,Session,$scope,$http) {

  	$scope.instructorClasses = []
	$http.post(appserver + '/instructor/get_classes', { 'instructorId': Session.userId }).
		success(function(results){
		console.log('Loading instructor classes: ' + JSON.stringify(results));
		$scope.instructorClasses = results['classes'];
	});
  });