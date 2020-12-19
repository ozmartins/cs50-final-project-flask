income_statement = []
cash_flow = []
balance_sheet = []

function getIncomeStatement(symbol) {
    axios.get('/income_statement/' + symbol).then((response) => {              
        income_statement[0] = ['Ano', 'Receita Líquida', 'Lucro Líquido'];        
        for (var i = 0; i < response.data.length; i++) {
            income_statement[i+1] = []
            income_statement[i+1][0] = response.data[i]['endDate']
            income_statement[i+1][1] = response.data[i]['totalRevenue']
            income_statement[i+1][2] = response.data[i]['netIncome']
          }                
        
    });
}

function getCashFlow(symbol) {
    axios.get('/cash_flow/' + symbol).then((response) => {              
        cash_flow[0] = ['Ano', 'FCI', 'FCF', 'FCO'];        
        for (var i = 0; i < response.data.length; i++) {
            cash_flow[i+1] = []
            cash_flow[i+1][0] = response.data[i]['endDate']
            cash_flow[i+1][1] = response.data[i]['totalCashflowsFromInvestingActivities']
            cash_flow[i+1][2] = response.data[i]['totalCashFromFinancingActivities']
            cash_flow[i+1][3] = response.data[i]['totalCashFromOperatingActivities']
          }                
        
    });
}

function getBalanceSheet(symbol) {
    axios.get('/balance_sheet/' + symbol).then((response) => {              
        balance_sheet[0] = ['Ano', 'Caixa', 'Dívida'];        
        for (var i = 0; i < response.data.length; i++) {
            balance_sheet[i+1] = []
            balance_sheet[i+1][0] = response.data[i]['endDate']
            balance_sheet[i+1][1] = response.data[i]['cash']
            balance_sheet[i+1][2] = response.data[i]['longTermDebt']            
          }                
        
    });
}

getIncomeStatement(document.getElementById('ticker').value)
getCashFlow(document.getElementById('ticker').value)
getBalanceSheet(document.getElementById('ticker').value)

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChartIncomeStatement);
google.charts.setOnLoadCallback(drawChartCashFlow);
google.charts.setOnLoadCallback(drawChartBalanceSheet);
    
// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChartIncomeStatement() {
    // Create the data table.
    var data2 = new google.visualization.DataTable();
    data2.addColumn('string', 'Ano');
    data2.addColumn('number', 'Receita Líquida');
    data2.addColumn('number', 'Lucro Líquido');        
    
    var data = google.visualization.arrayToDataTable(income_statement);

    // Set chart options
    var options = {
                    title:'DRE',                       
                    height:500,
                    vAxis: {
                        title: 'Valor em reais'
                    }
                };

    // Instantiate and draw our chart, passing in some options.
    var dre = new google.visualization.ColumnChart (document.getElementById('dre'));        

    dre.draw(data, options);
}

function drawChartCashFlow() {
    // Create the data table.
    var data2 = new google.visualization.DataTable();
    data2.addColumn('string', 'Ano');
    data2.addColumn('number', 'FCI');
    data2.addColumn('number', 'FCF'); 
    data2.addColumn('number', 'FCO'); 
    
    var data = google.visualization.arrayToDataTable(cash_flow);

    // Set chart options
    var options = {
                    title:'Fluxo de caixa',                       
                    height:500,
                    vAxis: {
                        title: 'Valor em reais'
                    }
                };

    // Instantiate and draw our chart, passing in some options.
    var fluxoCaixa = new google.visualization.ColumnChart (document.getElementById('fluxoCaixa'));        

    fluxoCaixa.draw(data, options);
}

function drawChartBalanceSheet() {
    // Create the data table.
    var data2 = new google.visualization.DataTable();
    data2.addColumn('string', 'Ano');
    data2.addColumn('number', 'caixa');
    data2.addColumn('number', 'Dívida');     
    
    var data = google.visualization.arrayToDataTable(balance_sheet);

    // Set chart options
    var options = {
                    title:'Caixa e dívida',
                    height:500,
                    vAxis: {
                        title: 'Valor em reais'
                    }
                };

    // Instantiate and draw our chart, passing in some options.
    var balanceSheet = new google.visualization.ColumnChart (document.getElementById('balanceSheet'));        

    balanceSheet.draw(data, options);
}