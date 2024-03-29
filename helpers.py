import os
import requests
import urllib.parse
from flask import redirect, render_template, request, session
from functools import wraps
import datetime
import calendar

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def apology(message, code=400):    
    def escape(s):        
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def last_month():
    today = datetime.date.today()
    first = today.replace(day=1)
    lastMonth = first - datetime.timedelta(days=1)
    return lastMonth

def last_day_of_month(date):    
    last_day_of_month = calendar.monthrange(date.year,date.month)[1]        
    return date.replace(day=last_day_of_month)

def first_day_of_month(date):        
    return date.replace(day=1)

def one_year_ago(date):
    return date.replace(year=date.year-1)

def month_name(month):
    return months[month-1]