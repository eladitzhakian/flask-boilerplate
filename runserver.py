import myapp.settings as settings
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from myapp import setup_logging, create_app

setup_logging()
app = create_app()

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(settings.PORT, address='0.0.0.0')
IOLoop.instance().start()
