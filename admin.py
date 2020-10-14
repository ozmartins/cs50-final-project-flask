import sqlite3

def update_indicators():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("""insert into indicators (Id, IbovespaCurrent, IbovespaMin52Weeks, IbovespaMax52Weeks,
              IfixAtual, IfixMin52Weeks, IfixMax52Week,
              Selic12Months, SelicCurrentMonth, SelicMonthName,
              CDI12Months, CDIMesCurrent, CDIMonthName,
              IPCA12Months, IPCACurrentMonth, IPCAMonthName)
              values (:Id, :IbovespaCurrent, :IbovespaMin52Weeks, :IbovespaMax52Weeks,
              :IfixAtual, :IfixMin52Weeks, :IfixMax52Week,
              :Selic12Months, :SelicCurrentMonth, :SelicMonthName,
              :CDI12Months, :CDIMesCurrent, :CDIMonthName,
              :IPCA12Months, :IPCACurrentMonth, :IPCAMonthName)""")    

def update_news():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("")