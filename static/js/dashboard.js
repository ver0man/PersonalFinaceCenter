/**
 * Created by Truman on 1/19/16.
 */

$(document).ready(function () {
    var statistic_plot = {

        chart: {
            renderTo: 'statistics',
            type: 'column'
        },

        title: {
            text: 'Wallet Total'
        },

        xAxis: {
            categories: []
        },
        series: [{
            name: 'Income',
            data: []
        }, {
            name: 'Expense',
            data: []
        }, {
            name: 'Total',
            data: []
        }]
    };

    var chartDataUrl = "/wallet/statistics/";
    $.getJSON(chartDataUrl, function (data) {
        statistic_plot.xAxis.categories = data['xAxis'];
        statistic_plot.series[0].data = data['income'];
        statistic_plot.series[1].data = data['expense'];
        statistic_plot.series[2].data = data['total'];
        var chart = new Highcharts.Chart(statistic_plot);
    });


    var contrast_plot = {

        chart: {
            renderTo: 'contrast',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'Repo Share'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        series: [{
            name: 'Repos',
            colorByPoint: true,
            data: []
        }]
    };

    var chartDataUrl2 = "/wallet/contrast/";
    $.getJSON(chartDataUrl2, function (data) {
        contrast_plot.series[0].data = data['total'];
        var chart2 = new Highcharts.Chart(contrast_plot);
    });

});
