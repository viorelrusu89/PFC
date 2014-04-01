angular.module('NCommitsApp.controllers', []).
controller('ncommitsController', function($scope, ergastAPIservice) {
	$scope.ncommits = 0;

ergastAPIservice.getDrivers().success(function (response) {
        //Dig into the responde to get the relevant data
        $scope.ncommits = response.ncommits;
    });

});