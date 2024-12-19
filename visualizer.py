# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

def visualize_protein(protein_obj):
   
    protein_grid = protein_obj.get_protein_tuples()
    
    
    amino_acids = [item[0] for item in protein_grid]
    coordinates = [item[1] for item in protein_grid]
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    
    
    colors = ["red" if aa == "H" else "blue" for aa in amino_acids]  
    
   
    plt.figure(figsize=(10, 5))
    
  
    plt.plot(x_coords, y_coords, color="gray", linestyle="--", linewidth=2, zorder=1)
    
   
    for i, (x, y, color) in enumerate(zip(x_coords, y_coords, colors)):
        plt.scatter(x, y, color=color, s=100, zorder=5, label=amino_acids[i] if i == 0 or amino_acids[i] != amino_acids[i-1] else "")
    
   
    for i, amino_acid in enumerate(amino_acids):
        plt.text(x_coords[i], y_coords[i] + 0.1, amino_acid, 
                 fontsize=12, ha='center', va='bottom', color="black")
    
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xticks(range(min(x_coords) - 1, max(x_coords) + 2))
    plt.yticks(range(min(y_coords) - 1, max(y_coords) + 2))  
    plt.gca().set_aspect("equal", adjustable="box")  
    plt.show()