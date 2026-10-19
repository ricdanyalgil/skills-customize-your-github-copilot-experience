# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game to practice string manipulation, loops, conditionals, random selection, and handling user input in Python.

## 📝 Tasks

### 🛠️ Select a Random Word

#### Description
Create a predefined list of words and write code that randomly selects one word for each new game.

#### Requirements
Completed program should:

- Define a list of at least 5 words.
- Use the `random` module to pick one word at the start of each game.

### 🛠️ Accept Guesses and Show Progress

#### Description
Prompt the player to guess one letter at a time and display the word with unguessed letters hidden.

#### Requirements
Completed program should:

- Accept a single letter guess using `input()`.
- Show current progress in `_ _ _` format, revealing correctly guessed letters.
- Example output:
  ```
  Word: p _ t h _ n
  Guess a letter: o
  Word: p _ t h o n
  ```

### 🛠️ Track Attempts and End the Game

#### Description
Keep track of incorrect guesses and end the game when the word is guessed or the player runs out of attempts.

#### Requirements
Completed program should:

- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed or attempts are exhausted.
- Display a win or lose message, revealing the word at the end.
