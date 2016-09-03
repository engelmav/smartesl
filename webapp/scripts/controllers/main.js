'use strict';

/**
 * @ngdoc function
 * @name smarteslApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the smarteslApp
 */
angular.module('smarteslApp')
  .controller('MainCtrl', function ($scope, USER_ROLES, AuthService) {
  	console.log('Main controller entered.');

  	$scope.currentUser = null;
  	$scope.userRoles = USER_ROLES;
  	$scope.isAuthorized = AuthService.isAuthorized;

  	$scope.setCurrentUser = function(user) {
  		$scope.currentUser = user;
  	};
  });
