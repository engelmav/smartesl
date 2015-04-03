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
      .otherwise({
        redirectTo: '/'
      });
  })
  .value('appserver', 'http://127.0.0.1:5000')
  .factory('modelService', function(){});
