from pymongo import MongoClient
import os
from  collections import OrderedDict
import numpy as np
import test

mongoClient = MongoClient('localhost',27017) # Conexion al Server de MongoDB pasandole el host y el puerto
db = mongoClient.ge_docker # Conexion a la base de datos
collection = db.ges # Conexion a la coleccion
print('------------- install KeyRock -------------')
os.system("python test-GE.py")

report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('log_file.txt',delimiter='\t',dtype=str)

reporte ={
	'ge_name' : 'Keyrock',
	'version' : report[2],
	'host_name' : report[9],
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
	}
	]
}
collection.insert(reporte)

