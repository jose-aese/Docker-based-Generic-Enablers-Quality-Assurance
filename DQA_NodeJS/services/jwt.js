'use strict'

var jwt = require('jwt-simple');
var moment = require('moment');
var secret = 'ITSM.FIWARE_DOCKER';

exports.createToken = function(user){
    var payload = {
        sub: user._id,
        name: user.name,
        nick: user.nick,
        email: user.email,
        role: user.role,
        imagen: user.imagen,
        ait: moment().unix(),
        exp: moment().add(30,'days').unix
    };
    return jwt.encode(payload, secret);
};