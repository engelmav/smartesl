'use strict';

angular.module('smarteslApp')
  .constant('AUTH_EVENTS', {
    loginSuccess: 'auth-login-success',
    loginFailed: 'auth-login-failed',
    logoutSuccess: 'auth-logout-success',
    sessionTimeout: 'auth-session-timeout',
    notAuthenticated: 'auth-not-authenticated',
    notAuthorized: 'auth-not-authorized'
  })
  .constant('USER_ROLES', {
    all: '*',
    admin: 'admin',
    instructor: 'instructor',
    student: 'student',
    guest: 'guest'
  })
  .factory('AuthService', function ($http, Session, appserver) {
    var authService = {};

    authService.login = function (credentials) {
      console.log('In the authService.login method.');
      var testReturn = $http
        .post(appserver + '/login', credentials)
        .then(function (res) {
          var userLoginData = res.data;
          console.log('Login data received from server:');
          console.log(userLoginData);
          Session.create(userLoginData);
          return userLoginData;
        });
      console.log(JSON.stringify(testReturn));
      return testReturn;

    };

    authService.isAuthenticated = function () {
      return !!Session.userId;
    };

    authService.isAuthorized = function (authorizedRoles) {
      console.log('In the authService.isAuthorized method.');
      if (!angular.isArray(authorizedRoles)) {
        console.log('Checking if authorizedRoles (' + JSON.stringify(authorizedRoles) + ') is an array');
        authorizedRoles = [authorizedRoles];
      }
      return (authService.isAuthenticated() &&
        // if userRole is present and the user is authenticated, then return true.
        authorizedRoles.indexOf(Session.userRole) !== -1);
    };

    return authService;
  })
  .service('Session', function ($rootScope) {

    this.loggedOn = 0;

    this.create = function (userData) {
      console.log('In the Session.create method - creating session data using:');
      this.id = userData['sessionId'];
      this.userId = userData['userId'];
      this.firstName = userData['firstName'];
      this.lastname = userData['lastName'];
      this.role = userData['role'];
      this.views = userData['views'];
      this.loggedOn = 1;
    };
    this.destroy = function () {
      console.log('In the Session.destroy method.');
      this.id = null;
      this.userId = null;
      this.userRole = 0;
      this.loggedOn = false;
    };

  });
