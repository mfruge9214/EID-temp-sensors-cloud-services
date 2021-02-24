


import tornado.ioloop
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.web import RequestHandler
from tornado.httpserver import HTTPServer


# used information from this tutorial: https://os.mbed.com/cookbook/Websockets-Server
# used information from this video: https://www.youtube.com/watch?v=SkETonolR3U

# class WebSocketsHandler(RequestHandler):

# 	# Redirect to sensor table page
# 	def get(self):
# 		self.redirect('/sensor-table')



# class SensorTableHandler(RequestHandler):

# 	# Render table page
# 	def get(self):
# 		print("SensorHandler:")
# 		self.render("Sensor_Table.html")


class SensorTableWebSocketHandler(WebSocketHandler):
    def open(self):
    	print("WebSocket open")
    	self.write_message("Hello, world")

    def on_message(self, message):
    	self.write_message(u"You said: " + message)
    	self.render("html_test.py")

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



