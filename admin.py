import sqlite3
import requests
from helpers import apology, last_month, month_name, last_day_of_month, first_day_of_month, one_year_ago
from datetime import date, datetime, timedelta

def create_indicators_record():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("select count(*) from indicators")
    rows = c.fetchall()    
    if rows[0][0] == 0:
        c.execute("insert into indicators (Id) values (1)")    
        conn.commit()


def get_yahoo_headers():
    return {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "b86840a0f4mshd0750b5555ff72cp1653d3jsn06f167d0fd64"
        }


def get_google_params():
    return {        
        'apiKey': 'cdeadf494b5e4fd48b31a9900ad9a6b5',
        'sortBy': 'popularity',
        'q': 'ibovespa AND hoje',
        'from': date.today().strftime("%Y-%m-%d")
        }        


def update_ibovespa():    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"symbols":"^BVSP","region":"BR"}    

    response = requests.request("GET", url, headers=get_yahoo_headers(), params=querystring)

    resp = response.json()

    IbovespaCurrent = resp["quoteResponse"]["result"][0]["regularMarketPrice"]
    IbovespaMin52Weeks = resp["quoteResponse"]["result"][0]["fiftyTwoWeekLow"]
    IbovespaMax52Weeks = resp["quoteResponse"]["result"][0]["fiftyTwoWeekHigh"]        

    create_indicators_record()

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("update indicators set IbovespaCurrent=round(?), IbovespaMin52Weeks=round(?), IbovespaMax52Weeks=round(?) where id = 1", 
              (IbovespaCurrent, IbovespaMin52Weeks, IbovespaMax52Weeks))
    
    conn.commit()

def update_ifix():    
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/v2/get-quotes"

    querystring = {"symbols":"IFIX.SA","region":"BR"}

    response = requests.request("GET", url, headers=get_yahoo_headers(), params=querystring)

    resp = response.json()

    IfixCurrent = resp["quoteResponse"]["result"][0]["regularMarketPrice"]
    IfixMin52Weeks = resp["quoteResponse"]["result"][0]["fiftyTwoWeekLow"]
    IfixMax52Weeks = resp["quoteResponse"]["result"][0]["fiftyTwoWeekHigh"]        

    create_indicators_record()

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("update indicators set IfixCurrent=round(?), IfixMin52Weeks=round(?), IfixMax52Weeks=round(?) where id = 1", 
              (IfixCurrent, IfixMin52Weeks, IfixMax52Weeks))
    
    conn.commit()

def update_news():
    #cdeadf494b5e4fd48b31a9900ad9a6b5
    url = "http://newsapi.org/v2/everything"

    response = requests.request("GET", url, params=get_google_params())

    resp = response.json()    

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("delete from news")

    id = 0    

    for article in resp["articles"]:        
        id += 1
        c.execute("insert into news (id, title, description, url, urltoimage, publishedat) values (?, ?, ?, ?, ?, ?)", 
           (id, article["title"], article["description"], article["url"], article["urlToImage"], article["publishedAt"])
        )
    
    conn.commit()

def update_selic():
    #https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=21/10/2019&dataFinal=21/10/2020

    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados"

    initial_date = one_year_ago(first_day_of_month(datetime.today().date()))
    final_date = last_day_of_month(last_month())

    querystring = {
            "formato":"json",
            "dataInicial": initial_date.strftime("%d/%m/%Y"),
            "dataFinal": final_date.strftime("%d/%m/%Y")
        }

    response = requests.request("GET", url, params=querystring)

    resp = response.json()

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("delete from selic")

    for selic in resp:
        date = datetime.strptime(selic["data"], '%d/%m/%Y').date()        
        c.execute("insert into selic (date, value) values (?, ?)", (date, selic["valor"]))
    
    c.execute("""update indicators set 
        Selic12Months = (select sum(value) from selic where date >= ? and date <= ?),
        SelicLastMonth = (select sum(value) from selic where strftime('%Y%m', date) = ?),
        SelicMonthName = ?""",
        (initial_date, final_date, last_month().strftime('%Y%m'), month_name(last_month().month)))
    
    conn.commit()

def update_ipca():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.16121/dados"

    initial_date = one_year_ago(first_day_of_month(datetime.today().date()))
    final_date = last_day_of_month(last_month())

    querystring = {
            "formato":"json",
            "dataInicial": initial_date.strftime("%d/%m/%Y"),
            "dataFinal": final_date.strftime("%d/%m/%Y")
        }

    response = requests.request("GET", url, params=querystring)

    resp = response.json()

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("delete from ipca")

    for ipca in resp:
        date = datetime.strptime(ipca["data"], '%d/%m/%Y').date()        
        c.execute("insert into ipca (date, value) values (?, ?)", (date, ipca["valor"]))
    
    c.execute("""update indicators set 
        Ipca12Months = (select sum(value) from ipca where date >= ? and date <= ?),
        IpcaLastMonth = (select sum(value) from ipca where strftime('%Y%m', date) = ?),
        IpcaMonthName = ?""",
        (initial_date, final_date, last_month().strftime('%Y%m'), month_name(last_month().month)))
    
    conn.commit()


