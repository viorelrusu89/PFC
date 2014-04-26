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


djangoAPIservice.getTimeSeries().success(function (response){
		$scope.timeseries = response.values;

});
g = new Dygraph(
    document.getElementById("demodiv"),
    function() {

      //Trying to fill out data from server
/*      r = "date,ncommits\n";
      for (var i=0; i<$scope.timeseries.values.length; i++) {
                      r += $scope.timeseries["values"][i][0] + "," + $scope.timeseries["values"][i][1] + "\n";
            }

      r = r.replace(/T00:00:00/g, " ");
      return r;*/
 
      //hand-written "object". TODO: generate it from server
      r =  "date,ncommits\n" + 
           "2012-08-01, 16\n" +
           "2012-09-01, 21\n" +
           "2012-10-01, 9\n" +
           "2012-11-01, 2\n" +
           "2012-12-01, 33\n" +
           "2013-01-01, 6\n" +
           "2013-02-01, 6\n" +
           "2013-03-01, 75\n" +
           "2013-04-01, 196\n";
      return r;

      /*
      // Dygraphs working model code
      var zp = function(x) { if (x < 10) return "0"+x; else return x; };
      var r = "date,parabola\n";
      for (var i=1; i<=31; i++) {
      r += "200610" + zp(i);
      r += "," + 10*(i*(31-i));
      r += "\n";

      }
      return r;
      */

    },
    {
      strokeWidth: 2,
      'ncommits': {
        strokeWidth: 0.0,
        drawPoints: true,
        pointSize: 6,
        highlightCircleSize: 6
      },
    }
);


});