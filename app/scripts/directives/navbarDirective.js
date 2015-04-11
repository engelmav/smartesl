'use strict';

angular.module('smarteslApp')
  .directive('navbar', function(){

        return {
            restrict: 'E',
            scope: {
                navbar: '=' // inherit from parent
            },
            templateUrl: '/views/navbar.html',
            
            controller: function($scope,Session){
              console.log('navbar loaded');

              $scope.Session = Session;

            },
            controllerAs: 'NavBarCtrl'
        };


    });
