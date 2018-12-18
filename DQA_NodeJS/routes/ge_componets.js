'use strict'

var express = require('express');
var GeComponetControler = require('../controllers/ge_component');

var api = express.Router();

var multipart = require('connect-multiparty');
var md_upload = multipart({uploadDir: './uploads/ge_components'});

api.get('/ge-components', GeComponetControler.getComponets); //extraer todos los registros de la db
api.post('/registerGEcomponent', GeComponetControler.saveGeComponent);
api.post('/upload-image-gecomp/:ge', md_upload, GeComponetControler.uploadImage);//subir imagen
api.get('/image-gecomp/:imageFile',GeComponetControler.getImagenFile);//extraer imagen


module.exports = api; 