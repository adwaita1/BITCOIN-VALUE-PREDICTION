var cool = require('cool-ascii-faces');
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/cool', function(request, response) {
    response.send(cool());
});

router.get('/getGraph', function(req,res){
    res.render('graph', { title: 'Express' });
});
module.exports = router;
