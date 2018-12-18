'use strict'

var mongoose = require('mongoose');
var Schema = mongoose.Schema; 

var ComponentSchema = Schema({
        ge: String,
        url: String,
        image: String
});

module.exports = mongoose.model('ge_component',ComponentSchema);