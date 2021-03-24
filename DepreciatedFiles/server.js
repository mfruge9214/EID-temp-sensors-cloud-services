// https://www.pubnub.com/blog/nodejs-websocket-programming-examples/

const { getAllTableData } = require('./Database.js');


// Node.js socket server script
const net = require('net');

function get_last_10(all_data) {
	var last_10 = {}
  all_data.forEach(function (item, index) {
    if(! (item['SensorNumber'] in last_10)){
      last_10[item['SensorNumber']] = []
    }
    last_10[item['SensorNumber']].push(item)
  });
  for (var key in last_10) {
    // getting last 10 elements came from
    // https://stackoverflow.com/questions/6473858/in-a-javascript-array-how-do-i-get-the-last-5-elements-excluding-the-first-ele     
    last_10[key] = last_10[key].slice(Math.max(last_10[key].length - 10, 0))
}
  return last_10;
}

// Create a server object
const server = net.createServer((socket) => {
  socket.on('data', (data) => {
    console.log(data.toString());
  });
  getAllTableData().then(function(result) {
    var last_10 = get_last_10(result.recordset)
    socket.write(JSON.stringify(last_10));
    socket.end('SERVER: Closing connection now.<br>');
  })
  
  //socket.end('SERVER: Closing connection now.<br>');
}).on('error', (err) => {
  console.error(err);
});
// Open server on port 9898
server.listen(9898, () => {
  console.log('opened server on', server.address().port);
});