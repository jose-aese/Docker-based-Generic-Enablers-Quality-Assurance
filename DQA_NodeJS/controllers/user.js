'use stric'
var bcrypt = require('bcrypt-nodejs');
var mongoosePaginate = require('mongoose-pagination');
var fs = require('fs');
var path = require('path');

var User = require('../models/user');
var jwt = require('../services/jwt');

function home(req,res){
    res.status(200).send({
        message: 'controlador de usuario'
    });
}

function pruebas(req, res){
    console.log(req.body);
    res.status(200).send({
        message:'Accion de pruebas'
    });
}

// Registro de nuevo usuario
function saveUser(req, res){
    var params = req.body;
    var user = new User();

    if(params.name && params.nick && params.password && params.email){
        user.name = params.name;
        user.nick = params.nick;
        user.email = params.email;
        user.role = 'ROLE_ADMIN';
        user.image = null;

        // control de usuarios duplicados
        User.find({ $or:[
            {email: user.email.toLowerCase()},
            {nick: user.nick.toLowerCase()}
        ]}).exec((err, users)=>{
            if(err) return res.status(500).send({message:'Error en la petición de usuarios'});
        
            if(users && users.length >= 1){
                return res.status(200). send({message:'El usuario ya existe'});
            }else{
                // cifrar password y guardar datos
                bcrypt.hash(params.password, null, null, (err, hash) =>{
                    user.password = hash;

                    user.save((err, userStored)=>{
                        if(err) return res.status(500).send({message:'error al guardar usuario'});
                        
                        if(userStored){
                            res.status(200).send({user:userStored});
                        }else{
                            res.status(404).send({message:'No se ha registrado el usuario'});
                        }
                    });
                });                
            }
        });
    }else{
        res.status(200).send({
            message:'Envia todos los campos necesarios!!!'
        });

    }
}
 // login
function loginUser(req, res){
    var params = req.body;
    
    var email = params.email;
    var password = params.password;

    User.findOne({email:email},(err, user) => {
        if(err) return res.status(500).send({message:'Error en la petición'});

        if(user){
            bcrypt.compare(password, user.password, (err, check) => {
                if(check){
                    if(params.gettoken){
                        //generar y devolver token
                        return res.status(200).send({
                            token: jwt.createToken(user)    
                        });

                    }else{
                        //devolver datos de usuario
                        user.password = undefined;
                        return res.status(200).send({user});
                    }
                }else{
                    return res.status(404).send({message:'El usuario no ha podido identificarse'});
                }
            });
        }else{
            return res.status(404).send({message:'El usuario no ha podido identificarse!!!'});
        }
    });
}

//Conseguir datos de un usuario
function getUser(req, res){
    var userId = req.params.id;

    User.findById(userId, (err, user) => {
        if(err) return res.status(500).send({message:'Error en la paticion'});

        if (!user) return res.status(404).send({message:'El usuario no existe'});

        return res.status(200).send({user});
    });
}

//Devolver usuarios paginados
function getUsers(req, res){
    var identity_user_id = req.user.sub;
    
    var page = 1;
    if(req.params.page){
        page = req.params.page;
    }

    var itemsPerPage = 5;

    User.find().sort('_id').paginate(page, itemsPerPage, (err, users, total) => {
        if(err) return res.status(500).send({message:'Error en la paticion'});

        if(!users) return res.status(404).send({message:'No hay usurios disponobles'});

        return res.status(200).send({
            users,
            total,
            pages: Math.ceil(total/itemsPerPage)
        });
    });
}

//Edición de datos de usario
function updateUser(req, res){
    var userId = req.params.id;
    var update = req.body;

    //borrar propiedad password
    delete update.password;

    if (userId != req.user.sub){
        return res.status(500).send({message:'No tienes permiso para actualizar datos del usario'});
    }
    User.findByIdAndUpdate(userId, update,{new:true}, (err, userUpdate) => {
        if(err) return res.status(500).send({message:'Error en la paticion'});

        if(!userUpdate) return res.status(404).send({message:'No se ha podido actualizar el usario'});

        return res.status(200).send({userUpdate});
    });
}

// Subir imagen/avatar de usuario
function uploadImage(req, res){
    var userId = req.params.id;
    
    if(req.files){
        var file_path = req.files.image.path;
        var file_split = file_path.split('\/');
        var file_name = file_split[2];   
        var ext_split = file_name.split('\.');
        var file_ext = ext_split[1];

        if (userId != req.user.sub){
            return removeFilesOfUploads(res, file_path, 'No tienes permiso para actualizar datos del usario');
            //return res.status(500).send({message:'No tienes permiso para actualizar datos del usario'});
        }    

        if(file_ext == 'png' || file_ext == 'jpg' || file_ext == 'jpeg' || file_ext =='gif'){
            //actualizar documento de usuario logeado
            User.findByIdAndUpdate(userId, {image: file_name},{new:true}, (err, userUpdate) =>{
                if(err) return res.status(500).send({message:'Error en la paticion'});

                if(!userUpdate) return res.status(404).send({message:'No se ha podido actualizar el usario'});
        
                return res.status(200).send({userUpdate});
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
    var path_file = './uploads/users/'+image_file;

    fs.exists(path_file, (exists) =>{
        if(exists){
            res.sendFile(path.resolve(path_file))
        }else{
            res.status(200).send({message:'No existe la imagen..'});
        }
        
    });
}
module.exports = {
    home, 
    pruebas,
    saveUser,
    loginUser,
    getUser,
    getUsers,
    updateUser,
    uploadImage,
    getImagenFile
}