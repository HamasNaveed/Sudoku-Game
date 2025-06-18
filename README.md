# Sudoku-Game
A Pygame-based Sudoku game with dynamic puzzle fetching, difficulty levels (Easy, Medium, Hard, Expert), and a lives system. Built by Hamas Naveed.

Sudoku Game
🧩 A dynamic Sudoku game built with Python and Pygame, featuring puzzles fetched from an API, four difficulty levels (Easy, Medium, Hard, Expert), and a lives-based challenge system. Created by Hamas Naveed.
Table of Contents

Features
Installation
How to Play
Technologies Used

Features

Dynamic Puzzle Fetching: Pulls new 9x9 Sudoku puzzles from an API with four difficulty levels.
Interactive Menu: Choose difficulty (1: Easy, 2: Medium, 3: Hard, 4: Expert) or view instructions.
Lives System: Start with 3 lives; invalid moves reduce lives, ending the game at 0.
Responsive Controls: Click to select cells and use the keyboard to input numbers (1–9).
Instructions Screen: Clear rules and gameplay guide accessible via the menu.
Visual Feedback: Highlights selected cells and displays invalid move messages.


Installation
To run the game locally:


Install dependencies:Ensure you have Python 3.6+ installed. Install Pygame and Requests:pip install pygame requests


Run the game:python Sudoku.py



How to Play

From the main menu, press:
1 for Easy, 2 for Medium, 3 for Hard, or 4 for Expert to start a game.
I to view instructions.


In the game:
Click a cell to select it (highlighted in gray).
Enter a number (1–9) using your keyboard.
Numbers are valid only if they match the puzzle’s solution (fetched from the API).
Invalid moves reduce your lives (starting at 3). The game ends when lives reach 0.


From the instructions screen, press B to return to the menu.

Technologies Used

Python: Core programming language.
Pygame: Handles the game interface, grid rendering, and user interactions.
Requests: Fetches Sudoku puzzles from an external API.
API: Uses sudoku-api.vercel.app for puzzle generation.


✨ Challenge your logic skills with this interactive Sudoku game! Feedback is appreciated. 🎮
