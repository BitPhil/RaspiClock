//#region weather

function setWidgetData_1659676024(data){ 
    if(typeof(data) != 'undefined' && data.results.length > 0) {
        for(let i = 0; i < data.results.length; ++i) { 
            let objMainBlock = '';
            const params = data.results[i];
            objMainBlock = document.getElementById('tw_'+params.widget_type+'_'+params.widget_id);
            if(objMainBlock !== null) objMainBlock.innerHTML = params.html_code;
        } 
    }
    console.log(data);
}
let clock_timer_1659676024 = -1;
                
function refresh(){
    setInterval(() => {setWidgetData_1659676024(data)}, 10);
}
//#endregion

//#region light
// when light-button is clicked, the connected light should be turned on/off
// actual status is shown bei button color

$(document).ready(function(){  
    $("#light_on").click(function(){
        alert("Clicked");
        // prüfen, ob Licht an oder aus ist (Hue-Abfrage, Datenbank, CSV, ...)
        
        // data im folgenden ajax dementsprechend True (wenn Licht aus ist) oder False (wenn Licht an ist) setzen
        $.ajax({
            url: '/_light',
            data: {'status_on':'True'},
            type: 'POST',
            success: function(response) {
                console.log(response);
                alert("success");
            },
            error: function(error) {
                console.log(error);
                alert("error");
            }
        });
    });
});

/*
Light_on = false;

function switch_light(){
    if(Light_on == false){
        Light_on = true;
        document.getElementById('btn_color').style.color = 'orange';
    }
    else{
        Light_on = false;
        document.getElementById('btn_color').style.color = 'black';
    }
}
//#endregion

*/