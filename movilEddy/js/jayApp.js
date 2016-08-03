/*LONDONCG 2016- SCRIPT BY Eddy Medina
COMPONENTE CONTROLADOR ANGULAR
*/

var myApp = angular.module('MyApp',['cgBusy']);

myApp.controller('listadoCtrl', function($scope, $http) {
	$scope.myPromise =  $http.get('/cgi-bin/RH/27/movilEddy/GET/movilGET.py',{	params: {"accion":"empleados"}}).success(function(data) {
		$scope.empleados = data;
	});


$scope.puestoHelper = function(){
	if ($scope.willSmith == "eddy"){
		$scope.puestoFiltro = undefined;
		
	}else{
		$scope.puestoFiltro = $scope.willSmith;
		}

}
	
	
 $scope.reload=function(empn){
				window.location.href = '/RH/27/movilEddy/consulDetalle.htm?empn='+empn;
			};

})

 myApp.controller('detallesConsultor', function($scope, $http) {

	$scope.dato = "si";
		$http.get('/cgi-bin/RH/27/movilEddy/GET/movilGET.py',{	params: {"accion": "detallesConsultor","empn": empn}}).success(function(data) {
		$scope.empleado = data;
		});

})