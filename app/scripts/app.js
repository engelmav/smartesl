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
      .when('/create_question', {
        templateUrl: 'views/create_question.html',
        controller: 'CreateQuestionCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .value('appserver', 'http://127.0.0.1:5000')
  .factory('dataService', function(){


  })
  .factory('modelService', function(){})
  .directive('question', function(appserver){

        return {
            restrict: 'E',
            scope: {
                progress: '=question'
            },
            templateUrl: '/views/question_body.html',
            
            controller: function($scope,$http,$timeout){

              console.log('Inside the controller of the question directive.');

              $scope.setupQuestion = function(data){
                $scope.question.body = data.body;
                $scope.question.choices = data.choices;
              };


              $scope.submitAnswer = function(answer){
                console.log('Submitted answer: ' + answer);
                $http.post(appserver + '/question/submit_answer', { "answer": answer }).
                  success(function(results){
                    console.log('submitAnswer success response: ' + results)
                  });
              };

              var lastQuestionId;

              var timeout = '';
              var poller = function() {
                $http.get(appserver + '/question/get_question').
                  success(function(data, status, headers, config){
                    console.log(data,status);
                    lastQuestionId = data.id;
                    if (lastQuestionId === data.id){
                      $scope.setupQuestion(data);
                    }
                })
                timeout = $timeout(poller, 2000);
              };
              poller();




            },
            controllerAs: 'question'
        };


    });
