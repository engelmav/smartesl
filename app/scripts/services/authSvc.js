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
          var userData = res.data;
          // { 'sessionId':12345, 'username': username, 'firstname': firstname, 'lastname': lastname, 'role': role  }
          Session.create(userData.sessionId, userData.username,
                         userData.firstname, userData.lastname, userData.role);
          return userData;
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

    this.loggedOn = false;

    this.create = function (sessionId, userId, firstname, lastname, userRole) {
      console.log('In the Session.create method');
      this.id = sessionId;
      this.userId = userId;
      this.firstName = firstname
      this.lastname = lastname
      this.userRole = userRole;
      this.loggedOn = true;
    };
    this.destroy = function () {
      console.log('In the Session.destroy method.');
      this.id = null;
      this.userId = null;
      this.userRole = null;
      this.loggedOn = false;
    };

  });