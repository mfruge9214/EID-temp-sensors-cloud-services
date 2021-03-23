
  // log function
  log = function(data){
    $("div#terminal").prepend("</br>" +data);
    console.log(data);
  };


log("Running")

$(document).ready(function () {

	$("#DataGet").click(function(evt){

		log("Start Get Data");

		var start_timestamp = Date.now()

		$("#DataOut").empty()


		$.get(
	    "https://d4v65xybyh.execute-api.us-east-2.amazonaws.com/prod/getSensorData",
	    {paramOne : 1, paramX : 'abc'},
	    function(data) {


	       log(data)

	       let i = 0;

	       for(i=0; i<data.length; i++){
	       		$("#DataOut").append("<li>" + JSON.stringify(data[i]) + "</li>")
	       }

	       var end_timestamp = Date.now()

			var elapsedTime = Math.floor(end_timestamp) - Math.floor(start_timestamp)
	    
	    	$(".elapsedTime").html(elapsedTime.toString() + " Milliseconds");

		    log("Data Got")

	       
	    })


		
	    

	})

});