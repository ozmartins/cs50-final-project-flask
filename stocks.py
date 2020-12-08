import sqlite3

def get_orderby_criterias():
    orderby_criterias = [
                {
                    "id": "0",
                    "description": "Valor de mercado"
                },
                {
                    "id": "1",
                    "description": "Nome"
                },
                {
                    "id": "2",
                    "description": "Patrimônio líquido"
                },
                {
                    "id": "3",
                    "description": "Ano de fundação"
                },
                {
                    "id": "4",
                    "description": "Ano de IPO"
                },
                {
                    "id": "5",
                    "description": "Anos lucrativos"
                }
            ]    

    return orderby_criterias

def get_filter_options(filter_field):    
    options = []

    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    
    c.execute("select distinct {0} from stock_profile".format(filter_field))
    rows = c.fetchall()
    for row in rows:        
        options.append({
            "value": row[0]            
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

def get_stock_list(filters):
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    
    whereClause = "where 1=1 "
    options = ""
    for filter in filters:        
        for option in filter["options"]:
            options += "'{}'".format(option)
        
        if len(options) > 0:
            whereClause += "and {} in ({})".format(filter["field-name"], options)
        
    print("whereClause")
    print(whereClause)

    c.execute("""select ticker, name, sector, industry, longBusinessSummary 
                 from stock
                 left outer join stock_profile on (stock_profile.idstock = stock.id) {}""".format(whereClause))

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
