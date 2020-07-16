from flask import Blueprint, render_template
from flask import current_app

page = Blueprint('page', __name__, template_folder='templates')


@page.route("/")
def home():
    """
    Render a hello world response
    :return: Flask Response
    """
    # return current_app.config.get('HELLO')
    return render_template('page/home.html')


@page.route("/terms")
def terms():
    """
    Render a hello world response
    :return: Flask Response
    """
    # return current_app.config.get('HELLO')
    return render_template('page/terms.html')


@page.route("/privacy")
def privacy():
    """
    Render a hello world response
    :return: Flask Response
    """
    # return current_app.config.get('HELLO')
    return render_template('page/privacy.html')
