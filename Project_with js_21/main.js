// let btn1 = document.querySelector("#btn1");
// btn1.onclick = () => {
//     console.log("btn1 was cliked");
//     let a = 25;
//     a++;
//     console.log(a);//26
// }
// let div = document.querySelector("div");
// div.onmouseover = () => {
//     console.log("you are inside div");
// }

btn1.addEventListener("click", () => {
    console.log("button1 was clicked - handler1");
});

btn1.addEventListener("click", () => {
    console.log("button1 was clicked - handler2");
});

const handler3 = () => {
    console.log("button1 was clicked - handler3");
};

btn1.addEventListener("click", handler3);

btn1.addEventListener("click", () => {
    console.log("button1 was clicked - handler4");
});

btn1.removeEventListener("click", handler3);

