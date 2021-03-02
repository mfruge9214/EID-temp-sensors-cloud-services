import tornado.ioloop
from tornado.websocket import WebSocketHandler, WebSocketClosedError
from tornado.web import RequestHandler




class SensorTableHandler(RequestHandler):

	# Render table page
	def get(self):
		self.render("Sensor_Table.html")


urls = [
	(r"/", SensorTableHandler)
	]


port = 8888

def make_app(endpoints):
    return tornado.web.Application(
    	endpoints
    	)



if __name__ == "__main__":
    app = make_app(urls)
    app.listen(port)
    tornado.ioloop.IOLoop.instance().start()