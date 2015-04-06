'use strict';

/**
 * @ngdoc overview
 * @name smarteslApp
 * @description
 * # smarteslApp
 *
 * Main module of the application.
 */
angular
  .module('smarteslApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/login_form.html',
        controller: 'LoginController'
      })
      .when('/answer_question', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/create_question', {
        templateUrl: 'views/create_question_container.html',
        controller: 'CreateQuestionCtrl'
      })
      .when('/create_question_set', {
        templateUrl: 'views/create_question_timeline.html',
        controller: 'QuestionTimelineCtrl'
      })
      .when('/question_promptor', {
        templateUrl: 'views/question_promptor.html',
        controller: 'QuestionPromptorCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .constant('appserver', 'http://127.0.0.1:5000');
