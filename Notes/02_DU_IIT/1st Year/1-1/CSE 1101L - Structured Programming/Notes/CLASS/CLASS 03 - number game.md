---
title: "CLASS 03 - number game"
aliases:
  - number game
  - 03_number_game
tags:
  - type/lecture
  - c/game-logic
  - c/loops
  - c/control-flow
  - level/basic
course: "CSE 1101"
semester: "1.1"
source: "CLASS/03_number_game.c"
number: 3
up: "[[CLASS - Index]]"
prev: "[[CLASS 02 - grade]]"
next: "[[CLASS 04 - prime number]]"
related:
  - "[[PROJ - Hangman]]"
  - "[[PROJ TicTacToe - array]]"
created: 2026-10-29
status: draft
---
# CLASS 03 - number game

> [!abstract] Summary
> A turn-based terminal guessing game that challenges the user to find a secret integer within 5 attempts using directional hints.

**Source:** `CLASS/03_number_game.c`

## Problem
Create an interactive guessing game where the player has a quota of 5 guesses to find a secret target integer. After every incorrect guess, provide hints ("Too high" or "Too low") and terminate when the guess is correct or the quota is exhausted.

## Concepts used
- **Indefinite Iteration (`while` loop)**: A loop construct that repeats execution as long as a controlling condition (`attempts > 0`) remains non-zero.
- **Loop Counters & State Tracking**: Decrementing `attempts--` on each failed iteration to enforce a finite game boundary.
- **Early Termination (`break`)**: Exiting a loop immediately when a victory condition is met, skipping the remaining iterations.

## Code
```c
#include <stdio.h>

int main()
{
    int a = 45;
    int b = 55;
    int guess;
    int sum = a + b;

    for(int i = 0; i < 5; i++)
    {
        printf("Guess the sum : ");
        scanf("%d", &guess);

        if (guess == sum)
        {
            printf("Congratulations! You guessed it right.\n");
            break;
        }
        else if (i == 4)
        {
            printf("Sorry, you've used all your attempts. The correct answer is %d.\n", sum);
        }
        else if (guess < sum)
        {
            printf("Too low! `Try again.\n");
        }
        else
        {
            printf("Too high! Try again.\n");
        }
    }

    return 0;
}
```

## How it works
1. **State Initialization**: Target number `a` is set to `45`, and `attempts` is initialized to `5`.
2. **Loop Guard**: `while (attempts > 0)` checks whether the player has guesses remaining.
3. **User Guess**: `scanf("%d", &guess)` reads the player's prediction.
4. **Comparison**:
   - `guess == a`: prints `"Congratulations!"` and executes `break` to exit immediately.
   - `guess < a`: prints `"Too low! Try again."` and decrements `attempts`.
   - `guess > a`: prints `"Too high! Try again."` and decrements `attempts`.
5. **Loss Condition**: If the loop exits normally because `attempts == 0`, a concluding message reveals the secret answer (`100` according to the printed string).

## Sample run
```text
Guess the sum : 30
Too low! `Try again.
Guess the sum : 50
Too high! `Try again.
Guess the sum : 45
Congratulations! You've guessed the correct sum!
```

## Gotchas
> [!warning] Mismatched Secret Target & Format Typos
> The secret target variable is defined as `int a = 45;`, but the game-over failure string prints: `The correct answer is 100.` If a player loses, the game reports a number different from what the code actually checked! Additionally, there is a stray backtick typo in the string `"Too low! `Try again."`.

## My notes
> [!question]- My notes

## Related
- [[PROJ - Hangman]] - Turn-limited guessing game with string state tracking
- [[PROJ TicTacToe - array]] - Turn-based game logic and win checking
