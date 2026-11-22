```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Rock Paper Scissors</title>
    <style>
        /* ---------- BASIC LAYOUT ---------- */
        body {
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            background: #f0f4f8;
            color: #333;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        h1 {
            margin-top: 2rem;
            color: #2c3e50;
        }

        .game {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,.1);
            padding: 2rem;
            margin-top: 1rem;
            text-align: center;
            width: 320px;
        }

        .choices button {
            font-size: 1.2rem;
            padding: 0.6rem 1rem;
            margin: 0.5rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: transform .1s, background .2s;
        }

        .choices button:hover {
            transform: scale(1.07);
        }

        .choices button:active {
            transform: scale(0.95);
        }

        .rock  { background:#e74c3c; color:#fff; }
        .paper { background:#3498db; color:#fff; }
        .scissors { background:#2ecc71; color:#fff; }

        .result {
            margin-top: 1.5rem;
            font-size: 1.2rem;
            min-height: 2rem;
        }

        .scoreboard {
            margin-top: 1rem;
            font-size: 1rem;
        }

        .scoreboard span {
            font-weight: bold;
        }

        footer {
            margin-top: auto;
            padding: 1rem;
            font-size: .85rem;
            color: #777;
        }
    </style>
</head>
<body>

    <h1>Rock‑Paper‑Scissors</h1>

    <div class="game">
        <div class="choices">
            <button class="rock"     data-choice="rock">✊ Rock</button>
            <button class="paper"    data-choice="paper">✋ Paper</button>
            <button class="scissors" data-choice="scissors">✌️ Scissors</button>
        </div>

        <div class="result" id="result">Make your move!</div>

        <div class="scoreboard">
            You: <span id="playerScore">0</span> |
            Computer: <span id="computerScore">0</span>
        </div>
    </div>

    <footer>© 2026 – Rock‑Paper‑Scissors demo</footer>

    <script>
        // ------- GLOBAL STATE -------
        const choices = ["rock", "paper", "scissors"];
        let playerScore = 0;
        let computerScore = 0;

        // ------- DOM ELEMENTS -------
        const resultDiv = document.getElementById('result');
        const playerScoreSpan = document.getElementById('playerScore');
        const computerScoreSpan = document.getElementById('computerScore');
        const buttons = document.querySelectorAll('.choices button');

        // ------- HELPER FUNCTIONS -------
        function getComputerChoice() {
            const randIdx = Math.floor(Math.random() * choices.length);
            return choices[randIdx];
        }

        function decideWinner(player, computer) {
            if (player === computer) return "draw";
            // rock beats scissors, scissors beats paper, paper beats rock
            if (
                (player === "rock" && computer === "scissors") ||
                (player === "scissors" && computer === "paper") ||
                (player === "paper" && computer === "rock")
            ) {
                return "win";
            }
            return "lose";
        }

        function updateScoreboard() {
            playerScoreSpan.textContent = playerScore;
            computerScoreSpan.textContent = computerScore;
        }

        function showResult(player, computer, outcome) {
            const emojis = { rock: "✊", paper: "✋", scissors: "✌️" };
            let msg = `You chose ${emojis[player]} ${player}, computer chose ${emojis[computer]} ${computer}. `;

            if (outcome === "win") {
                msg += "You win! 🎉";
                resultDiv.style.color = "#27ae60";
            } else if (outcome === "lose") {
                msg += "You lose. 😢";
                resultDiv.style.color = "#c0392b";
            } else {
                msg += "It's a draw. 🤝";
                resultDiv.style.color = "#7f8c8d";
            }

            resultDiv.textContent = msg;
        }

        // ------- MAIN LOGIC -------
        buttons.forEach(btn => {
            btn.addEventListener('click', () => {
                const playerChoice = btn.dataset.choice;
                const computerChoice = getComputerChoice();
                const outcome = decideWinner(playerChoice, computerChoice);

                // Update scores
                if (outcome === "win") playerScore++;
                else if (outcome === "lose") computerScore++;

                updateScoreboard();
                showResult(playerChoice, computerChoice, outcome);
            });
        });

        // Initialize scoreboard
        updateScoreboard();
    </script>
</body>
</html>
```

### How it works
1. **HTML** – Buttons for the three moves (`rock`, `paper`, `scissors`) each carry a `data-choice` attribute.
2. **CSS** – Simple styling gives the page a clean look, with distinct colors for each button and a subtle card‑like container.
3. **JavaScript** –  
   * Randomly picks a computer move.  
   * Compares the player’s selection with the computer’s to decide win/lose/draw.  
   * Updates the displayed result and the running scores.

Open the file in any modern browser and start playing! Feel free to expand it (e.g., add a reset button, play‑to‑10 logic, or animation) – the foundation is all there. Enjoy!