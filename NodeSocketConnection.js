var node_host = 'localhost';
var node_port = 9898;
var node_uri = '';



message_struct = {
                  'command':     "None",
                  'trigger_id':  "None",
                  'output_id':   "None"
}

// log function
log = function(data){
  $("div#terminal").prepend("</br>" +data);
  console.log(data);
};


handleICommand = function(data){

  var num_str = data['trigger_id'][-3];

  var trigger_id = data['trigger_id'];

  var output_id = data['output_id'];

  $("#" + output_id).html(data['output']);

};

handleSCommand = function(data){

  var num_str = data['trigger_id'][-3];

  var trigger_id = data['trigger_id'];

  var output_id = data['output_id'];

  $("#" + output_id).html(data['output']);
  
};

handleCCommand = function(data){

  log(data)
  
};


$(document).ready(function () {

    var node_ws;

    // create websocket instance
    node_ws = new WebSocket("ws://" + node_host + ":" + node_port + node_uri);
     

    // Handle incoming websocket message callback


    node_ws.onmessage = function(evt) {
      log("Message Received: " + evt.data);
      
      var dataBack = JSON.parse(evt.data);

      command = dataBack['command']

      if(command == "I"){
        handleICommand(dataBack)
      }

      if(command == "S"){
        handleSCommand(dataBack)
      }

      if(command == "C"){
        handleCCommand(dataBack)
      }


      };

    // Close Websocket callback
    node_ws.onclose = function(evt) {
      log("***Connection Closed***");
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
      log("***Connection Opened***");
    };


    // Individual data request events
    $(".n_req").click(function(evt) {

      var current_row = $(this).closest('tr')

      var output_box = $(current_row).find('p')

      var message = message_struct;

      message['command']  = "I"
      message['output_id'] = output_box.attr("id")
      message['trigger_id'] = this.id

      //  send serialized dictionary of output box and button that caused event 
      node_ws.send(JSON.stringify(message));
    });


    $("#S_convertTemp").click(function(evt){

      var group = $(this).parent();

      var output_box = $(group).find("p");

      var message = message_struct;

      message['command']  = "S"
      message['output_id'] = output_box.attr("id")
      message['trigger_id'] = this.id


      node_ws.send(JSON.stringify(message));


    });


    $("#C_allData").click(function(evt){

      var message = message_struct;

      message['command']  = "C"
      message['trigger_id'] = this.id

      
      node_ws.send(JSON.stringify(message));
    });
});

