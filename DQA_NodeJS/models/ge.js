'use strict'

var mongoose = require('mongoose');
var Schema = mongoose.Schema; 

var GeSchema = Schema({
        ge_name: String,
        version: String,
        host_name: String,
        test: String,
        execution_time: String,
        date: String,
        time: String
});

module.exports = mongoose.model('Ge',GeSchema);