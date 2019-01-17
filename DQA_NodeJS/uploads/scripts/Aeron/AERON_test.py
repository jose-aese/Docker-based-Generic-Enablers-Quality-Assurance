from time import strftime
import time
import subprocess
import unittest
import json
import os

class aeon(unittest.TestCase):
    def test(self):
        os.system('docker rm AERON -f')
        if os.path.exists('Aeron'):
            os.chdir('Aeron')
            os.system('git pull')
        else:
            os.system('git clone https://github.com/Aeronbroker/Aeron')
            os.chdir('Aeron')
        
        os.system('docker run -d -t -p 8065:8065 -p 8060:8060 -p 5984:5984 --name AERON fiware/iotbroker:standalone-dev')
        version = os.popen('git tag').readlines().pop().rstrip('\n') #Obtener la ultima version
        hour = strftime('%H:%M:%S')
        date = strftime('%y-%m-%d')
        host_name = os.popen('hostname').readline().rstrip('\n')
        
        container_info = os.popen('docker ps -f "name=AERON"').readlines()
        info_split = container_info[1].split()
        container_status = 'error'
        for can in info_split:
            if can == 'Up':
                container_status = 'Up'
        container_id =  info_split[0]
        time.sleep(20)
        os.system('curl 127.0.0.1:8060/sanityCheck')
        container_name = os.popen('docker rm AERON -f').readline().rstrip('\n')    

        #test_info = [version,hour,date,host_name,container_id,container_status,container_name,]
        #print(test_info)}

        os.chdir('../')
        f = open('report.txt','w') #Abrir archivo report.txt
        f.write(date+','+hour+','+version+','+container_name+','+container_status+','+container_id+','+host_name)#Escribir en archivo   

        
if __name__ == "__main__":
    f = open('test.txt', 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()

     
