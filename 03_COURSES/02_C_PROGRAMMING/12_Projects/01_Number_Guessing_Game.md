---
tags: [c-programming, projects, game-development]
---

# Project 1: Number Guessing Game

## Goal
Write a program that generates a random number and asks the player to guess it.

## Rules
- If the player's guess is higher than the actual number, display "Lower number please".
- If the player's guess is too low, display "Higher number please".
- When the player guesses the correct number, display the number of guesses used to arrive at the number.

## Hints
- Use a loop (like `while` or `do-while`).
- Use a random number generator (`rand()` from `stdlib.h` and `time()` from `time.h`).

## Logic Overview
1. Generate a random number between 1 and 100.
2. Initialize a counter for guesses.
3. Start a loop to take user input.
4. Compare user input with the random number and provide feedback.
5. Exit loop when the guess is correct.
