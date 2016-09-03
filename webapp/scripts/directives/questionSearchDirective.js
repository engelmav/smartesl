'use strict';

angular.module('smarteslApp')
  .directive('questionsearch', function(){

    return {
      restrict: 'E',
      scope: {
        searchquestion: '=' // inherit from parent
      },
      templateUrl: '../views/components/question_search.html',
      controller: function(appserver,$scope,$http,questionTimelineSvc){

        $scope.searchQuestions = function(searchPhrase){
          $scope.searchResults = [];
          $http.post(appserver + '/search/questions', { 'phrase': searchPhrase }).
            success(function(results){
              console.log('search results: ' + JSON.stringify(results));
              $scope.searchResults = results.results;
          });
        };

        $scope.addQuestionFromSearch = function(index){
          console.log('User adding ' + JSON.stringify($scope.searchResults[index][0]));
          var questionId = $scope.searchResults[index][0];
          questionTimelineSvc.addQuestion(questionId);
        };

      }
    }
});
