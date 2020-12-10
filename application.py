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
from stocks import get_orderby_criterias, get_filters, get_stock_list, manage_session_filters
from admin import update_ibovespa, update_ifix, update_news, update_cdi, update_selic, update_ipca


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


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", indicators=get_market_indicators(), news=get_market_news())


@app.route("/order-stocks-list", methods=["POST"])
def order_stocks_list():          
    session["order"] = request.form["order"]
    return render_template("stocks-list.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())


@app.route("/order-stocks-grid", methods=["POST"])
def order_stocks_grid():      
    session["order"] = request.form["order"]
    return render_template("stocks-grid.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())


@app.route("/stocks-grid", methods=["GET", "POST"])
def stocks_grid():
    if request.method=="GET":
        session["filters"] = []
        session["order"] = "name"
    elif request.method=="POST":        
        manage_session_filters(request.form)

    return render_template("stocks-grid.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())


@app.route("/stocks-list", methods=["GET", "POST"])
def stocks_list():      
    if request.method=="GET":
        session["filters"] = []
        session["order"] = "name"
    elif request.method=="POST":        
        manage_session_filters(request.form)
    return render_template("stocks-list.html", orderby_criterias=get_orderby_criterias(), filters=get_filters(), stock_list=get_stock_list())


@app.route("/stock/<symbol>", methods=["GET"])
def stock(symbol=""):
    return render_template("stock.html", symbol=symbol)

@app.route("/search_stocks/<query>", methods=["GET"])
def search_stocks(query=""):
    print(query)
    return ["Bradesco", "Itaú", "Banrisul"]

def errorhandler(e):    
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "GET":
        return render_template("admin.html")    
    elif request.method == "POST":
        if request.form.get("ibovespa")=="on":
            update_ibovespa()        
        if request.form.get("ifix")=="on":
            update_ifix()            
        if request.form.get("selic")=="on":
            update_selic()            
        if request.form.get("cdi")=="on":    
            update_cdi()            
        if request.form.get("ipca")=="on":
            update_ipca()    
        if request.form.get("news")=="on":
            update_news()            
        return redirect("/")   


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    #app.run(host="0.0.0.0", port=port)
    app.run()