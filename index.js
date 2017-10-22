var express = require('express');
var app = express();
var request = require('request')



app.get('/', function (req, res) {

  	var lat = 47.6616099;
	var long = -122.3020524;

	let options = getParkingInfo2(lat, long);

	function getParkingInfo(lat, long) {
		return {
			"url": "https://apis.solarialabs.com/shine/v1/parking-rules/meters",
			"method": "GET",
			"qs": {
				"lat": lat,
			    "long": long,
			    "apikey": "dpAeTEA7PbFCC8zt5fW5CmqStFmRAid6"
			}
		}
	}


	function getParkingInfo2(lat, long) {
		return {
			"url": "http://127.0.0.1:5000/fifteen/155000",
			"method": "GET",
		}
	}

	request(options,(err,resp,body)=>{
		res.send(body);															
  		console.log(body);
	});

});
app.listen(8080, function () {
  console.log('Example app listening on port 3000!');
});