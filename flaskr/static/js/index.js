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
    setInterval(() => {setWidgetData_1659676024(data)}, 10)
}

//#region light
// when light-button is clicked, the connected light should be turned on/off
// actual status is shown bei button color
getElementbyid(light).addEventListener("click", lightOnOff)
function lightOnOff(){
    alert("light switched:" + toString(status))
}



//#endregion