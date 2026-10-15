
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a text-based Hangman game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Secret Word

#### Description
Create the data and game setup needed to select a secret word and display the player's initial progress.

#### Requirements
Completed program should:

- Store at least five possible words in a predefined list.
- Randomly select one word from the list at the start of each game.
- Display one underscore for each letter in the secret word, such as `_ _ _ _ _`.
- Set and display a limit for the number of incorrect guesses.

### 🛠️ Implement the Guessing Game

#### Description
Allow the player to guess letters and continue playing until the word is revealed or the player runs out of attempts.

#### Requirements
Completed program should:

- Accept a letter guess from the player during each turn.
- Reveal correctly guessed letters in their positions and keep unguessed letters hidden.
- Track incorrect guesses and show the number of attempts remaining.
- Continue until the player guesses the complete word or uses all allowed incorrect guesses.
- Display a clear win message when the word is guessed and a clear lose message that reveals the word when attempts are exhausted.
