import unittest
from time import sleep,strftime
from sys import stdout
import subprocess
import os

class idm(unittest.TestCase):
	"""docstring for idm git(https://github.com/ging/fiware-idm.git)"""

	def test_search_install(self):
		if os.path.exists('fiware-idm'):
			os.system('cd fiware-idm && git pull')
		else:
			os.system('git clone https://github.com/ging/fiware-idm.git')
		version = subprocess.check_output("cd ./fiware-idm && git describe --tags", shell=True).strip()
		os.system('cd ./fiware-idm/extras/docker && docker-compose up -d')
		sleep(5)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		host_name = os.popen("hostname").readline()
		sleep(5)
		resultadoid = os.popen("docker ps").readlines()
		total1 = resultadoid[1].split()
		numtotal1 = 0
		for can in total1:
			numtotal1 += 1
		name = total1[numtotal1-1]
		id = total1[0]
		status = 'error'
		for can in total1:
			if can == 'Up':
				status = 'Up'
		total2 = resultadoid[2].split()
		numtotal2 = 0
		for can in total2:
			numtotal2 += 1
		name2 = total2[numtotal2-1]
		id2 = total1[0]
		status2 = 'error'
		for can in total1:
			if can == 'Up':
				status2 = 'Up'
		contenedor =[host_name, fecha, hora, version,name,id,status,name2, id2, status2 ]
		r = open('report.txt','w')
		r.write(str(contenedor[1]+','+contenedor[2]+','+contenedor[3]+','+contenedor[4]+','+contenedor[5]+','+contenedor[6]+','+contenedor[7]+','+contenedor[8]+','+contenedor[9]+','+contenedor[0]))


	def tearDown(self):
		os.system('cd ./fiware-idm/extras/docker && docker-compose down')

if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

