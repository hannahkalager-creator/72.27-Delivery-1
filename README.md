# TP1 – Métodos de Búsqueda

Implementation and comparison of search algorithms for a Multi-Agent Grid World.

## About the Project

The project implements a turn-based Multi-Agent Grid World. Each agent has its own start and goal position, and only one agent moves at a time.

After an agent makes a valid move, the turn passes to the next agent. Agents cannot move outside the board, through walls, or into a position occupied by another agent.

If an agent has already reached its goal, it stays in place and passes the turn to the next agent.

The objective is to find a solution where all agents reach their respective goals and compare the performance of different search algorithms.

The implementation supports a variable number of agents. Different configurations with 2, 3 and 4 agents are included in `boards.py` and used in the performance analysis.

## Project Structure

- `main.py` – Runs the search algorithms, prints the results and starts the visualization.
- `grid_world.py` – Defines the Multi-Agent Grid World, valid movements, state transitions and goal conditions.
- `boards.py` – Contains the board configurations, start positions and goal positions.
- `search.py` – Contains BFS, DFS, Greedy and A*.
- `heuristics.py` – Contains the heuristics used by the informed search methods.
- `cost.py` – Calculates the movement cost for each agent.
- `game_visual.py` – Visualizes the solution paths using pygame.
- `analysis.ipynb` – Compares the performance of the different search algorithms.
- `tests/` – Contains tests for the search algorithms and multi-agent behavior.

## Requirements

- Python 3.12
- pygame
- numpy
- matplotlib
- Jupyter Notebook

## Installation

Create and activate a virtual environment:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install pygame numpy matplotlib notebook
```

## Running the Program

Run the program with:

```bash
python main.py
```

The program runs the different search algorithms and reports:

- Solution path
- Turn cost
- Movement cost per agent
- Total movement cost
- Expanded nodes
- Frontier nodes
- Processing time
- Success/failure

The solution path for each algorithm is also visualized using pygame.

Close the pygame window to continue to the next search algorithm.

## Search Algorithms

The following search algorithms are implemented:

- BFS
- DFS
- Greedy
- A*

BFS and DFS are uninformed search methods.

Greedy and A* use heuristics to decide which states to explore.

## Heuristics

The informed search methods use:

- Manhattan distance
- Euclidean distance
- Weighted Manhattan distance

For a multi-agent state, the heuristic cost is calculated as the sum of the estimated distance from each agent to its own goal.

Manhattan and Euclidean distance are admissible for this problem. Weighted Manhattan is non-admissible because it can overestimate the remaining cost.

## State Representation

A state contains the positions of all agents and the index of the agent whose turn it is:

```text
((agent_0_position, agent_1_position, ...), current_agent)
```

For example:

```text
(((0, 0), (4, 0)), 0)
```

means that Agent 0 is at `(0, 0)`, Agent 1 is at `(4, 0)`, and it is Agent 0's turn.

After an agent moves, the turn passes to the next agent.

## Cost

Each state transition has a turn cost of 1.

The program also calculates the movement cost for each agent by counting how many times its position changes in the solution path.

The reported costs are:

- Turn cost – number of state transitions in the solution.
- Movement cost per agent – number of actual moves made by each agent.
- Total movement cost – sum of the movement costs of all agents.

## Visualization

The solution paths are visualized using pygame when running:

```bash
python main.py
```

The program uses the multi-agent configuration defined by `multi_board`, `multi_start` and `multi_goal` in `boards.py`.

Each agent is represented by a different color. The visualization shows the grid and the path followed by each agent from its start position to its goal.

A separate visualization is shown for each search method. Close the pygame window to continue to the next search method.

## Analysis

The performance analysis is implemented in:

```text
analysis.ipynb
```

Start Jupyter Notebook with:

```bash
jupyter notebook
```

Then open `analysis.ipynb` and run the cells in order.

The analysis runs the search algorithms on Simple, Moderate and Hard boards. Each board is tested with configurations of 2, 3 and 4 agents to compare how the algorithms perform as the problem becomes more complex.

The following metrics are compared:

- Solution cost
- Expanded nodes
- Frontier nodes
- Processing time
- Peak memory usage

The notebook generates result tables, bar charts and line charts to compare the algorithms and show how their performance changes with the board difficulty and number of agents.

The analysis compares:

- BFS
- DFS
- Greedy with Manhattan distance
- Greedy with Euclidean distance
- A* with Manhattan distance
- A* with Euclidean distance

A timeout is used for searches that take too long to complete.
## Running the Tests

The project includes tests for the search algorithms, heuristics and multi-agent behavior.

Run the tests with:

```bash
python -m unittest discover tests
```

The tests check examples such as:

- Multi-agent heuristic calculation
- A* solution cost compared with BFS
- Admissibility of Manhattan and Euclidean heuristics
- Greedy finding a valid solution
- Weighted Manhattan expansion behavior
- A multi-agent case where no solution exists