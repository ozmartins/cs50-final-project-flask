income_statement = []

function getIncomeStatement(symbol) {
    axios.get('/income_statement?symbol=' + symbol).then((response) => {              
        alert(response.data);
    });
}

getIncomeStatement("ABEV3.SA")

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
    
    var data = google.visualization.arrayToDataTable([
        ['Ano', 'Receita Líquida', 'Lucro Líquido'],
        ['2015', 150, 35],
        ['2016', 200, 50],
        ['2017', 250, 65],
        ['2018', 300, 75],
        ['2019', 350, 95]
    ]);

    // Set chart options
    var options = {
                    title:'DRE',                       
                    height:500,
                    vAxis: {
                        title: 'Valor em milhões de reais'
                    }
                };

    // Instantiate and draw our chart, passing in some options.
    var dre = new google.visualization.ColumnChart (document.getElementById('dre'));        

    dre.draw(data, options);
}