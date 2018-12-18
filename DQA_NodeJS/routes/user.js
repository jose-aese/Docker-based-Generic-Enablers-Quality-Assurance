'use stric'

var express = require('express');
var UserController  = require('../controllers/user'); 

var api = express.Router();
var md_auth = require('../middlewares/authenticated');

var multipart = require('connect-multiparty');
var md_upload = multipart({uploadDir: './uploads/users'});

//api.get('/homeUser', UserController.home);
//api.get('/pruebasUser', md_auth.ensureAuth, UserController.pruebas);
api.post('/registerUser', UserController.saveUser);
api.post('/login', UserController.loginUser);
api.get('/user/:id', md_auth.ensureAuth, UserController.getUser);
api.get('/users/:page?', md_auth.ensureAuth, UserController.getUsers);
api.put('/updateUser/:id', md_auth.ensureAuth, UserController.updateUser);
api.post('/upload-image-user/:id', [md_auth.ensureAuth, md_upload], UserController.uploadImage);
api.get('/image-user/:imageFile',UserController.getImagenFile);

module.exports = api;