# -*- coding: utf-8 -*-


import random
import math
from energy import energy_function
from movement import modify_conformation

k = 0.001987  # kcal/mol·K

def mc_search(o, current_conformation,Temp, n):
    for i in range(o):
        new_conformation = current_conformation
        
        k = random.randint(1, n-1)
        modified_conformation = modify_conformation(new_conformation)
        delta_E = energy_function(modified_conformation) - energy_function(current_conformation)
        
        if delta_E < 0:  
            current_conformation = modified_conformation
        else:
            q = random.uniform(0, 1)  
            if q > math.exp(-1*delta_E/(k*Temp)):
                current_conformation = modified_conformation
        
    return current_conformation

def swap_labels(replica1, replica2):
    
    temp = replica1.get_protein_tuples()
    replica1.set_protein_tuples(replica2.get_protein_tuples())
    replica2.set_protein_tuples(temp)


def remc_simulation(current_states, E_star, o, temp,n):
    E_prime = 5  
    offset = 0
    M = len(current_states)  

    while E_prime > E_star:
        for i in range(M):
       
            current_states[i] = mc_search(o, current_states[i], temp,n)
           
            current_energy = energy_function(current_states[i])
            if current_energy < E_prime:
                E_prime = current_energy

        i = offset
        while i + 1 < M:
            j = i + 1
            delta_E = energy_function(current_states[i]) - energy_function(current_states[j])
            if delta_E <= 0:
           
                swap_labels(current_states[i], current_states[j])
            else:
             
                q = random.uniform(0, 1)
                if q < math.exp(-delta_E / (k*temp)): 
                    swap_labels(current_states[i], current_states[j])

            i += 2  

       
        offset = 1 - offset

    return current_states
