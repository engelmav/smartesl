'use strict';

angular.module('smarteslApp')
  .directive('navbar', function(){
        return {
            restrict: 'E',
            scope: {
                navbar: '=' // inherit from parent
            },
            templateUrl: '../app/views/navbar.html',

            controller: function($scope,Session){
              console.log('navbar loaded');

              $scope.Session = Session;
              console.log('Session.loggedOn: ' + Session.loggedOn);

            },
            controllerAs: 'NavBarCtrl'
        };


    });
