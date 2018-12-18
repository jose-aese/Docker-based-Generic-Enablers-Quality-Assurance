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
		sleep(15)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		host_name = os.popen("hostname").readline()
		sleep(20)
		resultado = os.popen("cd ./fiware-idm/extras/docker && docker-compose ps").readlines()
		resultadoid = os.popen("docker ps").readlines()
		contenedor =[host_name, fecha, hora, version, resultado[2].split()[0], resultadoid[1].split()[0], resultado[2].split()[3], resultado[3].split()[0], resultadoid[2].split()[0], resultado[3].split()[3]]
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

#Samuel Castillo Texocotitla
