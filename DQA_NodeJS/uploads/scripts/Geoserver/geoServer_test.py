import os
import time
import json
import unittest
import subprocess
from time import strftime

class geoserver(unittest.TestCase):
    def test(self):
        os.system('docker rm geoServer -f')
        #Comprovar existencia de directorio
        if os.path.exists('GISDataProvider'):
            os.chdir('GISDataProvider') 
            os.system('git pull') #Actualizar directorio 
        else:
            os.system('git clone https://github.com/Cyberlightning/GISDataProvider') #Clonar directorio
            os.chdir('GISDataProvider')
        
        #version = subprocess.check_output('git describe --tags', shell=True).strip() #Obtener version desde github
        version = os.popen('git tag').readlines().pop().rstrip('\n')
        date = strftime('%y-%m-%d') #Fecha de ejecucion
        hour = strftime('%H:%M:%S') #Hora de ejecucion
        host_name = os.popen('hostname').readline().rstrip('\n') #Nombre del Host de ejecucion

        os.system('docker run -d -it -p 9090:8080 --name geoServer fiware/gisdataprovider') #Creacion del contenedor
        
        info = os.popen('docker ps -f "name=geoServer"') #Extraer la informacion del estado del contenedor
        container_info = info.readlines() #Gaurdar informacion en arreglo
        containerID = container_info[1].split()[0] #Extraer el conytainer id del arreglo
        containerStatus = container_info[1].split()[7] #Extraer el Status del arreglo
        
        time.sleep(5)
        os.system('curl -I localhost:9090/geoserver/web/') #Respuesta por parte del servidor dentro del contenedor

        containerName = os.popen('docker rm geoServer -f').readline().rstrip('\n') #Detener contenedor y guardar su nombre        

        test_info =[host_name,date,hour,version,containerStatus,containerID,containerName] #Guardar valores obtenidos del test en arreglo
        print (test_info)    

        os.chdir('../')
        f = open('report.txt','w') #Abrir archivo report.txt
        f.write(test_info[1]+','+test_info[2]+','+test_info[3]+','+test_info[6]+','+test_info[4]+','+test_info[5]+','+test_info[0])#Escribir en archivo   

if __name__ == "__main__":
    f = open('test.txt', 'w')
    runner = unittest.TextTestRunner(f)
    unittest.main(testRunner=runner)
    f.close()
