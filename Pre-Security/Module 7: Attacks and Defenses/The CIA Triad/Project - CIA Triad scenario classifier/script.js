const scenarios = [
  {
    text: "An employee's password is stolen and used to access private company files.",
    answer: "Confidentiality",
    explanation: "Confidentiality is affected because unauthorized access exposed sensitive information."
  },
  {
    text: "A database record is changed without approval, causing incorrect customer information.",
    answer: "Integrity",
    explanation: "Integrity is affected because the data was modified without authorization."
  },
  {
    text: "A denial-of-service attack prevents users from accessing a website.",
    answer: "Availability",
    explanation: "Availability is affected because authorized users cannot access the service."
  },
  {
    text: "A backup system allows a company to restore files after a server failure.",
    answer: "Availability",
    explanation: "Availability is protected because backups help keep data accessible."
  },
  {
    text: "A file hash changes after a software download, suggesting the file was altered.",
    answer: "Integrity",
    explanation: "Integrity is affected because the file may no longer be accurate or trustworthy."
  },
  {
    text: "Encryption prevents unauthorized users from reading sensitive data.",
    answer: "Confidentiality",
    explanation: "Confidentiality is protected because encryption limits who can understand the data."
  }
];

let currentScenario = null;
let score = 0;
let attempts = 0;

const scenarioText = document.getElementById("scenario");
const feedback = document.getElementById("feedback");
const scoreDisplay = document.getElementById("score");
const newScenarioButton = document.getElementById("newScenario");
const answerButtons = document.querySelectorAll("[data-answer]");

function loadScenario() {
  const randomIndex = Math.floor(Math.random() * scenarios.length);
  currentScenario = scenarios[randomIndex];
  scenarioText.textContent = currentScenario.text;
  feedback.textContent = "Choose the CIA Triad principle affected by the scenario.";
}

function checkAnswer(selectedAnswer) {
  if (!currentScenario) {
    feedback.textContent = "Click New Scenario to begin.";
    return;
  }

  attempts = attempts + 1;

  if (selectedAnswer === currentScenario.answer) {
    score = score + 1;
    feedback.textContent = `Correct. ${currentScenario.explanation}`;
  } else {
    feedback.textContent = `Not quite. The answer is ${currentScenario.answer}. ${currentScenario.explanation}`;
  }

  scoreDisplay.textContent = `Score: ${score} / ${attempts}`;
}

answerButtons.forEach((button) => {
  button.addEventListener("click", () => {
    checkAnswer(button.dataset.answer);
  });
});

newScenarioButton.addEventListener("click", loadScenario);

loadScenario();
