'use strict'
var moongosePaginate = require('mongoose-pagination')

var Ge = require('../models/ge');

function home(req,res){
    res.status(200).send({
        message:'Hola mundo desde JS'
    });
}

function pruebas(req,res){
    console.log(req.body);
    res.status(200).send({
        message:'Acción de prueba en el servidor NodeJS'
    });
}

function saveGe(req, res){
    var params = req.body;
    var ge = new Ge();

    if(params.ge_name && params.version 
        && params.host_name && params.test 
        && params.execution_time && params.date && params.time){

        ge.ge_name = params.ge_name;
        ge.version = params.version;
        ge.host_name = params.host_name;
        ge.test = params.name;
        ge.execution_time = params.execution_time;
        ge.date = params.date;
        ge.time = params.time;

        ge.save((err, geStored) =>{
            if(err) return res.status(500).send({message:'Error al guardar reporte'});
            
            if(geStored){
                res.status(200).send({ge:geStored});
            }else{
                res.status(404).send({message:'No se ha registrado reporte'});
            }
        });
    }else{ 
        res.status(200).send({
            message:'Envia todos los campos necesarios'
        });
    }
}
//Obtener todos los datos pagindo
function getGes(req,res){
    var page = 1;
    if(req.params.page){
        page = req.params.page;
    }
    var itemsPerPage = 5;

    Ge.find().sort({'_id':-1}).paginate(page,itemsPerPage,(err,ges,total) =>{
        if(err) return res.status(500).send({message:'Error en la petición'});

        if(total==0) return res.status(404).send({message:'No hay datos en la DB'});

        return res.status(200).send({
            ges,
            total,
            pages: Math.ceil(total/itemsPerPage)
        });
    });
}

//Conseguir datos de un GE paginado
function getGe(req, res){
    var ge_Name = req.params.ge_name;
     
    var page = 1;
    if(req.params.page){
        page = req.params.page;
    }

    var itemsPerPage = 5;
    
    Ge.find({ge_name:ge_Name}).sort({'_id':-1}).paginate(page, itemsPerPage,(err, ge, total) => {
        if(err) return res.status(500).send({message:'Error en la petición'});

        if(total==0) return res.status(404).send({message:'El GE no existe'});

        return res.status(200).send({
            ge,
            total,
            pages: Math.ceil(total/itemsPerPage)
        });
    });
}


//Obtener documento por Id
function getGeId(req, res){
    var id = String;    
    id = req.params.id;
    Ge.find({_id:id}).exec((err, ge)=>{
        if(err) return res.status(500).send({message:'Error en la petición'});
        return res.status(200).send({ge});
    });
}

module.exports = {
    home,
    pruebas,
    saveGe,
    getGes,
    getGe,
    getGeId
}