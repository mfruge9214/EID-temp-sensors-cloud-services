


import tornado.ioloop
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.web import RequestHandler
from tornado.httpserver import HTTPServer
from Monitor import Monitor
import Server_Python_API as API
import json


# used information from this tutorial: https://os.mbed.com/cookbook/Websockets-Server
# used information from this video: https://www.youtube.com/watch?v=SkETonolR3U


class SensorTableWebSocketHandler(WebSocketHandler):
    
	def open(self):
		API.monitor = Monitor()
		print("WebSocket open")


	def on_message(self, message):

		received = json.loads(message)

		print(received)
		response = {}

		response['output'] = API.ParseMessage(received)
		response['command'] = received['command']
		response['trigger_id'] = received['trigger_id']
		response['output_id'] = received['output_id']

		self.write_message(json.dumps(response))

	def on_close(self):
		print("WebSocket closed")

	def check_origin(self, origin):
		return True




urls = [
	(r"/ws", SensorTableWebSocketHandler)
	]


port = 8888

def make_app(endpoints):
    return tornado.web.Application(
    	endpoints
    	)



if __name__ == "__main__":
	print(urls)
	app = make_app(urls)
	server = HTTPServer(app)
	server.listen(port)
	tornado.ioloop.IOLoop.instance().start()



