'use strict';

angular.module('smarteslApp')
  .controller('CreateQuestionCtrl', function (appserver,$scope,$http,newQuestionPanelSvc) {
    // set the panel to NOT show up as if it were clicked from the outline
    newQuestionPanelSvc.showNewQuestion = false;
  });