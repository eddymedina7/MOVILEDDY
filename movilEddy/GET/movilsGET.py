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
#accion = form.getvalue('accion');
sesion = lcgSql.conectar()

def empleados(empn):
	empleados = lcgSql.cursor(sesion,"SELECT nombre1, nombre2, apellido1, apellido2 ,puesto, nivel,fechaNacimiento FROM EMPLEADOS where status ='A' ")
	arreglo=[]
	
	if sesion.rowcount > 0:
	
		for row in empleados 
			d={}
			d['nombre1'] = row[0]
			d['nombre2'] = row[1]
			d['apellido1'] = row[2]
			d['apellido2'] = row[3]
			d['puesto'] = row[4]
			d['nivel'] = row[5]
			d['fechaNacimiento']= str(row[6])
		#Funcion de FOTO
			lol=lcgCgi.fotoAngularJS(empn)
			d['foto']  = lol
			arreglo.append(d)
		return arreglo


def todas():
	d = {}
	d['empleados'] = empleados()
	return d

print json.dumps(todas(), separators=(',',':'),encoding='iso-8859-1')