def update_cdi():
    cdi_file = open("import\\cdi.xls", "r")

    lines = [line.replace('\n', '').split('\t') for line in cdi_file.readlines()]
    lines.pop(0)

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute("delete from cdi")

    for line in lines:
        date = datetime.strptime(line[0], '%d/%m/%Y').date()
        c.execute("insert into cdi (date, value) values (?, ?)", (date, (float(line[4].replace('.', '').replace(',', '.'))-1) * 100) )

    initial_date = one_year_ago(first_day_of_month(datetime.today().date()))
    final_date = last_day_of_month(last_month())
    
    c.execute("""update indicators set 
        Cdi12Months = (select sum(value) from cdi where date >= ? and date <= ?),
        CdiLastMonth = (select sum(value) from cdi where strftime('%Y%m', date) = ?),
        CdiMonthName = ?""",
        (initial_date, final_date, last_month().strftime('%Y%m'), month_name(last_month().month)))
    
    conn.commit()


def update_income_statement(history):
    for year in history:
        if len(year['researchDevelopment']) > 0:
            researchDevelopment = year['researchDevelopment']['longFmt']

        if len(year['effectOfAccountingCharges']) > 0:
            effectOfAccountingCharges = year['effectOfAccountingCharges']['longFmt']

        if len(year['incomeBeforeTax']) > 0:
            incomeBeforeTax = year['incomeBeforeTax']['longFmt']
        
        if len(year['minorityInterest']) > 0:
            minorityInterest = year['minorityInterest']['longFmt']
        
        if len(year['netIncome']) > 0:
            netIncome = year['netIncome']['longFmt']
        
        if len(year['sellingGeneralAdministrative']) > 0:
            sellingGeneralAdministrative = year['sellingGeneralAdministrative']['longFmt']
        
        if len(year['grossProfit']) > 0:
            grossProfit = year['grossProfit']['longFmt']
        
        if len(year['ebit']) > 0:
            ebit = year['ebit']['longFmt']
        
        if len(year['endDate']) > 0:
            endDate = year['endDate']['fmt']
        
        if len(year['operatingIncome']) > 0:
            operatingIncome = year['operatingIncome']['longFmt']
        
        if len(year['otherOperatingExpenses']) > 0:
            otherOperatingExpenses = year['otherOperatingExpenses']['longFmt']
        
        if len(year['interestExpense']) > 0:
            interestExpense = year['interestExpense']['longFmt']
        
        if len(year['extraordinaryItems']) > 0:
            extraordinaryItems = year['extraordinaryItems']['longFmt']
        
        if len(year['nonRecurring']) > 0:
            nonRecurring = year['nonRecurring']['longFmt']
        
        if len(year['otherItems']) > 0:
            otherItems = year['otherItems']['longFmt']
        
        if len(year['incomeTaxExpense']) > 0:
            incomeTaxExpense = year['incomeTaxExpense']['longFmt']
        
        if len(year['totalRevenue']) > 0:
            totalRevenue = year['totalRevenue']['longFmt']
        
        if len(year['totalOperatingExpenses']) > 0:
            totalOperatingExpenses = year['totalOperatingExpenses']['longFmt']
        
        if len(year['costOfRevenue']) > 0:
            costOfRevenue = year['costOfRevenue']['longFmt']
        
        if len(year['totalOtherIncomeExpenseNet']) > 0:
            totalOtherIncomeExpenseNet = year['totalOtherIncomeExpenseNet']['longFmt']
        
        if len(year['discontinuedOperations']) > 0:
            discontinuedOperations = year['discontinuedOperations']['longFmt']
        
        if len(year['netIncomeFromContinuingOps']) > 0:
            netIncomeFromContinuingOps = year['netIncomeFromContinuingOps']['longFmt']
        
        if len(year['netIncomeApplicableToCommonShares']) > 0:
            netIncomeApplicableToCommonShares = year['netIncomeApplicableToCommonShares']['longFmt']


def update_stock_data(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

    querystring = {"symbol":stock,"region":"BR"}    

    response = requests.request("GET", url, headers=get_yahoo_headers(), params=querystring)

    resp = response.json() 

    update_income_statement(resp['incomeStatementHistory']['incomeStatementHistory'])


update_stock_data("PETR3.SA")