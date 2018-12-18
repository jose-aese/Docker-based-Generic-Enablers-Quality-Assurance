'use strict'

var express = require('express');
var api = express.Router();
var test = require('../controllers/ge_test');


api.get('/unit_test/:data', test.unitTest);


module.exports = api;