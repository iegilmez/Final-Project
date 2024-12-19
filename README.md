# Final Project
This project simulates the folding of proteins using Monte Carlo (MC) and Replica Exchange Monte Carlo (REMC) techniques.

## Project Overview
The main objective of this project is to simulate the folding process of proteins, study their conformations, and calculate energy levels. It employs:

- Monte Carlo (MC) search for exploring different conformations.
- Replica Exchange Monte Carlo (REMC) to improve convergence to the global minimum energy.

## Features
- **Protein class**: Represents a protein sequence and its conformation.
- **Energy calculation**: Calculates the energy of a protein conformation based on interactions.
- **Monte Carlo moves**: Implements corner, crankshaft, and pull moves.
- **Visualization**: Displays the protein structure using a 2D plot.
- **REMC simulation**: Optimizes protein folding by exchanging conformations between replicas.

## Key Functions

### 1. Protein Class (protein.py)
- **proteIn**: Represents a protein sequence and its grid.
- **Methods**:
  - `get_protein_tuples()`: Returns the grid of the protein.
  - `set_protein_tuples(grid)`: Updates the grid of the protein.

### 2. Energy Function (energy.py)
- `energy_function(protein)`: Calculates the energy of a given protein conformation based on hydrophobic ("H") interactions.

### 3. Monte Carlo Moves (movements.py)
- `corner_move(grid, i)`: Implements the corner move.
- `crankshaft_move(grid, i)`: Implements the crankshaft move.
- `pull_move(grid, i)`: Implements the pull move.

### 4. Monte Carlo Simulation (mc_remc.py)
- `mc_search(o, current_state, temp, n)`: Performs the Monte Carlo simulation.
- `remc_simulation(states, E_star, o, temp, n)`: Performs Replica Exchange Monte Carlo.

### 5. Visualization (visualizer.py)
- `visualize_protein(protein_obj)`: Plots the protein conformation.
