from collections import OrderedDict
from pymongo import  MongoClient
import numpy as np
import json
import os
import time

mongoClient = MongoClient('localhost',27017)
db = mongoClient.ge_docker
collection = db.ges
print('------------- install Wilma -------------')
os.system('python wilma_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)

reporte ={
	'ge_name' : 'Wilma',
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