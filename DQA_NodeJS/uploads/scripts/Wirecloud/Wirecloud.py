from collections import OrderedDict
from pymongo import MongoClient
import numpy as np
import json
import os
import time

mongoClient = MongoClient('localhost',27017) # Conexion al Server de MongoDB pasandole el host y el puerto
db = mongoClient.ge_docker # Conexion a la base de datos
collection = db.ges # Conexion a la coleccion
print('------------- install Wirecloud -------------')
os.system('python wirecloud_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)

reporte ={
	'ge_name' : 'Wirecloud',
	'version' : 'latest',
	'host_name' : report[15],
	'test' : test[len(test)-1],
	'execution_time' : test[len(test)-2].split(" ")[4],
	'date' : report[0],
	'time' : report[1],
	'containers' : [{
		'container_name' : report[3],
		'container_ID' : report[4],
		'status' : report[5]
	},{
		'container_name' : report[6],
		'container_ID' : report[7],
		'status' : report[8]
	},{
		'container_name' : report[9],
		'container_ID' : report[10],
		'status' : report[11]
	},{
		'container_name' : report[12],
		'container_ID' : report[13],
		'status' : report[14]
	}]
}
collection.insert(reporte)
