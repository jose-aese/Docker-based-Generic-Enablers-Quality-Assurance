'use strict'

var express = require('express');//Importar framework de express 
var bodyParser = require('body-parser');//Importar libreria body-parser
var path = require('path');//Importar libreria path 

var app = express();//Instanciar framewok express a una varible 

// cargar rutas (directorio ./routes)
var ge_routes = require('./routes/ge');//Importar archivo ge.js 
var user_routes = require('./routes/user');//Importar archivo user.js
var ge_component_routes = require('./routes/ge_componets');//Importar archivo ge_componets.js
var test = require('./routes/ge_test');//Importar archivo ge_test.js

// middlewares
app.use(bodyParser.urlencoded({extended:false}));//Configuracion necesaria para la libreria body-parser
app.use(bodyParser.json());//Convierte la peticion a un objeto JSON

// cors configurar cabeceras http
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
 
    next();
});

// rutas
app.use('/',express.static('client',{redirect:false}));
app.use('/api',ge_routes);
app.use('/api',user_routes);
app.use('/api',ge_component_routes);
app.use('/api',test);
app.get('*',function(req,res,next){
    res.sendFile(path.resolve('client/index.html'));
});

//expotar
module.exports = app;
