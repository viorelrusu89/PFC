angular.module('NCommitsApp.controllers', []).

/* Ncommits controller */
controller('ncommitsController', function($scope, djangoAPIservice) {
	$scope.ncommits = 0;

djangoAPIservice.getNCommits().success(function (response) {
        //Dig into the response to get the relevant data
        $scope.ncommits = response.ncommits;
    });
}).

/* timeseriesController */
controller('timeseriesController', function($scope, djangoAPIservice) {
	$scope.timeseries = 777;

      g = new Dygraph(
              document.getElementById("demodiv"),
              function() {
                var zp = function(x) { if (x < 10) return "0"+x; else return x; };
                var r = "date,parabola,line,another line,sine wave\n";
                for (var i=1; i<=31; i++) {
                r += "200610" + zp(i);
                r += "," + 10*(i*(31-i));
                r += "\n";
                }
                return r;
              },
              {
                strokeWidth: 2,
                'parabola': {
                  strokeWidth: 0.0,
                  drawPoints: true,
                  pointSize: 4,
                  highlightCircleSize: 6
                },
              }
          );


/*
djangoAPIservice.getTimeSeries().success(function (response){
		$scope.timeseries = response.values;

});
*/
});