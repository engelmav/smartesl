'use strict';
// https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
angular.module('smarteslApp')
  .controller('LoginController', function ($scope, $rootScope, AUTH_EVENTS, AuthService, Session) {
    $scope.credentials = {
      username: '',
      password: ''
    };
    $scope.Session = Session;
    $scope.login = function (credentials) {
      console.log('LoginController.login called');
      AuthService.login(credentials).then(function (user) {
        console.log('User object in then method: ' + JSON.stringify(user));
        $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
        $scope.setCurrentUser(user);
      }, function () {
        $rootScope.$broadcast(AUTH_EVENTS.loginFailed);
      });
    };
  });
