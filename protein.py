# -*- coding: utf-8 -*-


class proteIn:
    def __init__(self, length, proteın ):
        self.length = length
        self.proteın = proteın
        self.grıd = self.create_proteIn()
        
    def get_length(self):
        return self._length
    
    def get_proteın(self):
        return self._proteın
    
    def set_proteın(self, proteın):
            self._proteın = proteın
    def create_proteIn(self):
        grıd= []
        ycord=0
        for ıdx in range(0,len(self.proteın)):
            grıd.append((self.proteın[ıdx], (ıdx, ycord)))
        return grıd
    
    def dısplayProteın(self):
        for item in self.grıd:
            print(item)
    
    def get_protein_tuples(self):
        return self.grıd
    def set_protein_tuples(self, new_grid):
        self.grıd = new_grid
 