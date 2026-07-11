let secretNumber = Math.floor(Math.random() * 10) + 1;
let attempts = 0;

const guessInput = document.getElementById("guess");
const submitButton = document.getElementById("submitGuess");
const resetButton = document.getElementById("resetGame");
const message = document.getElementById("message");
const attemptsDisplay = document.getElementById("attempts");

function checkGuess() {
  const userGuess = Number(guessInput.value);
  attempts = attempts + 1;

  if (userGuess < 1 || userGuess > 10 || guessInput.value === "") {
    message.textContent = "Please enter a number between 1 and 10.";
  } else if (userGuess === secretNumber) {
    message.textContent = `Correct. The number was ${secretNumber}.`;
  } else if (userGuess < secretNumber) {
    message.textContent = "Too low. Try again.";
  } else {
    message.textContent = "Too high. Try again.";
  }

  attemptsDisplay.textContent = `Attempts: ${attempts}`;
  guessInput.value = "";
}

function resetGame() {
  secretNumber = Math.floor(Math.random() * 10) + 1;
  attempts = 0;
  message.textContent = "Enter a number to begin.";
  attemptsDisplay.textContent = "Attempts: 0";
  guessInput.value = "";
}

submitButton.addEventListener("click", checkGuess);
resetButton.addEventListener("click", resetGame);
