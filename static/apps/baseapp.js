document.addEventListener("DOMContentLoaded", () => {
    console.log("site loaded");
});


function showmenu() {
    var button = document.getElementById("navi");
    if(button.style.display === "block") {
        button.style.display = "none";
    } else {
        button.style.display = "block";
    }
}


async function requestData() {
    const response = await fetch("/button");
    const json = await response.json();
    const value = JSON.stringify(json);
    console.log(value);

    document.getElementById("value").textContent = "Value: " + json.hello;
}