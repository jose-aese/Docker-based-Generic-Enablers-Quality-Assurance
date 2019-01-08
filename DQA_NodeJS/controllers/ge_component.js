'use stric'
//Importtar modelo ge_component.js.
var ge_component = require('../models/ge_component');
//Importar libreria File Server para trabajar con el sistema de archivos del servidor.
var fs = require('fs');
//Importar libreria path para manipular las rutas de los ficheros.
var path = require('path');
// Registro de nuevo ge_component
//Función utilizada para registrar un nuevo habilitador en la base de datos.
function saveGeComponent(req, res){
    //Extraer datos contenidos en el objeto JSON de la petición entrante.
    var params = req.body;
    //Instanciando modelo ge_component.js
    var ge_comp = new ge_component();
    
    //Comprovar que todos los parametros necesarios hayan sido enviados por el usurio.
    if(params.ge && params.url){ 
        //Capturar nombre de GE y convertir cadena entrante en minusculas.
        ge_comp.ge = params.ge.toLowerCase();
        //Capturar parametro URL. 
        ge_comp.url = params.url;
        //Igualar atributo image al valor null
        ge_comp.image = null;
        
        // control de ge_component duplicado
        ge_component.find(
            //Consulta a la colección (ges) de la base de datos (ge_docker) para verificar que no exista el nuevo GE 
            {ge: ge_comp.ge.toLowerCase()}
            //El resultado de la consulta se guarda en la varible (ges_comp).
        ).exec((err, ges_comp) => {
            //Si ocurre algun error durante la petición se retorna.
            if(err) 
                return res.status(500).send({message:'Error en la petición'});
            //Verificar si existe algún dato en la varible (ges_comp).
            if(ges_comp && ges_comp.length >= 1){ 
                //Si existe dato en (ges_comp) signifiaca que ya existe el GE, se retornara un mensaje al usuario
                return res.status(500).send({message:'El GE component ya existe'});
            }else{
                //Función para guardar objeto (ge_comp) en la colección (ges). 
                ge_comp.save((err, ge_compStored) => {//Retorna un (err) o un objeto (ge_compStored).
                    //Si ocurre algún error durante el proceso de guardar el objeto se retornara el error obtenido. 
                    if(err) return res.status(500).send({message:'error al guardar GE component'});
                    //Si se guardo correctamente el objeto (ge_comp) en la colección la base retornara un objeto JSON
                    //y se guardara en la varible (ge_compStored).
                    if(ge_compStored){//Comprobar que exista varible (ge_compStored)
                        //Retornar objeto (ge_compStored) como confirmación de transacción realizada con exito.
                        res.status(200).send({ge_comp:ge_compStored});
                    }else{
                        //Retornar mensaje de transaccción no realizada con exito.
                        res.status(404).send({message:'No se ha registrado el GE component'});
                    }
                });
            }
        });
    //Retornar mensaje pidiendo al usuario que ingrese todos los parametros necesarios    
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
