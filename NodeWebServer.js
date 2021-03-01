// based on examples from https://www.npmjs.com/package/websocket

var WebSocketServer = require('websocket').server;
var http = require('http');

const { formatOutput, get_last_measurement, get_last_10 } = require('./Server_JS_API.js');
const { getAllTableData } = require('./Database.js');

var server = http.createServer(function(request, response) {
  console.log((new Date()) + ' Received request for ' + request.url);
  response.writeHead(404);
  response.end();
});
server.listen(9898, function() {
  console.log((new Date()) + ' Server is listening on port 9898');
});

wsServer = new WebSocketServer({
  httpServer: server,
  // You should not use autoAcceptConnections for production
  // applications, as it defeats all standard cross-origin protection
  // facilities built into the protocol and the browser.  You should
  // *always* verify the connection's origin and decide whether or not
  // to accept it.
  autoAcceptConnections: false
});

function originIsAllowed(origin) {
  // put logic here to detect whether the specified origin is allowed.
  return true;
}

wsServer.on('request', function (request) {
  if (!originIsAllowed(request.origin)) {
    // Make sure we only accept requests from an allowed origin
    request.reject();
    console.log((new Date()) + ' Connection from origin ' + request.origin + ' rejected.');
    return;
  }

  var connection = request.accept(null, request.origin);
  console.log((new Date()) + ' Connection accepted.');
  connection.on('message', function (message) {
    console.log('Received Message: ' + message.utf8Data);

    var received = JSON.parse(message.utf8Data)
    var command = received['command']

    var response = {}
    response['command'] = received['command']
    response['trigger_id'] = received['trigger_id']
    response['output_id'] = received['output_id']


    getAllTableData().then(function (result) {
      if (command == 'I') {
        var sensor_number = parseInt(received['trigger_id'].charAt(7))
        var sensor_data = get_last_measurement(result.recordset, sensor_number)
        response['output'] = formatOutput(sensor_data)
      }
      else if (command == 'C') {
        var last_10 = get_last_10(result.recordset)
        var formatted_last_10 = {}

        for (var key in last_10) {
          formatted_last_10[key] = []
          last_10[key].forEach(function (item, index) {
            formatted_last_10[key].push(formatOutput(item));
          });
        };

        response['output'] = formatted_last_10
      }
      connection.sendUTF(JSON.stringify(response));
    });
  });
  connection.on('close', function (reasonCode, description) {
    console.log((new Date()) + ' Peer ' + connection.remoteAddress + ' disconnected.');
  });
});
