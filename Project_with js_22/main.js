let modeBtn = document.querySelector("#mode");
let curMode = "light";

modeBtn.addEventListener("click", () => {
    if (curMode === "light") {
        curMode = "dark";
        document.body.classList.add("dark");
    } else {
        curMode = "light";
        document.body.classList.remove("dark");
    }
    console.log(curMode);
});
