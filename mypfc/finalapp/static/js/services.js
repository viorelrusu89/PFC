angular.module('NCommitsApp.services', []).
	factory('djangoAPIservice', function($http) {

		var djangoAPI = {};

		djangoAPI.getNCommits = function() {
			return $http({
				url: 'http://localhost:1234/ncommits'
			});
		}

		djangoAPI.getTimeSeries = function() {
			return $http({
				url: 'http://localhost:1234/timeseries'
			});
		}

		return djangoAPI;
	});