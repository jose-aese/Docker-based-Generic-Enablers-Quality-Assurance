'use stric'

var ge_component = require('../models/ge_component');
var fs = require('fs');
var path = require('path');

// Registro de nuevo ge_component
function saveGeComponent(req, res){
    var params = req.body;
    var ge_comp = new ge_component();
    
    

    if(params.ge && params.url){
        ge_comp.ge = params.ge.toLowerCase();
        ge_comp.url = params.url;
        ge_comp.image = null;
        
        // control de ge_component duplicado
        ge_component.find(
            {ge: ge_comp.ge.toLowerCase()}
        ).exec((err, ges_comp) => {
            if(err) 
                return res.status(500).send({message:'Error en la petición'});

            if(ges_comp && ges_comp.length >= 1){
                return res.status(500).send({message:'El GE component ya existe'});
            }else{
                ge_comp.save((err, ge_compStored) => {
                    if(err) return res.status(500).send({message:'error al guardar GE component'});
                        
                    if(ge_compStored){
                        res.status(200).send({ge_comp:ge_compStored});
                    }else{
                        res.status(404).send({message:'No se ha registrado el GE component'});
                    }
                });
            }
        });
        
    }else{
        res.status(200).send({
            message:'Envia todos los campos necesarios!!!'
        });
    }
}

//Obtener datos de los componentes  
function getComponets(req, res){
    ge_component.find({}).select({'_id':0}).exec((err, components)=>{
        if(err) return res.status(500).send({message:'Error en la petición'});

        return res.status(200).send({components});
    });
}

// Subir imagen de usuario GE Component
function uploadImage(req, res){
    //var userId = req.params.id;
    var ge_name = req.params.ge.toLowerCase(); 
    console.log(ge_name);

    if(req.files){
        var file_path = req.files.image.path; //path completo
        var file_split = file_path.split('\/'); 
        var file_name = file_split[2];
        var ext_split = file_name.split('\.');
        var file_ext = ext_split[1];

        //if (userId != req.user.sub){
        //    return removeFilesOfUploads(res, file_path, 'No tienes permiso para actualizar datos del usario');
            //return res.status(500).send({message:'No tienes permiso para actualizar datos del usario'});
        //}    

        if(file_ext == 'png' || file_ext == 'jpg' || file_ext == 'jpeg' || file_ext =='gif'){
            //actualizar documento de usuario logeado
            ge_component.findOneAndUpdate({ge:ge_name}, {image: file_name},{new:true}, (err, geUpdate) =>{
                if(err) return res.status(500).send({message:'Error en la paticion'});

                if(!geUpdate) return res.status(404).send({message:'No se ha podido actualizar el GE component'});
        
                return res.status(200).send({geUpdate});
            });
        }else{
            return removeFilesOfUploads(res, file_path,'Extención no valida');
        }
    }else{
        return res.status(200).send({message:'No se ha subido imagen'});
    }
}

function removeFilesOfUploads(res, file_path, message){
    fs.unlink(file_path, (err) => {
        return res.status(200).send({message:message});
    });
}

//Extraer imagen 
function getImagenFile(req, res){
    var image_file = req.params.imageFile;
    var path_file = './uploads/ge_components/'+image_file;

    fs.exists(path_file, (exists) =>{
        if(exists){
            res.sendFile(path.resolve(path_file))
        }else{
            res.status(200).send({message:'No existe la imagen..'});
        }    
    });
}

module.exports = {
    saveGeComponent,
    getComponets,
    uploadImage,
    getImagenFile

}