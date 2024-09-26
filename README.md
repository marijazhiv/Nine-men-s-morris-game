N-Mens Morris Game ("Mice" Game) Implementation
Introduction
This project provides a Python implementation of the N-Mens Morris game, also known as "Mice." This strategy board game involves placing and moving pieces to form mills (three in a row) and capture the opponent's pieces.

Features
Minimax Algorithm: Utilizes the Minimax algorithm with alpha-beta pruning for optimal move selection. This algorithm evaluates all possible moves and selects the best one based on the game's current state.
Heuristics: Implements heuristic evaluations to assess the board state and guide the Minimax algorithm. These heuristics help in estimating the value of different board configurations.
Data Structures:
HashMap: Used for quick lookups of board states and their evaluations.
Graph: Represents the game board as a graph to manage piece positions and connections.
Lists: Utilized for managing moves, board states, and other game-related data.
Prerequisites
Python 3.x
