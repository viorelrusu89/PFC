angular.module('dashboardApp.services', []).
	factory('djangoAPIservice', function($http) {

		var djangoAPI = {};

		djangoAPI.getNCommits = function() {
			return $http({
				url: '/ncommits'
			});
		}

		djangoAPI.getTimeSeries = function() {
			return $http({
				url: '/timeseries'
			});
		}

		return djangoAPI;
	});