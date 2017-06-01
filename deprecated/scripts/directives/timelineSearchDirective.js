'use strict';

angular.module('smarteslApp')
  .directive('timelinesearch', function(){

    return {
      restrict: 'E',
      scope: {
        searchtimeline: '=' // inherit from parent
      },
      templateUrl: '/views/components/timeline_search.html',
      controller: function(appserver,$scope,$http,questionTimelineSvc){

        $scope.searchTimelines = function(searchPhrase){
          $scope.searchResults = [];
          $http.post(appserver + '/search/timelines', { 'phrase': searchPhrase }).
            success(function(results){
              console.log('search results: ' + JSON.stringify(results));
              $scope.searchResults = results.results;
          });
        };

        $scope.addTimelineFromSearch = function(index){
          console.log('User adding ' + JSON.stringify($scope.searchResults[index][0]));
        };

      }
    }
});
