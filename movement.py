# -*- coding: utf-8 -*-

import random


def pull_move(protein_grid, i):
    #coordinates of residues i-1, i, and i+1
    x_i, y_i = protein_grid[i][1]
    x_i_plus_1, y_i_plus_1 = protein_grid[i + 1][1]

    
    if abs(x_i - x_i_plus_1) + abs(y_i - y_i_plus_1) != 1:
        # If residues are not adjacent in x or y, it's a bond break, no pull move ıs allowed
        return protein_grid

    #possible pull move positions 
    L = (x_i + 1, y_i)  # bend in x direction
    C = (x_i - 1, y_i)  # bend in x direction
    U = (x_i, y_i + 1)  # bend in y direction
    D = (x_i, y_i - 1)  # bend in y direction

    # Checkıng if adjacent positions are unoccupied
    available_positions = [L, C, U, D]
    for new_pos in available_positions:
        # Checkıng if the position is empty and not colliding with another residue
        if not any(pos == new_pos for _, pos in protein_grid):
            # Movıng residue i to the new position
            protein_grid[i] = (protein_grid[i][0], new_pos)
            return protein_grid  # Return modified grid

    
    return protein_grid

def crankshaft_move(protein_grid, i):
  

    #coordinates
    x_i_minus_1, y_i_minus_1 = protein_grid[i - 1][1]
    x_i, y_i = protein_grid[i][1]
    x_i_plus_1, y_i_plus_1 = protein_grid[i + 1][1]
    x_i_plus_2, y_i_plus_2 = protein_grid[i + 2][1]

    # Checking if the residues form a U-bend shape
    if not (
        (x_i_minus_1 == x_i and y_i == y_i_plus_1 and x_i_plus_1 == x_i_plus_2)  # Vertical U-bend
        or (y_i_minus_1 == y_i and x_i == x_i_plus_1 and y_i_plus_1 == y_i_plus_2)  # Horizontal U-bend
    ):
        # Not a U-bend shape 
        return protein_grid

    #new positions for residues i and i+1
    if x_i_minus_1 == x_i:  # Vertical U-bend
        new_i = (x_i_plus_1, y_i_minus_1)  # Rotate i around the bend
        new_i_plus_1 = (x_i_minus_1, y_i_plus_1)  # Rotate i+1 around the bend
    else:  # Horizontal U-bend
        new_i = (x_i_minus_1, y_i_plus_1)  # Rotate i around the bend
        new_i_plus_1 = (x_i_plus_1, y_i_minus_1)  # Rotate i+1 around the bend

    # Ensure new positions are valid (no overlap)
    if not any(pos == new_i or pos == new_i_plus_1 for _, pos in protein_grid):
        # Perform crankshaft move
        protein_grid[i] = (protein_grid[i][0], new_i)
        protein_grid[i + 1] = (protein_grid[i + 1][0], new_i_plus_1)
        return protein_grid

    # Return unchanged grid if move is invalid
    return protein_grid



def corner_move(protein_grid, i):
 
    x_i_minus_1, y_i_minus_1 = protein_grid[i - 1][1]
    x_i, y_i = protein_grid[i][1]
    x_i_plus_1, y_i_plus_1 = protein_grid[i + 1][1]
    
    # 4 possible adjacent positions
    possible_moves = [(x_i - 1, y_i-1), (x_i + 1, y_i+1), (x_i+1, y_i - 1), (x_i-1, y_i + 1)]
    
    #  no bond breakage
    for move in possible_moves:
        if move != (x_i_minus_1, y_i_minus_1) and move != (x_i_plus_1, y_i_plus_1):
            # Ensure the position is unoccupied
            if not any(pos == move for _, pos in protein_grid):
                # Make sure no bond is broken by the move 
                distance = abs(move[0] - x_i) + abs(move[1] - y_i)
                if distance == 1:  # Valid move
                    protein_grid[i] = (protein_grid[i][0], move)
                    return protein_grid  # Return modified
    return protein_grid  # Return the original grid if no valid move is found



def modify_conformation(protein_obj):
        move_type = random.choice(["corner", "crankshaft", "pull"])
        
        
        grid = protein_obj.get_protein_tuples()
        
       
        if move_type == "corner":
            new_grid = corner_move(grid, random.randint(1, len(grid) - 2))
        elif move_type == "crankshaft":
            new_grid = crankshaft_move(grid, random.randint(1, len(grid) - 3))
        elif move_type == "pull":
            new_grid = pull_move(grid, random.randint(1, len(grid) - 2))
        
       
        protein_obj.grıd = new_grid
        return protein_obj
