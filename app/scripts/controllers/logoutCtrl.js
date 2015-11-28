'use strict';
// https://medium.com/opinionated-angularjs/techniques-for-authentication-in-angularjs-applications-7bbf0346acec
angular.module('smarteslApp')
  .controller('LogoutCtrl', function ($scope, $rootScope, AUTH_EVENTS, AuthService, Session) {
    $scope.Session = Session;


    console.log('Logout Controller executed');

    Session.destroy();

    /* define inverses of the below:
    $scope.login = function (credentials) {
      console.log('LoginController.login called');
      AuthService.login(credentials).then(function (user) {
        console.log('User object in then method: ' + JSON.stringify(user));
        $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
        $scope.setCurrentUser(user);
      }, function () {
        $rootScope.$broadcast(AUTH_EVENTS.loginFailed);
      });
    }; */
  });
