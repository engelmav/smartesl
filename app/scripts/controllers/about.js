'use strict';

/**
 * @ngdoc function
 * @name smarteslApp.controller:AboutCtrl
 * @description
 * # AboutCtrl
 * Controller of the smarteslApp
 */
angular.module('smarteslApp')
  .controller('AboutCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
