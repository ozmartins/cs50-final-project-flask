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


def update_income_statement(idstock, history):
    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()    

    for year in history:
        endDate=datetime.today()
        researchDevelopment=0
        effectOfAccountingCharges=0
        incomeBeforeTax=0
        minorityInterest=0
        netIncome=0
        sellingGeneralAdministrative=0
        grossProfit=0
        ebit=0
        operatingIncome=0
        otherOperatingExpenses=0
        interestExpense=0
        extraordinaryItems=0
        nonRecurring=0
        otherItems=0
        incomeTaxExpense=0
        totalRevenue=0
        totalOperatingExpenses=0
        costOfRevenue=0
        totalOtherIncomeExpenseNet=0
        discontinuedOperations=0
        netIncomeFromContinuingOps=0
        netIncomeApplicableToCommonShares=0

        if 'researchDevelopment' in year and len(year['researchDevelopment']) > 0:
            researchDevelopment = year['researchDevelopment']['raw']

        if 'effectOfAccountingCharges' in year and len(year['effectOfAccountingCharges']) > 0:
            effectOfAccountingCharges = year['effectOfAccountingCharges']['raw']

        if 'incomeBeforeTax' in year and len(year['incomeBeforeTax']) > 0:
            incomeBeforeTax = year['incomeBeforeTax']['raw']
        
        if 'minorityInterest' in year and len(year['minorityInterest']) > 0:
            minorityInterest = year['minorityInterest']['raw']
        
        if 'netIncome' in year and len(year['netIncome']) > 0:
            netIncome = year['netIncome']['raw']
        
        if 'sellingGeneralAdministrative' in year and len(year['sellingGeneralAdministrative']) > 0:
            sellingGeneralAdministrative = year['sellingGeneralAdministrative']['raw']
        
        if 'grossProfit' in year and len(year['grossProfit']) > 0:
            grossProfit = year['grossProfit']['raw']
        
        if 'ebit' in year and len(year['ebit']) > 0:
            ebit = year['ebit']['raw']
        
        if 'endDate' in year and len(year['endDate']) > 0:
            endDate = year['endDate']['fmt']
        
        if 'operatingIncome' in year and len(year['operatingIncome']) > 0:
            operatingIncome = year['operatingIncome']['raw']
        
        if 'otherOperatingExpenses' in year and len(year['otherOperatingExpenses']) > 0:
            otherOperatingExpenses = year['otherOperatingExpenses']['raw']
        
        if 'interestExpense' in year and len(year['interestExpense']) > 0:
            interestExpense = year['interestExpense']['raw']
        
        if 'extraordinaryItems' in year and len(year['extraordinaryItems']) > 0:
            extraordinaryItems = year['extraordinaryItems']['raw']
        
        if 'nonRecurring' in year and len(year['nonRecurring']) > 0:
            nonRecurring = year['nonRecurring']['raw']
        
        if 'otherItems' in year and len(year['otherItems']) > 0:
            otherItems = year['otherItems']['raw']
        
        if 'incomeTaxExpense' in year and len(year['incomeTaxExpense']) > 0:
            incomeTaxExpense = year['incomeTaxExpense']['raw']
        
        if 'totalRevenue' in year and len(year['totalRevenue']) > 0:
            totalRevenue = year['totalRevenue']['raw']
        
        if 'totalOperatingExpenses' in year and len(year['totalOperatingExpenses']) > 0:
            totalOperatingExpenses = year['totalOperatingExpenses']['raw']
        
        if 'costOfRevenue' in year and len(year['costOfRevenue']) > 0:
            costOfRevenue = year['costOfRevenue']['raw']
        
        if 'totalOtherIncomeExpenseNet' in year and len(year['totalOtherIncomeExpenseNet']) > 0:
            totalOtherIncomeExpenseNet = year['totalOtherIncomeExpenseNet']['raw']
        
        if 'discontinuedOperations' in year and len(year['discontinuedOperations']) > 0:
            discontinuedOperations = year['discontinuedOperations']['raw']
        
        if 'netIncomeFromContinuingOps' in year and len(year['netIncomeFromContinuingOps']) > 0:
            netIncomeFromContinuingOps = year['netIncomeFromContinuingOps']['raw']
        
        if 'netIncomeApplicableToCommonShares' in year and len(year['netIncomeApplicableToCommonShares']) > 0:
            netIncomeApplicableToCommonShares = year['netIncomeApplicableToCommonShares']['raw']

        c.execute("""insert into income_statement 
                    (                        
                        idStock,
                        endDate,
                        researchDevelopment,
                        effectOfAccountingCharges,
                        incomeBeforeTax,
                        minorityInterest,
                        netIncome,
                        sellingGeneralAdministrative,
                        grossProfit,
                        ebit  ,
                        operatingIncome,
                        otherOperatingExpenses,
                        interestExpense,
                        extraordinaryItems,
                        nonRecurring,
                        otherItems,
                        incomeTaxExpense,
                        totalRevenue,
                        totalOperatingExpenses,
                        costOfRevenue,
                        totalOtherIncomeExpenseNet,
                        discontinuedOperations,
                        netIncomeFromContinuingOps,
                        netIncomeApplicableToCommonShares
                    )
                    values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",                        
                    (
                        idstock,
                        endDate,
                        researchDevelopment,
                        effectOfAccountingCharges,
                        incomeBeforeTax,
                        minorityInterest,
                        netIncome,
                        sellingGeneralAdministrative,
                        grossProfit,
                        ebit,
                        operatingIncome,
                        otherOperatingExpenses,
                        interestExpense,
                        extraordinaryItems,
                        nonRecurring,
                        otherItems,
                        incomeTaxExpense,
                        totalRevenue,
                        totalOperatingExpenses,
                        costOfRevenue,
                        totalOtherIncomeExpenseNet,
                        discontinuedOperations,
                        netIncomeFromContinuingOps,
                        netIncomeApplicableToCommonShares                   
                    )
        )

    conn.commit()
                    

def update_balance_sheet(idstock, history):
    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    for year in history:
        intangibleAssets=0
        capitalSurplus=0
        totalLiab=0
        totalStockholderEquity=0
        otherCurrentLiab=0
        totalAssets=0
        endDate=date.today()
        commonStock=0
        otherCurrentAssets=0
        retainedEarnings=0
        otherLiab=0
        treasuryStock=0
        otherAssets=0
        cash=0
        totalCurrentLiabilities=0
        shortLongTermDebt=0
        propertyPlantEquipment=0
        totalCurrentAssets=0
        netTangibleAssets=0
        netReceivables=0
        longTermDebt=0
        inventory=0
        accountsPayable=0       

        if 'intangibleAssets' in year and len(year['intangibleAssets']) > 0:
            intangibleAssets = year['intangibleAssets']['raw']
        if 'capitalSurplus' in year and len(year['capitalSurplus']) > 0:
            capitalSurplus = year['capitalSurplus']['raw']
        if 'totalLiab' in year and len(year['totalLiab']) > 0:
            totalLiab = year['totalLiab']['raw']
        if 'totalStockholderEquity' in year and len(year['totalStockholderEquity']) > 0:
            totalStockholderEquity = year['totalStockholderEquity']['raw']
        if 'otherCurrentLiab' in year and len(year['otherCurrentLiab']) > 0:
            otherCurrentLiab = year['otherCurrentLiab']['raw']
        if 'totalAssets'in year and len(year['totalAssets']) > 0:
            totalAssets = year['totalAssets']['raw']
        if 'endDate' in year and len(year['endDate']) > 0:
            endDate = year['endDate']['fmt']
        if 'commonStock' in year and len(year['commonStock']) > 0:
            commonStock =year['commonStock']['raw']
        if 'otherCurrentAssets' in year and len(year['otherCurrentAssets']) > 0:
            otherCurrentAssets = year['otherCurrentAssets']['raw']
        if 'retainedEarnings' in year and len(year['retainedEarnings']) > 0:
            retainedEarnings = year['retainedEarnings']['raw']
        if 'otherLiab' in year and len(year['otherLiab']) > 0:
            otherLiab = year['otherLiab']['raw']
        if 'treasuryStock' in year and len(year['treasuryStock']) > 0:
            treasuryStock = year['treasuryStock']['raw']
        if 'otherAssets' in year and len(year['otherAssets']) > 0:
            otherAssets = year['otherAssets']['raw']
        if 'cash' in year and len(year['cash']) > 0:
            cash = year['cash']['raw']
        if 'totalCurrentLiabilities' in year and len(year['totalCurrentLiabilities']) > 0:
            totalCurrentLiabilities = year['totalCurrentLiabilities']['raw']
        if 'shortLongTermDebt' in year and len(year['shortLongTermDebt']) > 0:
            shortLongTermDebt = year['shortLongTermDebt']['raw']
        if 'propertyPlantEquipment' in year and len(year['propertyPlantEquipment']) > 0:
            propertyPlantEquipment = year['propertyPlantEquipment']['raw']
        if 'totalCurrentAssets' in year and len(year['totalCurrentAssets']) > 0:
            totalCurrentAssets = year['totalCurrentAssets']['raw']
        if 'netTangibleAssets' in year and len(year['netTangibleAssets']) > 0:
            netTangibleAssets = year['netTangibleAssets']['raw']
        if 'netReceivables' in year and len(year['netReceivables']) > 0:
            netReceivables = year['netReceivables']['raw']
        if 'longTermDebt' in year and len(year['longTermDebt']) > 0:
            longTermDebt = year['longTermDebt']['raw']
        if 'inventory' in year and len(year['inventory']) > 0:
            inventory = year['inventory']['raw']
        if 'accountsPayable' in year and len(year['accountsPayable']) > 0:
            accountsPayable = year['accountsPayable']['raw']
        
        c.execute("""insert into balance_sheet (
                                idStock,
                                endDate,
                                intangibleAssets,
                                capitalSurplus,
                                totalLiab,
                                totalStockholderEquity,
                                otherCurrentLiab,
                                totalAssets,
                                commonStock,
                                otherCurrentAssets,
                                retainedEarnings,
                                otherLiab,
                                treasuryStock,
                                otherAssets,
                                cash,
                                totalCurrentLiabilities,
                                shortLongTermDebt,
                                propertyPlantEquipment,
                                totalCurrentAssets,
                                netTangibleAssets,
                                netReceivables,
                                longTermDebt,
                                inventory,
                                accountsPayable
                        )
                        values 
                        (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                        (idstock, 
                         endDate, 
                         intangibleAssets, 
                         capitalSurplus, 
                         totalLiab, 
                         totalStockholderEquity, 
                         otherCurrentLiab, 
                         totalAssets, 
                         commonStock, 
                         otherCurrentAssets, 
                         retainedEarnings, 
                         otherLiab, 
                         treasuryStock, 
                         otherAssets,
                         cash, 
                         totalCurrentLiabilities,
                         shortLongTermDebt, 
                         propertyPlantEquipment, 
                         totalCurrentAssets, 
                         netTangibleAssets, 
                         netReceivables, 
                         longTermDebt, 
                         inventory, 
                         accountsPayable))
        
    conn.commit() 


def update_cash_flow(idstock, history):
    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    for year in history:        
        endDate=datetime.today()
        changeToLiabilities=0
        totalCashflowsFromInvestingActivities=0
        netBorrowings=0
        totalCashFromFinancingActivities=0
        changeToOperatingActivities=0
        issuanceOfStock=0
        netIncome=0
        changeInCash=0        
        repurchaseOfStock=0
        totalCashFromOperatingActivities=0
        depreciation=0
        changeToInventory=0
        changeToAccountReceivables=0
        otherCashflowsFromFinancingActivities=0
        changeToNetincome=0
        capitalExpenditures=0

        if 'endDate' in year and len(year['endDate'])>0:
            endDate=year['endDate']['fmt']
        if 'changeToLiabilities' in year and len(year['changeToLiabilities'])>0:
            changeToLiabilities=year['changeToLiabilities']['raw']
        if 'totalCashflowsFromInvestingActivities' in year and len(year['totalCashflowsFromInvestingActivities'])>0:
            totalCashflowsFromInvestingActivities=year['totalCashflowsFromInvestingActivities']['raw']
        if 'netBorrowings' in year and len(year['netBorrowings'])>0:
            netBorrowings=year['netBorrowings']['raw']
        if 'totalCashFromFinancingActivities' in year and len(year['totalCashFromFinancingActivities'])>0:
            totalCashFromFinancingActivities=year['totalCashFromFinancingActivities']['raw']
        if 'changeToOperatingActivities' in year and len(year['changeToOperatingActivities'])>0:
            changeToOperatingActivities=year['changeToOperatingActivities']['raw']
        if 'issuanceOfStock' in year and len(year['issuanceOfStock'])>0:
            issuanceOfStock=year['issuanceOfStock']['raw']
        if 'netIncome' in year and len(year['netIncome'])>0:
            netIncome=year['netIncome']['raw']
        if 'changeInCash' in year and len(year['changeInCash'])>0:
            changeInCash=year['changeInCash']['raw']
        if 'repurchaseOfStock' in year and len(year['repurchaseOfStock'])>0:
            repurchaseOfStock=year['repurchaseOfStock']['raw']
        if 'totalCashFromOperatingActivities' in year and len(year['totalCashFromOperatingActivities'])>0:
            totalCashFromOperatingActivities=year['totalCashFromOperatingActivities']['raw']
        if 'depreciation' in year and len(year['depreciation'])>0:
            depreciation=year['depreciation']['raw']
        if 'changeToInventory' in year and len(year['changeToInventory'])>0:
            changeToInventory=year['changeToInventory']['raw']
        if 'changeToAccountReceivables' in year and len(year['changeToAccountReceivables'])>0:
            changeToAccountReceivables=year['changeToAccountReceivables']['raw']
        if 'otherCashflowsFromFinancingActivities' in year and len(year['otherCashflowsFromFinancingActivities'])>0:
            otherCashflowsFromFinancingActivities=year['otherCashflowsFromFinancingActivities']['raw']
        if 'changeToNetincome' in year and len(year['changeToNetincome'])>0:
            changeToNetincome=year['changeToNetincome']['raw']
        if 'capitalExpenditures' in year and len(year['capitalExpenditures'])>0:
            capitalExpenditures=year['capitalExpenditures']['raw']

        c.execute(
            """insert into cash_flow
            (
                    idstock,
                    endDate,
                    changeToLiabilities,
                    totalCashflowsFromInvestingActivities,
                    netBorrowings,
                    totalCashFromFinancingActivities,
                    changeToOperatingActivities,
                    issuanceOfStock,
                    netIncome,
                    changeInCash,
                    repurchaseOfStock,
                    totalCashFromOperatingActivities,
                    depreciation,
                    changeToInventory,
                    changeToAccountReceivables,
                    otherCashflowsFromFinancingActivities,
                    changeToNetincome,
                    capitalExpenditures
            )
            values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                    idstock,
                    endDate,
                    changeToLiabilities,
                    totalCashflowsFromInvestingActivities,
                    netBorrowings,
                    totalCashFromFinancingActivities,
                    changeToOperatingActivities,
                    issuanceOfStock,
                    netIncome,
                    changeInCash,
                    repurchaseOfStock,
                    totalCashFromOperatingActivities,
                    depreciation,
                    changeToInventory,
                    changeToAccountReceivables,
                    otherCashflowsFromFinancingActivities,
                    changeToNetincome,
                    capitalExpenditures
            )
        )

    conn.commit() 

        
def update_stock_data(idstock, ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

    querystring = {"symbol":ticker,"region":"BR"}    

    response = requests.request("GET", url, headers=get_yahoo_headers(), params=querystring)

    resp = response.json() 
    
    update_income_statement(idstock, resp['incomeStatementHistory']['incomeStatementHistory'])

    update_balance_sheet(idstock, resp['balanceSheetHistory']['balanceSheetStatements'])

    update_cash_flow(idstock, resp['cashflowStatementHistory']['cashflowStatements'])

def update_stock_profile(idstock, ticker):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"

    querystring = {"symbol":ticker,"region":"BR"}

    response = requests.request("GET", url, headers=get_yahoo_headers(), params=querystring)
    
    resp = response.json()

    zip = ''
    sector = ''
    fullTimeEmployees = 0
    compensationRisk = 0
    auditRisk = 0
    longBusinessSummary = ''
    city = ''
    phone = ''
    shareHolderRightsRisk = 0
    governanceEpochDate = 0
    boardRisk = 0
    country = ''
    website = ''
    maxAge = 0
    overallRisk = 0
    address1 = ''
    industry = ''
    address2 = ''

    if 'zip' in resp['assetProfile']:
	    zip = resp['assetProfile']['zip']
    if 'sector' in resp['assetProfile']:
	    sector = resp['assetProfile']['sector']
    if 'fullTimeEmployees' in resp['assetProfile']:
	    fullTimeEmployees = resp['assetProfile']['fullTimeEmployees']
    if 'compensationRisk' in resp['assetProfile']:
	    compensationRisk = resp['assetProfile']['compensationRisk']
    if 'auditRisk' in resp['assetProfile']:
	    auditRisk = resp['assetProfile']['auditRisk']
    if 'longBusinessSummary' in resp['assetProfile']:
	    longBusinessSummary = resp['assetProfile']['longBusinessSummary']
    if 'city' in resp['assetProfile']:
	    city = resp['assetProfile']['city']
    if 'phone' in resp['assetProfile']:
	    phone = resp['assetProfile']['phone']
    if 'shareHolderRightsRisk' in resp['assetProfile']:
	    shareHolderRightsRisk = resp['assetProfile']['shareHolderRightsRisk']
    if 'governanceEpochDate' in resp['assetProfile']:
	    governanceEpochDate = resp['assetProfile']['governanceEpochDate']
    if 'boardRisk' in resp['assetProfile']:
	    boardRisk = resp['assetProfile']['boardRisk']
    if 'country' in resp['assetProfile']:
	    country = resp['assetProfile']['country']
    if 'website' in resp['assetProfile']:
	    website = resp['assetProfile']['website']
    if 'maxAge' in resp['assetProfile']:
	    maxAge = resp['assetProfile']['maxAge']
    if 'overallRisk' in resp['assetProfile']:
	    overallRisk = resp['assetProfile']['overallRisk']
    if 'address1' in resp['assetProfile']:
	    address1 = resp['assetProfile']['address1']
    if 'industry' in resp['assetProfile']:
	    industry = resp['assetProfile']['industry']
    if 'address2' in resp['assetProfile']:
	    address2 = resp['assetProfile']['address2'] 

    conn = sqlite3.connect('./db/cs50.db')

    c = conn.cursor()

    c.execute(
        """insert into stock_profile 
        (
            idstock,
            zip,
            sector,
            fullTimeEmployees,
            compensationRisk,
            auditRisk ,
            longBusinessSummary,
            city,
            phone,
            shareHolderRightsRisk,
            governanceEpochDate,
            boardRisk,
            country,
            website,
            maxAge,
            overallRisk,
            address1,
            industry,
            address2
        )
        values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (
            idstock, zip, sector, fullTimeEmployees, compensationRisk, auditRisk, longBusinessSummary, city, phone, shareHolderRightsRisk, 
            governanceEpochDate, boardRisk, country, website, maxAge, overallRisk, address1, industry, address2            
        )    
    )

    conn.commit()
    

def update_all_stocks_data():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()    
    c.execute("delete from income_statement")
    c.execute("delete from balance_sheet")
    c.execute("delete from cash_flow")
    c.execute("delete from stock_profile")
    conn.commit()
    c.execute("select id, ticker from stock")
    rows = c.fetchall()    
    for row in rows:
        idstock = row[0]
        symbol = '{0}.SA'.format(row[1])
        print(symbol)
        try:
            update_stock_profile(idstock, symbol)
            update_stock_data(idstock, symbol)
        except:
            print('Error getting data from the next symbol: {}'.format(symbol))

update_stock_profile(168, 'BTOW3.SA')