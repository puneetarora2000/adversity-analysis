google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(drawBasic);

    function drawBasic() {

      var data = google.visualization.arrayToDataTable([
        ['City', '2010 Population',],
        ['New York City, NY', 8175000],
        ['Los Angeles, CA', 3792000],
        ['Chicago, IL', 2695000],
        ['Houston, TX', 2099000],
        ['Philadelphia, PA', 1526000]
      ]);

      var options = {
        title: 'Population of Largest U.S. Cities',
        chartArea: {width: '50%'},
        hAxis: {
          title: 'Total Population',
          minValue: 0
        },
        vAxis: {
          title: 'City'
        }
      };

      var chart = new google.visualization.BarChart(document.getElementById('attack_method_graph'));

    }

$(document).ready(function() {
    attack_methods = $.parseJSON($('#attack_methods').val());
    console.log(attack_methods);
    attack_method_data = [];

    attack_methods.forEach(function(a) {
        attack_method_data.push([a.Spear_Attack_Method__AttackMethod, a.attackcount]);
    });
    console.log(attack_method_data);
    data = [["Clone-Site-Link", 1], ["Not Available", 9]];


});

