# TP1 – Métodos de Búsqueda

Implementation of search algorithms for the Multi-Agent Grid World problem.

## About the Project

The project implements a turn-based Multi-Agent Grid World. Each agent has its own start position and goal position, and only one agent moves at a time.

After an agent makes a valid move, the turn passes to the next agent. Agents cannot move into walls or positions occupied by another agent.

The goal is for all agents to reach their own goal positions and to compare the different search algorithms.
## Project Structure

- `main.py` – Runs the search algorithms and prints the results.
- `grid_world.py` – Defines the Grid World, valid movements, state transitions and goal conditions.
- `boards.py` – Contains the board configurations, start positions and goal positions.
- `search.py` – Contains the implementations of BFS, DFS, Greedy and A*.
- `heuristics.py` – Contains the heuristics used by the informed search methods.
- `game_visual.py` – Visualizes the solution paths using pygame.
- `tests/` – Contains tests for the Grid World and search algorithms.

## Requirements

- Python 3.12
- pygame

## Installation

Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install pygame
```

## Running the Program

Run the search engine with:

```bash
python main.py
```

The program reports:

- Success/failure
- Turn cost
- Movement cost per agent
- Total movement cost
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
- Weighted Manhattan distance (non-admissible)

For multiple agents, the heuristic is the sum of the distance from each agent to its goal.

## Visualization

The solution paths can be visualized using pygame.

[Add final instructions when the visualization is finished.]

## Analysis

The search algorithms are compared based on solution cost, expanded nodes, frontier nodes and processing time.

[Add final instructions when the analysis is finished.]