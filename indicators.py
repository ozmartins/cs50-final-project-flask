import sqlite3
import locale

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

    locale.setlocale(locale.LC_ALL, 'pt')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'    

    ibovespa = {
            "current": '{:n}'.format(rows[0][0]),
            "min52weeks": '{:n}'.format(rows[0][1]),
            "max52weeks": '{:n}'.format(rows[0][2])
        }

    ifix = {
            "current": '{:n}'.format(rows[0][3]),
            "min52weeks": '{:n}'.format(rows[0][4]),
            "max52weeks": '{:n}'.format(rows[0][5])
        }

    selic = {
            "yearrate": '{:.2f}%'.format(rows[0][6]).replace('.', ','),
            "monthrate": '{:.2f}%'.format(rows[0][7]).replace('.', ','),
            "monthname": rows[0][8]
        }

    cdi = {
            "yearrate": '{:.2f}%'.format(rows[0][9]).replace('.', ','),
            "monthrate": '{:.2f}%'.format(rows[0][10]).replace('.', ','),
            "monthname": rows[0][11]
        }

    ipca = {
            "yearrate": '{:.2f}%'.format(rows[0][12]).replace('.', ','),
            "monthrate": '{:.2f}%'.format(rows[0][13]).replace('.', ','),
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
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("select urltoimage, title, description, url from news")
    rows = c.fetchall()
    news = []

    for r in rows:
        news.append(
            {
                "urltoimage": r[0],
                "title": r[1],
                "description": r[2],
                "url": r[3]
            }        
        )

    return news