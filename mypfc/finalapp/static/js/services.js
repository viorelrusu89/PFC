angular.module('NCommitsApp.services', []).
	factory('ergastAPIservice', function($http) {

		var ergastAPI = {};

		ergastAPI.getDrivers = function() {
			return $http({
				url: 'http://localhost:1234/ncommits'
			});
		}

		return ergastAPI;
	});