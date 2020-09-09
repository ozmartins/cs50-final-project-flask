import os
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import requests
from helpers import apology

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
    ibovespa = {
            "current": "102.000",
            "min52weeks": "65.000",
            "max52weeks": "120.000"
        }

    ifix = {
            "current": "2.000",
            "min52weeks": "1.000",
            "max52weeks": "3.000"
        }

    selic = {
            "yearrate": "3%",
            "monthrate": "0.2%",
            "monthname": "Agosto/2020"
        }

    cdi = {
            "yearrate": "2.9%",
            "monthrate": "0.19%",
            "monthname": "Agosto/2020"
        }

    ipca = {
            "yearrate": "2%",
            "monthrate": "0.1%",
            "monthname": "Agosto/2020"
        }

    indicators = {
        "ibovespa": ibovespa,
        "ifix": ifix,
        "selic": selic,
        "cdi": cdi,
        "ipca": ipca
    }

    news = [
        {
            "image": "./static/nova-previdencia-privada.jpg",
            "headline": "Manchete da primeira notícia",
            "text": "Texto da primeira notícia"
        },
        {
            "image": "./static/money-times.png",
            "headline": "Manchete da segunda notícia",
            "text": "Texto da segunda notícia"
        },        
    ]

    return render_template("index.html", indicators=indicators, news=news)


def errorhandler(e):    
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    app.run()