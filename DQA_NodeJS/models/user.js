'use stric'

var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var UserSchema = Schema({
    user_name: String,
    nick: String,
    password: String,
    role: String,
    image: String,
    email: String
});

module.exports = mongoose.model('User',UserSchema);