# Number Scrabble Game

This is a Python console game where players take turns choosing numbers from 1 to 9 to make a set of three numbers that sum up to 15.

## Rules
The objective of the game is to select three numbers such that their sum equals 15. Players take turns choosing numbers, and the player who forms a valid set of three numbers first wins the game. If all numbers are chosen without any valid set forming, the game ends in a draw.

## How to Play
- You can choose to play against the computer or another player.
- Players take turns choosing numbers from 1 to 9 that haven't been chosen before.
- The game continues until a player forms a set of three numbers that sum to 15 or all numbers are chosen without a valid set.

## Repository Structure
The repository includes the following files:
- `Number Scrabble Game.py`: Python script containing the game code.
- `README.md`: This file, providing instructions and information about the game.

## Getting Started
To run the game:
1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Open a terminal or command prompt.
4. Navigate to the directory where the game script is located.
5. Run the script using the command `python number_scrabble_game.py`.
6. Follow the on-screen instructions to play the game.

### Example

```plaintext
Welcome in Number Scrabble Game.
The player that choose 3 numbers which the sum of it = 15 will win.

Please choose between:
1- Playing with computer
2- Playing with another player
1
please enter your name: Alice

Alice, please choose number from [1, 2, 3, 4, 5, 6, 7, 8, 9] and not choose from [] : 1
Computer choose 8
Alice, please choose number from [2, 3, 4, 5, 6, 7, 9] and not choose from [1, 8] : 2
Computer choose 9
Alice, please choose number from [3, 4, 5, 6, 7] and not choose from [1, 8, 2, 9] : 3
Alice is win
1's choices [1, 2, 3]
Computer's choices [8, 9]
Do you want to play again? (y/n):  no
```

## Acknowledgements
- Developed by Yassin Ali.
- Inspired by mathematical puzzles and number games.
