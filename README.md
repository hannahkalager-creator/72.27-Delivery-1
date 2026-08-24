# TP1 – Métodos de Búsqueda

Implementation of search algorithms for the Multi-Agent Grid World problem.

## About the Project

The project implements a turn-based Multi-Agent Grid World. Each agent has
its own start and goal position, and only one agent moves at a time.

The objective is to find a solution where all agents reach their respective
goals while comparing the performance of different search algorithms.

## Project Structure

- `main.py` – Runs the search algorithms and prints the results.
- `grid_world.py` – Defines the Multi-Agent Grid World and the possible state transitions.
- `boards.py` – Contains the board configurations, start positions and goal positions.
- `search.py` – Contains BFS, DFS, Greedy and A*.
- `heuristics.py` – Contains the heuristics used by the informed search methods.
- `game_visual.py` – Visualizes the solution using pygame.
- `tests/` – Contains tests for the Grid World and search algorithms.

## Requirements

- Python 3.12
- pygame

## Installation

Create and activate a virtual environment:

    python3.12 -m venv .venv
    source .venv/bin/activate

Install the required dependencies:

    pip install pygame

## Running the Program

Run the search engine with:

    python main.py

The program reports:

- Success/failure
- Solution cost
- Expanded nodes
- Frontier nodes
- Solution path
- Processing time

## Search Algorithms

The following search algorithms are implemented:

- BFS
- DFS
- Greedy
- A*

## Heuristics

The informed search methods use:

- Manhattan distance
- Euclidean distance
- Weighted Manhattan distance

## Visualization

[Add final instructions when the visualization is finished.]

## Analysis

[Add final instructions when the analysis is finished.]