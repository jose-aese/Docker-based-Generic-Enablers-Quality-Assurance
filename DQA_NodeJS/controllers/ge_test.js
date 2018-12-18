'use strict'
var exec = require('child_process').exec;

var Ge = require('../models/ge');

function unitTest(req, res){
  var ruta = String;
  var script = String;
  var comando = String;
  var ge_name = req.params.data;
  ruta = "cd uploads/scripts/"+ge_name;
  script = "python "+ge_name+".py";
  comando = ruta+" && "+script;
  //res.send(ge_name+" Test start!!!") 
  exec(comando, function(err,stdout){
    if(err){
      throw err;
    }
    Ge.find({},{_id: 1}).sort({$natural: -1}).limit(1).exec((err, ge) =>{
      if(err) return res.status(500).send({message:'Error en la petición'});
      console.log(ge);
      return res.status(200).send(ge);
      
    });
   
  });
}
module.exports = {

  unitTest,
 
}