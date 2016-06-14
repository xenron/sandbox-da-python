var connect = require('connect');
var app = connect();
var fs = require('fs');
const PORT = 8181;


app.use('/getData', function(req, res, next){
	var resData = {
		code: 0
	}

	res.writeHead(200, {
		'Content-Type': 'text/json',
		'Access-Control-Allow-Origin': '*'
	});

	try{
		resData.data = fs.readFileSync('./data.json','utf-8');
	}catch(err){
		resData.code = -1;
		resData.msg = '读取数据文件出错,' + err;
		res.write(JSON.stringify(resData));
		res.end();
		return;
	}

	setTimeout(function(){
		res.write(JSON.stringify(resData));
		res.end();
	},2000);
});

app.use('/getScoreData', function(req, res, next){
	var resData = {
		code: 0
	}

	res.writeHead(200, {
		'Content-Type': 'text/json',
		'Access-Control-Allow-Origin': '*'
	});

	try{
		resData.data = fs.readFileSync('./score.json','utf-8');
	}catch(err){
		resData.code = -1;
		resData.msg = '读取数据文件出错,' + err;
		res.write(JSON.stringify(resData));
		res.end();
		return;
	}

	setTimeout(function(){
		res.write(JSON.stringify(resData));
		res.end();
	},2000);
});

app.listen(PORT, function(){
	console.log('listening on Port: ' + PORT);
});
