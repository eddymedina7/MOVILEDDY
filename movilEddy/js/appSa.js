
myapp.controller('listadoCtrl', function($scope, $http) {
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