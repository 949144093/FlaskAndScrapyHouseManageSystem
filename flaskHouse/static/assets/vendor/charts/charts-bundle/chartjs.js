(function(window, document, $, undefined) {
        "use strict";
        var chartdata = [];
        var chartlabel=[];
        $(function() {
            $.ajax({
                url:'/get_housecount',
                type:'POST',
                dataType:'json',
                success:function (data){
                    if(data){
                        for(var key in data){
                            chartlabel.push(key)
                            chartdata.push(data[key])
                            // cls[index] = key;
                            // num[index++] = data[key+''];
                        }
                         if ($('#chartjs_bar').length) {
                var ctx = document.getElementById("chartjs_bar").getContext('2d')   ;
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: chartlabel,
                        datasets: [{
                            label: '房源数量',
                            data: chartdata,
                            backgroundColor: "rgba(89, 105, 255,0.5)",
                            borderColor: "rgba(89, 105, 255,0.7)",
                            borderWidth: 2
                        }]
                    },
                    options: {
                        scales: {
                            yAxes: [{

                            }]
                        },
                             legend: {
                        display: true,
                        position: 'bottom',

                        labels: {
                            fontColor: '#71748d',
                            fontFamily: 'Circular Std Book',
                            fontSize: 14,
                        }
                    },
                }
                });
            }

            if ($('#chartjs_pie').length) {
                var ctx = document.getElementById("chartjs_pie").getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'pie',
                    data: {
                        labels: chartlabel,
                        datasets: [{
                            backgroundColor: [
                               "#5969ff",
                                "#ff407b",
                                "#25d5f2",
                                "#ffc750",
                                "#2ec551",
                            ],
                            data: chartdata
                        }]
                    },
                    options: {
                        legend: {
                        display: true,
                        position: 'bottom',

                        labels: {
                            fontColor: '#71748d',
                            fontFamily: 'Circular Std Book',
                            fontSize: 14,
                        }
                    },


                }
                });
            }

                    }
                }
            });







        });

})(window, document, window.jQuery);