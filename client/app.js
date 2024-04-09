function onClickedGetSensorData(){
    console.log("Get sensor button clicked");
    
    var temp = document.getElementById("uitemp");
    var hum = document.getElementById("uihum");
    

    var url = "http://127.0.0.1:5000/get_sensor_data";
    $.get(url,function(data, status) {
        if(data) {
            const result = data.result;
            const res_array = JSON.parse(result); 
            temp.value = res_array[0].toString();
            hum.value = res_array[1].toString();
        }
    });
}

function onClickedEstimateRainfall(){
    console.log("Estimate rainfall button clicked");
    var temp = document.getElementById("uitemp");
    var hum = document.getElementById("uihum");
    var estRain = document.getElementById("uiEstimatedRain");

    var url = "http://127.0.0.1:5000/predict_rainfall";

    $.post(url, {
        temperature: parseFloat(temp.value),
        humidity: parseFloat(hum.value)
    },function(data, status) {
        console.log(data.estimated_rainfall);
        estRain.innerHTML = data.estimated_rainfall.toString() + " mm";
        console.log(status);
    });
}
