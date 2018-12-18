import unittest
from sys import stdout
from time import sleep,strftime
import os

class knowage(unittest.TestCase):
	"""docstring for knowage git (https://github.com/KnowageLabs/Knowage-Server-Docker.git)"""

	def test_search_install(self):
		if os.path.exists('Knowage-Server-Docker'):
			os.system('cd Knowage-Server-Docker && git pull')
		else:
			os.system('git clone https://github.com/KnowageLabs/Knowage-Server-Docker.git')
		os.system('cd Knowage-Server-Docker/6.1.1 && docker-compose up -d')
		sleep(60)
		os.system('curl http://0.0.0.0:8080/knowage')
		sleep(15)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		version = "6.1.1"
		host_name = os.popen("hostname").readline()
		resultado = os.popen("cd Knowage-Server-Docker/6.1.1 && docker-compose ps").readlines()
		resultadoid = os.popen("docker ps").readlines()
		contenedor = [host_name, fecha, hora, version, resultado[2].split()[0], resultadoid[1].split()[0], resultado[2].split()[3], resultado[3].split()[0], resultadoid[2].split()[0], resultado[3].split()[3]]
		r = open('report.txt','w')
		r.write(str(contenedor[1]+','+contenedor[2]+','+contenedor[3]+','+contenedor[4]+','+contenedor[5]+','+contenedor[6]+','+contenedor[7]+','+contenedor[8]+','+contenedor[9]+','+contenedor[0]))


	def tearDown(self):
		os.system('cd Knowage-Server-Docker/6.1.1/ && docker-compose down')

if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

#Samuel Castillo Texocotitla