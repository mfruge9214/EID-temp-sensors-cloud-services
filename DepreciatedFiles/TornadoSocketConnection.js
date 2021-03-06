




  var host = 'localhost';
  var port = 8888;
  var uri = '/ws';



  message_struct = {
                    'command':     "None",
                    'trigger_id':  "None",
                    'output_id':   "None",
                    'timestamp':   "None"
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

  handleCCommand = function(data, timestamp){

    log(data)

    var start_time = data['timestamp']

    log(start_time)

    log(timestamp)

    var elapsedTime = Math.floor(timestamp) - Math.floor(start_time)
    
    $(".elapsedTime").html(elapsedTime.toString() + " Milliseconds");

    // Dictionary where keys = sensor numbers and values are arrays of up to 10 strings of formatted output
    var outputs = data['output'];

    var sensor_num;

    var table = $(".recentSensorData")

    for (sensor_num in outputs){

      var outputText_list = outputs[sensor_num];

      // Identify the list element we need to append to

      var sensor_list_el = $(".recentSensorData").find("ol#sensor" + sensor_num.toString() + "_list_data");

      sensor_list_el.empty();

      for (entry in outputText_list){

        sensor_list_el.append("<li>" + outputText_list[entry] + "</li>")

      }
    }
  };

  handleGCommand = function(data){
    // workaround to reload image every time from:
    // https://stackoverflow.com/questions/2104949/how-to-reload-refresh-an-elementimage-in-jquery
    $("#G_graph_img").attr('src', 'eid_graph.png?timestamp=' + new Date().getTime())
  };


  $(document).ready(function () {

    var ws;

    // create websocket instance
    ws = new WebSocket("ws://" + host + ":" + port + uri);
     

    // Handle incoming websocket message callback


    ws.onmessage = function(evt) {
      
      var dataBack = JSON.parse(evt.data);

      command = dataBack['command']

      // var resp_timestamp = evt.timeStamp;
      var resp_timestamp = Date.now()

      if(command == "I"){
        handleICommand(dataBack)
      }

      if(command == "S"){
        handleSCommand(dataBack)
      }

      if(command == "C"){
        handleCCommand(dataBack, resp_timestamp)
      }

      if(command == "G"){
        handleGCommand(dataBack)
      }

      };

    // Close Websocket callback
    ws.onclose = function(evt) {
      log("***Connection Closed***");
      alert("Connection close");
      // $("#host").css("background", "#ff0000"); 
      // $("#port").css("background", "#ff0000"); 
      // $("#uri").css("background",  "#ff0000");
      // $("div#message_details").empty();

      };

    // Open Websocket callback
    ws.onopen = function(evt) { 
      // $("#host").css("background", "#00ff00"); 
      // $("#port").css("background", "#00ff00"); 
      // $("#uri").css("background", "#00ff00");
      // $("div#message_details").show();
      log("***Connection Opened***");
    };

    $("#C_allData_Tornado").click(function(evt){

      // var timestamp = evt.timeStamp;
      var timestamp = Date.now()
      var message = message_struct;

      log(evt)

      message['timestamp'] = timestamp;
      message['command']  = "C"
      message['trigger_id'] = this.id

      log(message)
      ws.send(JSON.stringify(message));
    });

    $("#G_graph").click(function(evt){

      var message = message_struct;

      message['command']  = "G"
      message['trigger_id'] = this.id

      ws.send(JSON.stringify(message));
    });

    // Individual data request events
    $(".t_req").click(function(evt) {

      var current_row = $(this).closest('tr')

      var output_box = $(current_row).find('p')

      var message = message_struct;

      message['command']  = "I"
      message['output_id'] = output_box.attr("id")
      message['trigger_id'] = this.id

      $("#" + output_box.attr("id")).css("background-color", "#4CAF50");

      //  send serialized dictionary of output box and button that caused event 
      ws.send(JSON.stringify(message));
    });


    $("#S_convertTemp").click(function(evt){

      var group = $(this).parent();

      var output_box = $(group).find("p");

      var message = message_struct;

      message['command']  = "S"
      message['output_id'] = output_box.attr("id")
      message['trigger_id'] = this.id


      ws.send(JSON.stringify(message));


      $(".t_req").click()

      $("#C_allData_Tornado").click()

      $("#G_graph").click()

    });



});

