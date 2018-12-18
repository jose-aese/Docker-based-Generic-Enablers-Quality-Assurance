'use strict'

var mongoose = require('moongoose');
var Schema = mongoose.Schema;

var ContainerSchema = Schema({
        container_name1: String,
        container_ID1: String,
        status1: String,
        container_name2: String,
        container_ID2: String,
        status2: String,
        container_name3: String,
        container_ID3: String,
        status3: String,
        container_name4: String,
        container_ID4: String,
        status4: String,
        container_name5: String,
        container_ID5: String,
        status5: String,
        ge: {type: Schema.ObjectId, ref:'ge'}
});

module.exports = mongoose.model('Container',ContainerSchema);