""" 

Módulo responsável por realizar ordenação dos vetores de cidades, ligadas a um vértice do mapa.
"""


import numpy as np


class Sort:
    def __init__(self, size: int):
        self.size = size
        self.last_item_index = -1
        self.array = np.empty(self.size, dtype=int)

    def show_array(self):

        """ 

        Método que lista todos os itens do array ordenado. 
        """

        if self.last_item_index == -1:
            print("Vetor vazio")
        else:
            for index in range(self.last_item_index + 1):
                print(f"{index} -> {self.array[index]}")

    def insert(self, value):
        """ 

        Método que faz a inserção ordenada no vetor (self.array). 
        """

        if self.last_item_index == (self.size - 1):
            print("Capacidade máxima atingida.")
            return
        
        position = 0
        for position in range(self.last_item_index + 1):
            if self.array[position] > value:
                break
            if position == self.last_item_index:
                position += 1
            
        last_item_index = self.last_item_index
        while last_item_index >= self.last_item_index:
            next_position = last_item_index + 1
            self.array[next_position] = self.array[last_item_index]
            last_item_index -= 1

        self.array[position] = value
        self.last_item_index += 1

    

vetor = Sort(6)

vetor.insert(10)
vetor.insert(2)
vetor.insert(11)

vetor.insert(0)
vetor.insert(6)
vetor.insert(1)

vetor.show_array()
