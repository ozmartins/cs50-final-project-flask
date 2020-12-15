income_statement = []

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

getIncomeStatement("ABEV3")

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);
    
// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {
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