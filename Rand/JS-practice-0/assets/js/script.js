document.querySelectorAll(".blue-bg-button").forEach( element=> {
    addEventListener("click", btnclicked)})

function btnclicked() {
    alert("button clicked")
}
document.querySelectorAll(".border-btn").forEach(element => {
    addEventListener("click", btnclicked)
});