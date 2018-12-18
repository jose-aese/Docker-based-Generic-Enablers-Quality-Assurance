from time import strftime
import time
import os
import json
import unittest
import subprocess

class orion(unittest.TestCase):
	
#	def setUp(self):
#		self.driver = webdriver.Remote(
#				command_executor='http://localhost:4444/wd/hub',
#				desired_capabilities=DesiredCapabilities.CHROME)
	def test_search_install(self):	
		os.system("cd docker && docker-compose down")
		if os.path.exists("fiware-orion"):
			os.chdir('fiware-orion')
			os.system('git pull')
		else:
			os.system('git clone https://github.com/telefonicaid/fiware-orion')
			os.chdir('fiware-orion')

		version = subprocess.check_output("git describe --tags", shell=True).strip()

		#driver = self.driver
		#driver.get("https://github.com/telefonicaid/fiware-orion")
		#branch = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/button').click()
		#version = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[4]/div[1]/a[1]').get_attribute('data-name')
		#tags = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[2]').click()
		#ver = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[4]/div[1]/a[1]').click()
		#clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		#gitclone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		#driver.quit() 

		print('--------------------------------')
		print('version: ' + version)
		print('--------------------------------')
		#os.system('mkdir Docker | mkdir report')
		#os.system("git clone " + gitclone)
		os.system("cd docker && docker-compose up -d")
		print('--------------------------------')
		os.system('docker-compose ps')
		time.sleep(10)
		print('--------------------------------')
		os.system('curl http://localhost:1026/version')
		print('--------------------------------')

		date = strftime("%y-%m-%d")
		hour = strftime("%H:%M:%S")
		
		host = os.popen('hostname')
		host_name = host.readline()
		
		resultados = os.popen('docker ps')
		datos = resultados.readlines()
		
		containers = [host_name,date,hour,version,datos[1].split()[10],datos[1].split()[0],datos[1].split()[6],datos[2].split()[10],datos[2].split()[0],datos[2].split()[6]]
		os.system("cd docker && docker-compose down")

		os.chdir('../')
		f = open ('report.txt','w')
		f.write(containers[1]+","+containers[2]+","+containers[3]+","+containers[4]+","+containers[5]+","+containers[6]+","+containers[7]+","+containers[8]+","+containers[9]+","+containers[0])

		print('fin del script')

if __name__ == "__main__":	
	test_file = 'test.txt'
	f = open(test_file,'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()	

# Gustavo Bautista Gutierrez
