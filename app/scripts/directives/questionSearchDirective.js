'use strict';

angular.module('smarteslApp')
  .directive('questionsearch', function(){

    return {
      restrict: 'E',
      scope: {
        searchquestion: '=' // inherit from parent
      },
      templateUrl: '/views/components/question_search.html',
      controller: function(appserver,$scope,$http){

        $scope.searchQuestions = function(searchPhrase){
          $scope.searchResults = [];
          $http.post(appserver + '/search/questions', { 'phrase': searchPhrase }).
            success(function(results){
              console.log('search results: ' + JSON.stringify(results));
              $scope.searchResults = results.results;
          });
        };

      }
    }
});
