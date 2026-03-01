
let boxes = document.querySelectorAll(".box");
let resetbtn = document.querySelector("#reset-button");
let declareWinner = document.querySelector("#result");
let startbtn = document.querySelector("#start-game");

let turn0 = true; // player x , player 0

const resetGame = () => {
    turn0 = true;
    enableBoxes();

};

const enableBoxes = () => {
    for (let box of boxes) {
        box.innerText = "";
        box.disabled = false;
    }
};





const winPattern = [
    [0, 1, 2],
    [0, 3, 6],
    [0, 4, 8],
    [1, 4, 7],
    [2, 5, 8],
    [2, 4, 6],
    [3, 4, 5],
    [6, 7, 8]
];

const disable = () => {
    boxes.forEach((box) => {
        box.disabled = true;
    });
};





boxes.forEach((box) => {
    box.addEventListener("click", () => {
        console.log("The box was clicked");
        if (turn0) {
            box.innerText = "0";
            turn0 = false;
        }
        else {
            box.innerText = "X";
            turn0 = true;
        }
        box.disabled = true;
        checkWon();

    });
});

const checkWon = () => {
    for (let pattern of winPattern) {
        let pos1val = boxes[pattern[0]].innerText;
        let pos2val = boxes[pattern[1]].innerText;
        let pos3val = boxes[pattern[2]].innerText;

        if (pos1val != "" && pos1val == pos2val && pos2val == pos3val) {
            if (pos1val === pos2val && pos2val === pos3val) {
                console.log(`${pos1val} has won the game `);

                disable();
                declareWinner.innerText = `The winner is ${pos1val}`;
                console.log(pattern);
                showLine(pattern);

            }
        };
    };
};

resetbtn.addEventListener("click", resetGame);
startbtn.addEventListener("click", resetGame);






