


import tornado.ioloop
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.web import RequestHandler


# used information from this video: https://www.youtube.com/watch?v=SkETonolR3U

class IndexHandler(RequestHandler):

	# Redirect to sensor table page
	def get(self):
		self.redirect('/sensor-table')



class SensorTableHandler(RequestHandler):

	# Render table page
	def get(self):
		print("SensorHandler:")
		self.render("Sensor_Table.html")


class SensorTableWebSocketHandler(WebSocketHandler):
    def open(self):
    	print("WebSocket open")
    	self.write_message("Hello, world")

    def on_message(self, message):
    	self.write_message(u"You said: " + message)

    def on_close(self):
    	print("WebSocket closed")



urls = [
	(r"/$", IndexHandler),
	(r"/sensor-table", SensorTableHandler),
	(r"/sensor-table/ws$", SensorTableWebSocketHandler)
	]


def make_app(endpoints):
    return tornado.web.Application(
    	endpoints
    	)

if __name__ == "__main__":
    app = make_app(urls)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()