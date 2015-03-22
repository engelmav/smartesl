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
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .factory('dataService', function(){})
  .factory('modelService', function(){})
  .directive('question', function(){

        return {
            restrict: 'E',
            scope: {
                progress: '=question'
            },
            templateUrl: '/views/question_body.html',
            
            controller: function($scope){
              console.log('Inside the controller of the question directive.');



            },
            controllerAs: 'question'
        };


    });
