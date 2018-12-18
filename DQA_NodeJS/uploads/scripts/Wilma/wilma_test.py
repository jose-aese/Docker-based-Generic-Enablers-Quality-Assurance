from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import strftime
import os
import time
import unittest
import subprocess

class Wilma(unittest.TestCase):
	def test(self):
		os.system('docker rm -f pep-proxy')
		if os.path.exists("fiware-pep-proxy"):
			os.chdir('fiware-pep-proxy')
			os.system('git pull')
		else:
			os.system('git clone https://github.com/ging/fiware-pep-proxy')			
			os.chdir('fiware-pep-proxy')

		version = subprocess.check_output("git describe --tags", shell=True).strip()	
		print('--------------------------------')
		print ('install version '+ version)
		print('--------------------------------')
		dir = os.getcwd()
		runWilma = 'docker run -d --name pep-proxy -v /home/root/workspace/fiware-pep-proxy/config.js:/opt/fiware-pep-proxy/config.js -p 80:80 pep-proxy-image'
		runWilma1 = runWilma.replace('/home/root/workspace/fiware-pep-proxy', dir) 
		print('--------------------------------')
		os.system("mv config.js.template config.js")
		os.system(runWilma1)
		os.chdir("extras/docker")
		buildWilma='docker build -t pep-proxy-image .'
		os.system(buildWilma)
		print('--------------------------------')
		os.system('docker start pep-proxy')
		os.system('docker ps -l')
		print('--------------------------------')
		time.sleep(5)
		os.system('curl http://localhost:80') 
		print(' ')
		print('--------------------------------')


		os.chdir('../')
		os.chdir('../')
		os.chdir('../')
		
		date = strftime("%y-%m-%d")
		hour = strftime("%H:%M:%S")
		
		host = os.popen('hostname')
		host_name = host.readline()
		
		resultados = os.popen('docker ps -l') 
		datos = resultados.readlines()
		containers = [host_name,date,hour,version,datos[1].split()[12],datos[1].split()[0],datos[1].split()[7]]


		os.system('docker rm -f pep-proxy')

		f = open ('report.txt','w')
		f.write(containers[1]+","+containers[2]+","+containers[3]+
			","+containers[4]+","+containers[5]+","+containers[6]+
			","+containers[0])



if __name__=="__main__":
		test_file = 'test.txt'
		f = open(test_file,'w')
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
		f.close()
# Gustavo Bautista Gutierrez
