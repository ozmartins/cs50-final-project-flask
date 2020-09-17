import os
import requests

from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology
from indicators import get_market_indicators, get_market_news
from stocks import get_orderby_criterias, get_filters, get_stock_list


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():              
    return render_template("index.html", indicators=get_market_indicators(), news=get_market_news())


@app.route("/stocks/<view>")
def stocks(view=""):
    if (view=="grid"):
        return render_template("stocks-grid.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())
    else:
        return render_template("stocks-list.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())


def errorhandler(e):    
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()
