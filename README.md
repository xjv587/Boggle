### Efficient Boggle Solver with Recursive Search & Trie-based Dictionary
## Overview:
This project implements an optimized version of the classic Boggle game, integrating advanced data structures and recursive search techniques. The main objectives were to efficiently identify valid words on a dynamically generated Boggle board and compare human vs. computer performance.

## Key Features:
- Recursive Search Algorithms: Implemented two word-search strategies:
  - Board-Driven Search: Recursively explores words from each grid position while pruning invalid paths using prefix checks.
  - Dictionary-Driven Search: Iterates over a Trie-based dictionary to validate words on the board.
- Trie-Based Dictionary: Efficient word storage and lookup for large-scale word datasets (hundreds of thousands of words).
- User Interaction: Supports human gameplay with real-time word validation and scoring.
- Automated Computer Solver: Finds all possible words missed by the human player to demonstrate AI-driven search superiority.
- Scalability: Supports different board sizes (e.g., nxn), randomized board generation, and customizable game configurations.

## Technical Skills Demonstrated:
- Algorithms & Data Structures: Implemented recursive search, Trie data structure, and backtracking.
- Optimization & Pruning: Reduced search complexity using prefix-based early termination.
- Python Programming: Developed an object-oriented, modular architecture.
- Game AI: Built an automated solver outperforming human players.

## Applications:
- Demonstrates efficient search techniques applicable to NLP, text processing, and recommendation systems.
- Showcases AI-driven problem-solving for board games, puzzles, and optimization problems.
- Can be extended to dynamic word games, spell-checking, and auto-suggestion systems.
