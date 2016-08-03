angular.module('app.controllers', [])
  

.controller('listadoCtrl', function($scope, $http) {
	$scope.dato = "si";
	
	$http.get('/cgi-bin/RH/movilEddy/GET/movilGET.py',{	params: {"accion": "empleados"}}).success(function(data) {
		$scope.empleados = data;});
	
	$scope.mandame = function(empleado){
	
		url = "/RH/27/movilEddy/index.html#/page6";
		location.href = url ;
		alert(empleado.pincheNumeroDeEmpleado)
		$http.get('/cgi-bin/RH/movilEddy/GET/movilGET.py',{	params: {"accion": "detallesConsultor","empn": empleado.pincheNumeroDeEmpleado}}).success(function(data) {
		$scope.emp = data;

		});
		
	};

})
   
.controller('detallesConsultorCtrl', function($scope, $http) {

})

angular.module('ionicApp', ['ionic'])

.controller('MyCtrl', function($scope) {
  $scope.groups = [];
  for (var i=0; i<10; i++) {
    $scope.groups[i] = {
      name: i,
      items: []
    };
    for (var j=0; j<3; j++) {
      $scope.groups[i].items.push(i + '-' + j);
    }
  }
  
  /*
   * if given group is the selected group, deselect it
   * else, select the given group
   */
  $scope.toggleGroup = function(group) {
    if ($scope.isGroupShown(group)) {
      $scope.shownGroup = null;
    } else {
      $scope.shownGroup = group;
    }
  };
  $scope.isGroupShown = function(group) {
    return $scope.shownGroup === group;
  };
  
});