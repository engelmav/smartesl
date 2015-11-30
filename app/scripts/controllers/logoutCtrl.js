'use strict';
// https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
angular.module('smarteslApp')
  .controller('LogoutCtrl', function ($scope, $rootScope, AUTH_EVENTS, AuthService, Session) {
    $scope.Session = Session;
    Session.destroy();
  });
