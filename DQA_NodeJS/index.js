'use stric'

var mongoose = require('mongoose'); //Libreria para conectarse a la base de datos
var app = require('./app'); //Archivo que contiene la configuración inicial del back-end
var port = 3800; //Puerto mediante el cual se desplegara el servicio

// Conexión Dattabase
mongoose.Promise = global.Promise;//Promesa para realizar la conexión a la base de datos
mongoose.connect('mongodb://localhost:27017/ge_docker'/*,{useNewUrlParser:true}*/)//Se especifica el puerto de MongoDB y la base sonbre la cual se va a trabajar
        .then(()=> {
            console.log("la conexion a la DB se a realizado con exito") //Mensaje de conexión exitosa 
            
            // Crear servidor
            app.listen(port,() =>{//Desplegando el servidor
                console.log("servidor corriendo en puerto 3800"); //Mensaje de ejecución exitoso
            });
        })
        .catch(err => console.log(err)); //Si hubo un error en la conexión se retorna el error obtenido
