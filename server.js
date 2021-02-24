// https://www.pubnub.com/blog/nodejs-websocket-programming-examples/

const { getAllTableData } = require('./Database.js');


// Node.js socket server script
const net = require('net');
// Create a server object
const server = net.createServer((socket) => {
  socket.on('data', (data) => {
    console.log(data.toString());
  });
  getAllTableData().then(function(result) {
    socket.write(JSON.stringify(result.recordset));
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