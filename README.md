## python-guess-game
A simple Python game where the player has to guess a randomly generated number within a given range.

## Overview
In this game, the computer generates a random number within a specified range, and the player must guess the number. The game will give feedback on whether the guess is too low or too high until the correct number is guessed.

## Features
-> Random number generation between a specified range.
-> Feedback on whether the guessed number is too high, too low, or correct.
-> Option to play again after finishing the game.

## Requirements
-> Python 3.x
-> No external libraries are required.

## How to Play
-> Run the Python script.
-> The computer will ask you to guess a number within a given range.
-> You input your guess.
-> The computer will tell you whether your guess is too high, too low, or correct.
-> If you guess correctly, you can choose to play again.

## Installation
Clone the repository or download the guess_game.py script.
  git clone https://github.com/y18-h21/python-guess-game.git

Navigate to the directory where the file is located:
   cd random-guess-game

Run the game using Python:
   python randomguess.py
   
## Code Explanation
The game starts by generating a random number between 1 and 100 (you can adjust the range in the code).
The player is asked to input a guess.
After each guess, feedback is provided (too high, too low, or correct).
The game continues until the player guesses the number correctly.
Once the number is guessed correctly, the player is given the option to restart the game.

## Example Output
Welcome to the Random Guess Game!
I'm thinking of a number between 1 and 100.

Please guess a number: 50
Too high! Try again.

Please guess a number: 30
Too low! Try again.

Please guess a number: 40
Correct! You guessed the number!

Do you want to play again? (y/n): n
Thank you for playing!
