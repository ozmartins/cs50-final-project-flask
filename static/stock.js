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
    data2.addColumn('number', 'EBITDA');
    data2.addColumn('number', 'Lucro Líquido');
    data2.addRows([
        ['2015', 150, 50, 25],
        ['2016', 175, 50, 25],
        ['2017', 200, 50, 25],
        ['2018', 225, 50, 25],
        ['2019', 250, 50, 25]
    ]);

    
    var data = google.visualization.arrayToDataTable([
        ['Ano', 'Receita Líquida', 'EBITDA', 'Lucro Líquido'],
        ['2015', 150, 075, 35],
        ['2016', 200, 100, 50],
        ['2017', 250, 125, 65],
        ['2018', 300, 150, 75],
        ['2019', 350, 175, 95]
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
    var balanco = new google.visualization.ColumnChart (document.getElementById('balanco'));
    var dfc = new google.visualization.ColumnChart (document.getElementById('dfc'));
    var indicadores = new google.visualization.ColumnChart (document.getElementById('indicadores'));

    dre.draw(data, options);
    balanco.draw(data, options);
    dfc.draw(data, options);
    indicadores.draw(data, options);
}