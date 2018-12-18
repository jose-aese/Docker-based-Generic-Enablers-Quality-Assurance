'use stric'

var mongoose = require('mongoose');
var app = require('./app');
var port = 3800;

// Conexión Dattabase
mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost:27017/ge_docker'/*,{useNewUrlParser:true}*/)
        .then(()=> {
            console.log("la conexion a la DB se a realizado con exito")
            
            // Crear servidor
            app.listen(port,() =>{
                console.log("servidor corriendo en puerto 3800");
            });
        })
        .catch(err => console.log(err)); 