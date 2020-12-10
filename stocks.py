import sqlite3
from flask import session
from flask_session import Session

def get_orderby_criterias():    
    orderby_criterias = [
                {
                    "id": "name",
                    "description": "Nome",
                    "selected": "false"
                },
                {
                    "id": "totalRevenue",
                    "description": "Receita",
                    "selected": "false"
                },
                {
                    "id": "ebit",
                    "description": "EBIT",
                    "selected": "false"
                },
                {
                    "id": "netIncome",
                    "description": "Lucro",
                    "selected": "false"
                }
            ]

    for criteria in orderby_criterias:    
        if criteria["id"] == session["order"]:            
            criteria["selected"] = "true"

    return orderby_criterias

def exists_in_session_filters(filter_field, filter_value):
    if session.get("filters") != None:        
        for filter in session["filters"]:
            if filter["field-name"] == filter_field:
                for option in filter["options"]:
                    if option == filter_value:
                        return True                
    return False


def get_filter_options(filter_field):
    options = []

    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()

    whereClause = get_stock_list_where_clause()

    c.execute("""select distinct {}
                 from stock
                 left outer join stock_profile on (stock_profile.idstock = stock.id) {}""".format(filter_field, whereClause))    
        
    rows = c.fetchall()
    for row in rows:
        if exists_in_session_filters(filter_field, row[0]):
            value = "on"
        else:
            value = "off"
        options.append({
            "name": row[0],
            "value": value
        })    

    return options

def get_filters():
    filters = []        
    
    filters.append({
        "field": "sector",
        "description": "Setor",
        "options": get_filter_options("sector")
    })

    filters.append({
        "field": "industry",
        "description": "Segmento",
        "options": get_filter_options("industry")
    })

    return filters


def get_stock_list_where_clause():
    whereClause = "where 1=1 "

    if session["filters"] != None:
        for filter in session["filters"]:
            options = ""
            for option in filter["options"]:
                if len(options) > 0:
                    options += ","
                options += "'{}'".format(option)
            
            if len(options) > 0:
                whereClause += "and {} in ({})".format(filter["field-name"], options)

    return whereClause

def get_stock_list():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    
    whereClause = get_stock_list_where_clause()    

    orderByClause = ""
    if session["order"] != None:
        if session["order"] == "name":
            orderByClause = "order by {}".format(session["order"])
        else:
            orderByClause = "order by {} desc".format(session["order"])


    c.execute("""select * from (
                    select ticker, name, sector, industry, longBusinessSummary,
                           (select sum(totalRevenue) from income_statement where income_statement.idstock = stock.id) as totalRevenue,
                           (select sum(netIncome) from income_statement where income_statement.idstock = stock.id) as netIncome,
                           (select sum(ebit) from income_statement where income_statement.idstock = stock.id) as ebit
                    from stock
                    left outer join stock_profile on (stock_profile.idstock = stock.id)
                    {}
                ) {}""".format(whereClause, orderByClause))

    rows = c.fetchall()
    stock_list = []
    for row in rows:
        stock_list.append({
            "ticker": row[0][0:4],
            "name": row[1],
            "sector": row[2],
            "subsector": "",
            "segment": row[3],
            "description": row[4]
        }) 

    return stock_list

def search_stocks_by_name(field_name, operator, value):
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
        
    whereClause = " where {} {} '{}' ".format(field_name, operator, value)

    orderByClause = "order by {}".format("name")

    c.execute("select name from stock {} {}".format(whereClause, orderByClause))

    rows = c.fetchall()
    stock_list = []
    for row in rows:
        stock_list.append(row[0]) 

    return stock_list    

def manage_session_filters(form):
    options = []
    for item in form:
        if item != "field-name":
            options.append(item)
        
    new_filter = {
        "field-name": form["field-name"],
        "options": options 
    }

    if session.get("filters") != None:
        existing_filters = [filter for filter in session.get("filters") if filter["field-name"] == new_filter["field-name"]]
        if len(existing_filters) > 0:                
            for filter in session["filters"]:
                if filter["field-name"] == new_filter["field-name"]:
                    old_filter = filter
            index = session["filters"].index(old_filter)
            session["filters"][index] = new_filter            
        else:
            session["filters"].append(new_filter)                                    
    else:
        session["filters"] = [new_filter]