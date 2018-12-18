from collections import OrderedDict
from pymongo import MongoClient
import numpy as np
import time
import json
import os

mongoClient = MongoClient('localhost',27017) # Conexion al Server de MongoDB pasandole el host y el puerto
db = mongoClient.ge_docker # Conexion a la base de datos
collection = db.ges # Conexion a la coleccion
print('------------- install PROTON -------------')
os.system('python PROTON_test.py')

report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)

reporte ={
	'ge_name' : 'Proton',
	'version' : report[2],
	'host_name' : report[6],
	'test' : test[len(test)-1],
	'execution_time' : test[len(test)-2].split(" ")[4],
	'date' : report[0],
	'time' : report[1],
	'containers' : [{
		'container_name' : report[3],
		'container_ID' : report[4],
		'status' : report[5]
	}]
}
collection.insert(reporte)
