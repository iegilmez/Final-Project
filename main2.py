# -*- coding: utf-8 -*-




from protein import proteIn
from mc_remc import mc_search
from visualizer import visualize_protein
from energy import energy_function

def main():
    
    sequence = "HPHHPPPPHPH"
    protein_length = len(sequence) 

  
    protein = proteIn(protein_length, sequence)

  
    num_mc_steps = 5  
    temperature = 100  
    print(f"Initial energy: {energy_function(protein)}")

   
    final_protein = mc_search(num_mc_steps, protein, temperature, protein_length)

    print(f"Final energy: {energy_function(final_protein)}")
    visualize_protein(final_protein)

if __name__ == "__main__":
    main()
    
    
