# -*- coding: utf-8 -*-



def energy_function(protein):

    energy = 0.0
    grid = protein.get_protein_tuples()  # Get residues and their positions

    for idx, (current_residue, (current_x, current_y)) in enumerate(grid):
        
        for next_residue, (next_x, next_y) in grid[idx + 1:]:
           
            if current_residue == 'H' and next_residue == 'H':
                # Horizontal adjacency (same row, neighboring columns)
                if current_y == next_y and abs(current_x - next_x) == 1:
                    energy -= 1
                # Vertical adjacency (same column, neighboring rows)
                elif current_x == next_x and abs(current_y - next_y) == 1:
                    energy -= 1

    return energy
