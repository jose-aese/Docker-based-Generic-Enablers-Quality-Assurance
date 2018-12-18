import os 

print('------------- install MongoDB -------------')
os.system('docker rm -f fiware_report && docker rm -f fiware_selenium && docker rm -f fiware_chrome')#Eliminar contenedores
os.system('cd DQA_Compose && docker-compose up -d')#Desplegando contendores

print('------------- Start DockerQA -------------')
print('----To stop the service type ctr+c------')
os.system('cd DQA_NodeJS && node index.js')#Levantando servicio

os.system('cd DQA_Compose && docker-compose down')#Eliminar contendores
