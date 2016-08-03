#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
#2016 LondonCG 
import cgi,pickle,MySQLdb,string,time,os,calendar,collections,json
import lcgHtml,lcgCgi,lcgSql
from datetime import date
from decimal import *
form = lcgCgi.camposDeForma()
def inicio():
	print "Content-type: application/json"
	print ""
#form = cgi.FieldStorage()
inicio() 
accion = form.getvalue('accion');
empn =form.getvalue('empn');
sesion = lcgSql.conectar()

def empleados():
	empleados = lcgSql.cursor(sesion,"SELECT nombre1, nombre2, apellido1, apellido2 ,puesto, nivel,fechaNacimiento,empn FROM EMPLEADOS where status ='A' ORDER BY FIELD(puesto,'P','DR','DC','DCO','DO','DA','DRH','A','GO','C','HG','ADM','S','PL','L','F','DH','RH','T',''),apellido1 ASC")
	arreglo=[]
	if sesion.rowcount > 0:
		for row in empleados: 
			d={}
			d['nombre1'] = row[0]
			d['nombre2'] = row[1]
			d['apellido1'] = row[2]
			d['apellido2'] = row[3]
			d['nombreCompleto'] = d['apellido1']+' '+d['nombre1'] +' '+ d['nombre2']
			d['puesto'] = row[4]

			d['nivel'] = row[5]
			d['fechaNacimiento']= str(row[6])
			d['pincheNumeroDeEmpleado']= str(row[7])
		
			lol=lcgCgi.fotoAngularJS(d['pincheNumeroDeEmpleado'])
			d['foto']  = lol

			if d['puesto'] == 'P':
				d['nivel'] = 'Presidente'
			if d['nivel'] == 'DIR':
				d['nivel'] = 'Director Regional'
			if d['pincheNumeroDeEmpleado']=='483':
				d['nivel'] = ''
			arreglo.append(d) 
		return arreglo

def empleado():
	empleados = lcgSql.cursor(sesion,"SELECT nombre1, nombre2, apellido1, apellido2 ,p.puesto, nivel,fechaNacimiento,empn, ALTMAIL, IDskype, telcasa,telcel,tel1Asignacion,edoCivil, esquema, rota, INGRESO, nivel, p.nombre, tipoConsultor,  nacionalidad, ciudadBase, englishSpoken  FROM EMPLEADOS e LEFT JOIN puestos p ON e.puesto = p.puesto where empn ='%s' "%empn)
	
	if sesion.rowcount > 0:
		row = empleados[0]
		d={}
		d['nombre1'] = row[0]
		d['nombre2'] = row[1]
		d['apellido1'] = row[2]
		d['apellido2'] = row[3]
		d['nombreCompleto'] = d['nombre1'] +' '+ d['nombre2'] +' '+d['apellido1']
		d['puesto'] = row[4]
		
		d['nivel'] = row[5]
		d['fechaNacimiento']= str(row[6])
		d['pincheNumeroDeEmpleado']= str(row[7])
		d['ALTMAIL'] = row[8]
		d['IDskype'] = str(row[9])
		if d['IDskype'] is None or  d['IDskype'] == None or d['IDskype'] == "None":
			d['IDskype'] == ""
		d['telcasa'] = row[10]
		d['telcel'] = row[11]
		d['tel1Asignacion'] = row[12]
		d['edoCivil'] = row[13]
		d['esquema'] = row[14]
		d['rota'] = row[15]
		d['INGRESO'] = str(row[16])
		d['nivel'] = row[17]
		d['puesto'] = row[18]
		d['tipoConsultor'] = row[19]
		d['nacionalidad'] = row[20]
		d['ciudadBase'] = row[21]
		d['englishSpoken'] = row[22]

		#Funcion de FOTO
		lol=lcgCgi.fotoAngularJS(d['pincheNumeroDeEmpleado'])
		d['foto']  = lol
		


	return d
	
def config():
	visaPasaportes=  lcgSql.cursor(sesion,"SELECT nacionalidad, tipo, renovable, fechaTermino,numero, docVoP FROM VISAPASAPORTE where empN = '%s' " %empn) 
	d = {}
	if sesion.rowcount > 0:
		row = visaPasaportes[0]
		
		d['nacionalidad'] = row[0]
		d['tipo'] = row[1]
		d['renovable'] = row[2]
		d['fechaTermino'] = str(row[3])
		d['numero'] = row[4]
		d['docVop'] = row[5]
	return d

def puesto():
	puesto = lcgSql.cursor(sesion,"SELECT DISTINCT p.nombre,p.puesto FROM EMPLEADOS e LEFT JOIN puestos p ON e.puesto = p.puesto ORDER BY p.nombre")
	arreglo = []
	d= {}
	d['nombre'] = " Todos"
	d['puesto'] = "eddy"
	
	arreglo.append(d)
	for p in puesto:
		d= {}
		d['nombre'] = p[0]
		d['puesto'] = p[1]
		if d['nombre']  is None or d['nombre']  == "None":
			d['nombre']  = ""
		else:
			arreglo.append(d)
	return arreglo


def asignaciones():
	asigna =  lcgSql.cursor(sesion,"SELECT fechaIni, fechaFin, nivelAlAsignar, claveRegion, if(a.claveProyecto != '' , nombre,t.descripcion), clavePais,a.claveActividad FROM ASIGNACION a LEFT JOIN infSem.proyecto i ON a.claveProyecto = i.claveProyecto LEFT JOIN TIPOACTIVIDAD t ON a.claveActividad = t.claveActividad where empNo ='%s'  ORDER BY fechaIni DESC" %empn)
	arreglo=[]
	if sesion.rowcount > 0:
		for row in asigna: 
			d={}
			d['fechaIni'] = str(row[0])
			d['fechaFin'] = str(row[1])
			d['nivelAlAsignar'] = row[2]
			d['claveRegion'] = row[3]
			d['nombre'] = row[4]
			d['clavePais'] = row[5]

			
			arreglo.append(d) 
		return arreglo

def honorarios():
	honorarios=  lcgSql.cursor(sesion, "SELECT sueldo,concat(alta),come1,come2,come3,mark FROM INCREMENTO WHERE empN='%s' " %empn)
	if sesion.rowcount > 0:
		row = honorarios[0]
		d={}
		d['sueldo'] = row[0]
		d['alta'] = str(row[1])
		d['come1'] = row[2]
		d['come2'] = row[3]
		d['come3'] = row[4]
	return d


def todas():
	d = {}
	if accion == "empleados":
		d['empleados'] = empleados()
	if accion == "detallesConsultor":
		d['empleado'] = empleado()
		d['config'] = config()
		d['asignaciones'] = asignaciones()
		d['honorarios'] = honorarios()
	d['puesto']=puesto()
	
	return d

print json.dumps(todas(), separators=(',',':'),encoding='iso-8859-1')