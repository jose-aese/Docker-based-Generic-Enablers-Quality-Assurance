#from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import strftime
import unittest
import os
import time
import json

class wirecloud(unittest.TestCase):
	"""docstring for ClassName"""
	def test(self):	
		os.system('cd docker-wirecloud && docker-compose down')
		if os.path.exists("docker-wirecloud"):
			os.chdir('docker-wirecloud')	
			os.system('git pull')
		else:
			os.system('git clone https://github.com/Wirecloud/docker-wirecloud')
			os.chdir('docker-wirecloud')
		version = 'latest'

		print('--------------------------------')
		print ('instalando ' + version)
		print('--------------------------------')
		
		os.chdir('dev')
		os.system('docker-compose up -d')
		time.sleep(3)
		os.system('docker-compose exec wirecloud manage.py migrate')
		print('--------------------------------------------------------')
		
		date = strftime("%y-%m-%d")
		hour = strftime("%H:%M:%S")
		
		host = os.popen('hostname')
		host_name = host.readline()
		
		resultados = os.popen('docker ps')
		datos = resultados.readlines()
		resultados = os.popen('docker-compose ps')
		datos1 =resultados.readlines()

		containers = [host_name,date,hour,version,datos1[2].split()[0],datos[1].split()[0],datos1[2].split()[4],datos1[3].split()[0],datos[2].split()[0],datos1[3].split()[5],datos1[4].split()[0],datos[3].split()[0],datos1[4].split()[3],datos1[5].split()[0],datos[4].split()[0],datos1[5].split()[2]]
		
		os.system('docker-compose down')

		os.chdir('../')
		os.chdir('../')
		f = open ('report.txt','w')
		f.write(containers[1]+","+containers[2]+","+containers[3]+
			","+containers[4]+","+containers[5]+","+containers[6]+
			","+containers[7]+","+containers[8]+","+containers[9]+
			","+containers[10]+","+containers[11]+","+containers[12]+
			","+containers[13]+","+containers[14]+","+containers[15]+
			","+containers[0])


if __name__=="__main__":
		test_file = 'test.txt'
		f = open(test_file,'w')
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
		f.close()
# Gustavo Bautista Gutierrez 

