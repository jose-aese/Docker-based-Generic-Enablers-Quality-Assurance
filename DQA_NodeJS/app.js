'use strict'

var express = require('express');
var bodyParser = require('body-parser');
var path = require('path');

var app = express();

// cargar rutas
var ge_routes = require('./routes/ge');
var user_routes = require('./routes/user');
var ge_component_routes = require('./routes/ge_componets');
var test = require('./routes/ge_test');
// middlewares
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

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