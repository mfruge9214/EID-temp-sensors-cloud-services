var node_host = 'localhost';
var node_port = 9898;
var node_uri = '';
var node_celsius = false;



message_struct = {
                  'command':     "None",
                  'trigger_id':  "None",
                  'output_id':   "None",
                  'celsius_flag':     "None",
                  'timestamp': "None" 
}

// log function
node_log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};



$(document).ready(function () {

    var node_ws;

    // create websocket instance
    node_ws = new WebSocket("ws://" + node_host + ":" + node_port + node_uri);
     

    // Handle incoming websocket message callback


    node_ws.onmessage = function(evt) {
      node_log("Message Received: " + evt.data);
      
      var dataBack = JSON.parse(evt.data);
      var resp_timestamp = Date.now()

      command = dataBack['command']

      if(command == "I"){
        handleICommand(dataBack)
      }

      if(command == "S"){
        handleSCommand(dataBack)
      }

      if(command == "C"){
        handleCCommand(dataBack, resp_timestamp)
      }


      };

    // Close Websocket callback
    node_ws.onclose = function(evt) {
      node_log("***Connection Closed***");
      alert("Connection close");
      // $("#host").css("background", "#ff0000"); 
      // $("#port").css("background", "#ff0000"); 
      // $("#uri").css("background",  "#ff0000");
      // $("div#message_details").empty();

      };

    // Open Websocket callback
    node_ws.onopen = function(evt) { 
      // $("#host").css("background", "#00ff00"); 
      // $("#port").css("background", "#00ff00"); 
      // $("#uri").css("background", "#00ff00");
      // $("div#message_details").show();
      node_log("***Connection Opened***");
    };


    // Individual data request events
    $(".n_req").click(function(evt) {

      var current_row = $(this).closest('tr')

      var output_box = $(current_row).find('p')

      var message = message_struct;

      message['command']  = "I"
      message['output_id'] = output_box.attr("id")
      message['trigger_id'] = this.id
      message['celsius_flag'] = node_celsius


      $("#" + output_box.attr("id")).css("background-color", "aqua");

      //  send serialized dictionary of output box and button that caused event 
      node_ws.send(JSON.stringify(message));
    });


    $("#S_convertTemp").click(function(evt){

      node_celsius = ! node_celsius

      //node_ws.send(JSON.stringify(message));


    });


    $("#C_allData_Node").click(function(evt){

      var message = message_struct;

      // var timestamp = evt.timeStamp;

      var timestamp = Date.now()
      message['command']  = "C"
      message['trigger_id'] = this.id
      message['celsius_flag'] = node_celsius

      message['timestamp'] = timestamp
      
      node_ws.send(JSON.stringify(message));
    });
});

