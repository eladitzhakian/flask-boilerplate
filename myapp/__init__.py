import settings
import logging
from views import hello_world
from logging.handlers import WatchedFileHandler
from flask import Flask


def setup_logging():
    logging.basicConfig(format=settings.LOG_FORMAT, level=settings.LOG_LEVEL)
    handler = WatchedFileHandler(filename=settings.LOG_FILENAME)
    handler.setFormatter(logging.Formatter(fmt=settings.LOG_FORMAT))
    logging.getLogger().addHandler(handler)


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', view_func=hello_world.view, methods=['GET', 'POST'])

    return app
