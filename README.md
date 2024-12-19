# Dumb-peoples-game
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tricky Trigonometry Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: white;
            padding: 15px;
            text-align: center;
        }
        .game-container {
            margin: 20px auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            text-align: center;
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .options {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        .button:hover {
            background-color: #45a049;
        }
        .result {
            font-size: 18px;
            margin-top: 20px;
            font-weight: bold;
        }
        .play-again {
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #FF5722;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>

<header>
    <h1>Dumb peoples game</h1>
    <p>Test your knowledge of sine and cosine laws!</p>
</header>

<div class="game-container" id="gameContainer">
    <p class="question" id="questionText">Ready for a tricky question?</p>
    <div class="options" id="optionsContainer">
        <button class="button" onclick="checkAnswer('wrong')">Start Game</button>
    </div>
    <p class="result" id="resultText"></p>
</div>

<script>
    const questions = [
        {
            question: "Using the sine rule, find angle A: a = 10, b = 8, C = 60°.",
            options: [35.26, 45.5, 50.8],
            correctAnswer: 35.26
        },
        {
            question: "Using the cosine rule, find the side c: a = 5, b = 7, C = 60°.",
            options: [5.5, 8.0, 10.5],
            correctAnswer: 5.5
        },
        {
            question: "In a triangle ABC, a = 12, b = 15, angle C = 45°. What is the length of side c using the cosine law?",
            options: [18, 16, 14],
            correctAnswer: 16
        },
        {
            question: "Find angle B using sine law: a = 8, b = 10, c = 12.",
            options: [30, 50, 60],
            correctAnswer: 50
        },
        {
            question: "A triangle has sides a = 7, b = 10, c = 13. What is angle A using the cosine law?",
            options: [25, 30, 45],
            correctAnswer: 30
        }
    ];

    let currentQuestionIndex = 0;
    let score = 0;

    function loadQuestion() {
        const currentQuestion = questions[currentQuestionIndex];
        document.getElementById('questionText').textContent = currentQuestion.question;
        const optionsContainer = document.getElementById('optionsContainer');
        optionsContainer.innerHTML = '';
       
        currentQuestion.options.forEach(option => {
            const button = document.createElement('button');
            button.classList.add('button');
            button.textContent = option;
            button.onclick = () => checkAnswer(option);
            optionsContainer.appendChild(button);
        });
    }

    function checkAnswer(answer) {
        const currentQuestion = questions[currentQuestionIndex];
        const resultText = document.getElementById('resultText');
       
        if (answer === currentQuestion.correctAnswer) {
            score++;
            resultText.textContent = "Correct! Nice job!";
            resultText.style.color = "green";
        } else {
            resultText.textContent = " Haha, Youre Retarted and you got hacked!Mwahahahahaha";
            resultText.style.color = "red";
        }

        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            setTimeout(loadQuestion, 2000); // Move to next question after 2 seconds
        } else {
            setTimeout(endGame, 2000); // End the game after all questions
        }
    }

    function endGame() {
        const gameContainer = document.getElementById('gameContainer');
        gameContainer.innerHTML = `
            <p class="question">Game Over!</p>
            <p class="result">Your score: ${score} out of ${questions.length}</p>
            <button class="play-again" onclick="restartGame()">Play Again</button>
        `;
    }

    function restartGame() {
        currentQuestionIndex = 0;
        score = 0;
        document.getElementById('resultText').textContent = '';
        loadQuestion();
    }

    loadQuestion(); // Start the game with the first question
</script>

</body>
</html>

