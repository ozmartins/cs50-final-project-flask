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

def get_filters():
    filters = [
        {
            "id": "0",
            "description": "Setor",
            "options": 
                [ 
                    {
                        "id": "0",
                        "description": "Setor 1"
                    },
                    {
                        "id": "1",
                        "description": "Setor 2"
                    },
                    {
                        "id": "2",
                        "description": "Setor 3"
                    },
                    {
                        "id": "3",
                        "description": "Setor 4"
                    }                
                ]
        },
        {
            "id": "1",
            "description": "Sub-Setor",
            "options": 
                [
                    {
                        "id": "0",
                        "description": "Sub-Setor 1"
                    },
                    {
                        "id": "1",
                        "description": "Oleo e Gas"
                    },
                    {
                        "id": "2",
                        "description": "Sub-Setor 3"
                    },
                    {
                        "id": "3",
                        "description": "Sub-Setor 4"
                    }      
                ]          

        }
    ]

    return filters

def get_stock_list():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("select ticker, name from stock")
    rows = c.fetchall()
    stock_list = []
    for row in rows:
        stock_list.append({
            "ticker": row[0][0:4],
            "name": row[1],
            "sector": "Setor",
            "subsector": "Sub-setor",
            "segment": "Segment",
            "description": ""
        }) 

    return stock_list