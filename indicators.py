def get_market_indicators():
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