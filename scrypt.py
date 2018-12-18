import os

print('------------- install MongoDB -------------')

os.system('cd DQA_Compose && docker-compose down')#Eliminar contenedores
os.system('cd DQA_Compose && docker-compose up -d')#Levantar contenedor MongoDB 
os.system('cd DQA_Compose/fiware_report && docker cp output.json fiware_report:/ && docker exec fiware_report bash -c "mongoimport --db ge_docker --collection ge_components --file output.json"')

print('------------- install pip, numpy and pymongo -------------')
os.system('sudo apt install -y python-pip && pip install pymongo numpy selenium')#Instalar dependecias python
#validar existencia de dependencias

print('------------- install dependencies NodeJS -------------')
os.system('cd DQA_NodeJS && npm install')#Instalar dependencias NodeJS
#validar que exista carpeta node_modules

print('------------- Git clone GE -------------') #verificar existencia de la carpeta
os.system('cd DQA_NodeJS/uploads/scripts/Aeron && python Aeron.py')#Ejecutar scrypt AERON test
os.system('cd DQA_NodeJS/uploads/scripts/Authzforce && python Authzforce.py')#Ejecutar scrypt authzforce test
os.system('cd DQA_NodeJS/uploads/scripts/Geoserver && python Geoserver.py')#Ejecutar scrypt geoserver test
os.system('cd DQA_NodeJS/uploads/scripts/Kurento && python Kurento.py')#Ejecutar scrypt kurento test
os.system('cd DQA_NodeJS/uploads/scripts/Orion && python Orion.py')#Ejecutar scrypt orion test
os.system('cd DQA_NodeJS/uploads/scripts/Proton && python Proton.py')#Ejecutar scrypt proton test
os.system('cd DQA_NodeJS/uploads/scripts/Wilma && python Wilma.py')#Ejecutar scrypt wilma test
os.system('cd DQA_NodeJS/uploads/scripts/Wirecloud && python Wirecloud.py')#Ejecutar scrypt wirecloud test
os.system('cd DQA_NodeJS/uploads/scripts/Keyrock && python Keyrock.py')#Ejecutar scrypt wilma test
os.system('cd DQA_NodeJS/uploads/scripts/Knowage && python Knowage.py')#Ejecutar scrypt wirecloud test

print('------- Start service DockerQA ----------')
print('--- To stop the service type ctr+c -----')
os.system('cd DQA_NodeJS && node index.js')#Levantando servicio

os.system('cd DQA_Compose && docker-compose down')#Eliminar contendores

