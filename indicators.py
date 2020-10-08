import sqlite3

def get_market_indicators():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("""select IbovespaCurrent, IbovespaMin52Weeks, IbovespaMax52Weeks,
              IfixAtual, IfixMin52Weeks, IfixMax52Week,
              Selic12Months, SelicCurrentMonth, SelicMonthName,
              CDI12Months, CDIMesCurrent, CDIMonthName,
              IPCA12Months, IPCACurrentMonth, IPCAMonthName
              from indicators""")
    rows = c.fetchall()

    ibovespa = {
            "current": '{:d}'.format(rows[0][0]),
            "min52weeks": '{:d}'.format(rows[0][1]),
            "max52weeks": '{:d}'.format(rows[0][2])
        }

    ifix = {
            "current": '{:d}'.format(rows[0][3]),
            "min52weeks": '{:d}'.format(rows[0][4]),
            "max52weeks": '{:d}'.format(rows[0][5])
        }

    selic = {
            "yearrate": '{:.2f}%'.format(rows[0][6]),
            "monthrate": '{:.2f}%'.format(rows[0][7]),
            "monthname": rows[0][8]
        }

    cdi = {
            "yearrate": '{:.2f}%'.format(rows[0][9]),
            "monthrate": '{:.2f}%'.format(rows[0][10]),
            "monthname": rows[0][11]
        }

    ipca = {
            "yearrate": '{:.2f}%'.format(rows[0][12]),
            "monthrate": '{:.2f}%'.format(rows[0][13]),
            "monthname": rows[0][14]
        }

    indicators = {
        "ibovespa": ibovespa,
        "ifix": ifix,
        "selic": selic,
        "cdi": cdi,
        "ipca": ipca
    }

    return indicators

def get_market_news():
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

    return news