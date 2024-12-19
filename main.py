# -*- coding: utf-8 -*-

# main.py


import random
import math
import matplotlib.pyplot as plt
from protein import proteIn
from mc_remc import remc_simulation
from visualizer import visualize_protein
from energy import energy_function

k = 0.001987  # kcal/mol·K (Boltzmann constant)

def main():
    sequences = ["HPHHPPPPHPH", "HPHPPHPPHPH", "PPHPHPHPPHH", "HPPHHPHPPHP"]
    replicas = [proteIn(len(seq), seq) for seq in sequences]

    E_star = -1
    num_mc_steps = 5
    temperature = 100 
    protein_length = len(sequences[0])
    num_replicas = len(replicas)

    final_states = remc_simulation(replicas, E_star, num_mc_steps, temperature, protein_length)

    for i, replica in enumerate(final_states):
        print(f"\nReplica {i + 1}:")
        print("Final energy:", energy_function(replica))
        visualize_protein(replica)

if __name__ == "__main__":
    main()
