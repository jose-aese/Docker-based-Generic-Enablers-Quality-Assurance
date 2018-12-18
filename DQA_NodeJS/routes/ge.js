'use strict'

var express = require('express');
var GeController = require('../controllers/ge');

var api = express.Router();

//api.get('/home', GeController.home);
//api.get('/pruebas', GeController.pruebas);
api.post('/register', GeController.saveGe);
api.get('/GES/:page?', GeController.getGes);
api.get('/GE/:ge_name/:page?',GeController.getGe);
api.get('/getGEbyId/:id',GeController.getGeId);

module.exports = api; 