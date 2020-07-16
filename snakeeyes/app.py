import os

from flask import Flask

from snakeeyes.blueprints.page import page


def create_app():
    """
    Create the flask app using application factor pattern
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    return app


def main():
    app = create_app()
    app.run(port=9000)


if __name__ == '__main__':
    main()
