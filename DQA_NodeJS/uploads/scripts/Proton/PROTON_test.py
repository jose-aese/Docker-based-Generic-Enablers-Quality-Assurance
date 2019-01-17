import os
import time
import json
import unittest
import subprocess
from time import strftime

class geoserver(unittest.TestCase):
    def test(self):
        #Comprovar existencia de directorio
        os.system('docker rm -f proton')
        if os.path.exists('Proton'):
            os.chdir('Proton') 
            os.system('git pull') #Actualizar directorio 
        else:
            os.system('git clone https://github.com/ishkin/Proton') #Clonar directorio
            os.chdir('Proton')
        
        #version = subprocess.check_output('git describe --tags', shell=True).strip() #Obtener version desde github
        version = os.popen('git tag').readlines().pop().rstrip('\n') #Obtener version mediante el git tag
        date = strftime('%y-%m-%d') #Fecha de ejecucion
        hour = strftime('%H:%M:%S') #Hora de ejecucion
        host_name = os.popen('hostname').readline().rstrip('\n') #Nombre del Host de ejecucion
        
        os.chdir('docker')
        os.system('docker build -t fiware/proton .') #Creacion de la imagen mediante el Dockerfile
        os.system('docker run --name proton -p 8080:8080 -it -d fiware/proton') # creacion del contenedor
        
        info = os.popen('docker ps -f "name=proton"') #Extraer la informacion del estado del contenedor
        container_info = info.readlines() #Gaurdar informacion en arreglo
        info_split = container_info[1].split()
        numtotal = 0
        for can in info_split:
            numtotal += 1
        containerID =  info_split[0] #Extraer el conytainer id del arreglo
        containerStatus = 'error'
        for can in info_split:
            if can == 'Up':
                containerStatus = 'Up'	
        time.sleep(5)
        server_response= os.popen('curl -I http://localhost:8080/AuthoringTool/Main.html').readline() #Respuesta por parte del servidor dentro del contenedor
        containerName = os.popen('docker rm proton -f').readline().rstrip('\n') #Detener contenedor y guardar su nombre        
        test_info =[host_name,date,hour,version,containerStatus,containerID,containerName] #Guardar valores obtenidos del test en arreglo
        print (test_info)    

        os.chdir('../')
        os.chdir('../')
        f = open('report.txt','w') #Abrir archivo report.txt
        f.write(date+','+hour+','+version+','+containerName+','+containerID+','+containerStatus+','+host_name)#Escribir en archivo   

if __name__ == "__main__":
    f = open('test.txt', 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
