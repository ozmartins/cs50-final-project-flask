import sqlite3

def create_indicators_record():
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("select count(*) from indicators")
    rows = c.fetchall()
    if len(rows) == 0:
        c.execute("insert into indicators (Id) values (1)")    

def update_ibovespa():
    print("update_ibovespa")
    create_indicators_record()
    conn = sqlite3.connect('./db/cs50.db')
    c = conn.cursor()
    c.execute("""update indicators set 
                    IbovespaCurrent=?,
                    IbovespaMin52Weeks=?,
                    IbovespaMax52Weeks=?,
                    IfixAtual=?,
                    IfixMin52Weeks=?,
                    IfixMax52Week=?,
                    Selic12Months=?,
                    SelicCurrentMonth=?,
                    SelicMonthName=?,
                    CDI12Months=?,
                    CDIMesCurrent=?,
                    CDIMonthName=?,
                    IPCA12Months=?,
                    IPCACurrentMonth=?,
                    IPCAMonthName=?
                where id = 1""",
                (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
    conn.commit()                

update_ibovespa()
