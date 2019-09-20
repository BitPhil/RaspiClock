$(document).ready(function(){
    
    // Create two variable with the names of the months and days in an array
    var monthNames = [ "Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember" ]; 
    var dayNames= ["Sonntag","Montag","Dienstag","Mittwoch","Donnerstag","Freitag","Samstag"]
    
    // Create a newDate() object
    var newDate = new Date();
    // Extract the current date from Date object
    newDate.setDate(newDate.getDate());
    // Output the day
    $('#Day').html(dayNames[newDate.getDay()])
    // Output the date, month and year   
    $('#Date').html(newDate.getDate() + '. ' + monthNames[newDate.getMonth()] + ' ' + newDate.getFullYear());
    


    setInterval( function() {
        // Create a newDate() object and extract the seconds of the current time on the visitor's
        var seconds = new Date().getSeconds();
        // Add a leading zero to seconds value
        $("#sec").html(( seconds < 10 ? "0" : "" ) + seconds);
    },1000);
        
    setInterval( function() {
        // Create a newDate() object and extract the minutes of the current time on the visitor's
        var minutes = new Date().getMinutes();
        // Add a leading zero to the minutes value
        $("#min").html(( minutes < 10 ? "0" : "" ) + minutes);
    },1000);
        
    setInterval( function() {
        // Create a newDate() object and extract the hours of the current time on the visitor's
        var hours = new Date().getHours();
        // Add a leading zero to the hours value
        $("#hours").html(( hours < 10 ? "0" : "" ) + hours);
    }, 1000);
});

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
                $("#btn_color").style.color = 'orange';
            },
            error: function(error) {
                console.log(error);
                alert("error");
                $("#btn_color").style.color = 'black';
            }
        });
    });
});