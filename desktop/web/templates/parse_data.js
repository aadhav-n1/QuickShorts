async function render(){
    let data= {};
    const r_buttons= document.getElementsByName("radio_button");
    let selected_value= 0;
    for(const button in r_buttons){
        if(r_buttons[button].checked) selected_value= button;
    }
    console.log("Value is", selected_value);
    data= await eel.parseNews( parseInt(selected_value)+1 )();
    data= JSON.parse(data);
    const news_tags= ["news1","news2","news3","news4","news5"];
    for(let i=1; i<=5; i++){
        document.getElementById("news_"+i+"_title").innerHTML = data["news_"+i+"_title"];
        document.getElementById("news"+i).innerHTML= data["news_"+i];
        document.getElementById("title").innerHTML = data["title"];
    }
}
render();
