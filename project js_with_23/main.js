let userScore = 0;
let compScore = 0;

const choices = document.querySelectorAll(".choice"); 
const msg = document.querySelector("#msg");
const userScorePara = document.querySelector("#user-score");
const compScorePara = document.querySelector("#comp-score");

const genCompChoice = () => {
    const options = ["rock", "paper", "scissor"];
    const randIdx = Math.floor(Math.random() * 3);
    return options[randIdx];
};

const drawGame = () => {
    
    msg.innerText = "Game was a Draw. Play again.";
    msg.style.backgroundColor = "#081b31";
};

const showWinner = (userWin,userChoice, compChoice) => {
    if(userWin) {
         userScore++;
         userScorePara.innerText = userScore;
        msg.innerText = `You win! Your ${userChoice} beats ${compChoice}`;
        msg.style.backgroundColor = "green";
    } else {
         compScore++;
          compScorePara.innerText = compScore;
         
        msg.innerText = `You lose! beats your ${userChoice} beats ${compChoice}`;
        msg.style.backgroundColor = "red";
    }
};

const playGame = (userChoice) => {
    
    const compChoice = genCompChoice();
    

    if(userChoice === compChoice) {
        drawGame();
    } else {
        let userWin;
        if(userChoice === "rock") {
            userWin = compChoice === "scissor" ? true : false;
        } else if(userChoice === "paper") {
            userWin = compChoice === "rock" ? true : false;
        } else if(userChoice === "scissor") {
            userWin = compChoice === "paper" ? true : false;
        }

        showWinner(userWin, userChoice,compChoice);
    }
};

// Event listeners
choices.forEach((choice) => {
    choice.addEventListener("click", () => {
        const userChoice = choice.getAttribute("id");
        console.log("Choice was clicked:", userChoice);
        playGame(userChoice);
    });
});
