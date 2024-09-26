# N-Mens Morris Game ("Mice" Game) Implementation

## Introduction

This project provides a Python implementation of the **N-Mens Morris** game, also known as "Mice." This strategy board game involves placing and moving pieces to form mills (three in a row) and capture the opponent's pieces.

## Features

- **Minimax Algorithm**: Utilizes the Minimax algorithm with alpha-beta pruning for optimal move selection. This algorithm evaluates all possible moves and selects the best one based on the game's current state.
- **Heuristics**: Implements heuristic evaluations to assess the board state and guide the Minimax algorithm. These heuristics help in estimating the value of different board configurations.
- **Data Structures**:
  - **HashMap**: Used for quick lookups of board states and their evaluations.
  - **Graph**: Represents the game board as a graph to manage piece positions and connections.
  - **Lists**: Utilized for managing moves, board states, and other game-related data.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:marijazhiv/Nine-men-s-morris-game.git
    ```

2. Navigate to the project directory:

    ```bash
    cd n-mens-morris
    ```

3. Install any required dependencies (if applicable):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the N-Mens Morris game, use the main script. Replace `main_script.py` with the actual script name:

```bash
python main.py

