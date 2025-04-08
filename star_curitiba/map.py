"""
Representação do mapa da Curitiba, junto com a heurística - distância
em linha reta do vértice até Curitiba.
"""

class Vertex:
    def __init__(self, label: str, target_distance: int):
        self.label = label
        self.target_distance = target_distance
        self.adjacent = []
        self.visited = False
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)
    
    def show_adjacent(self):
        for adjacent in self.adjacent:
            print(f"Adjacente: {adjacent.vertex.label} - {adjacent.cost} km")


class Adjacent:
    def __init__(self, vertex, cost):
        self.vertex = vertex
        self.cost = cost
        self.star_distance = self.cost + self.vertex.target_distance


class Curitiba:
    porto_uniao = Vertex("Porto União", 203)
    paulo_frontin = Vertex("Paulo Frontin", 172)
    canoinhas = Vertex("Canoinhas", 141)
    tres_barras = Vertex("Três Barras", 131)
    sao_mateus_sul = Vertex("São Mateus do Sul", 123)
    irati = Vertex("Irati", 139)
    curitiba = Vertex("curitiba", 0)
    palmeira = Vertex("Palmeira", 59)
    mafra = Vertex("Mafra", 94)
    campo_largo = Vertex("Campo largo", 27) # <-
    balsa_nova = Vertex("Pitesti", 41)
    lapa = Vertex("Giurgiu", 74)
    tijucas_sul = Vertex("Tijucas do Sul", 56)
    araucaria = Vertex("Araucaria", 23)
    sao_jose = Vertex("Sao José dos Pinhais", 13)
    contenda = Vertex("Contenda", 39)

    porto_uniao.add_adjacent(Adjacent (paulo_frontin, 46))
    porto_uniao.add_adjacent(Adjacent (sao_mateus_sul, 87))
    porto_uniao.add_adjacent(Adjacent (canoinhas, 78))

    paulo_frontin.add_adjacent(Adjacent (irati, 75))
    paulo_frontin.add_adjacent(Adjacent (porto_uniao, 46))

    canoinhas.add_adjacent(Adjacent (porto_uniao, 78))
    canoinhas.add_adjacent(Adjacent (tres_barras, 12))
    canoinhas.add_adjacent(Adjacent (mafra, 66))

    tres_barras.add_adjacent(Adjacent (canoinhas, 12))
    tres_barras.add_adjacent(Adjacent (sao_mateus_sul, 43))

    sao_mateus_sul.add_adjacent(Adjacent (porto_uniao, 87))
    sao_mateus_sul.add_adjacent(Adjacent (tres_barras, 43))
    sao_mateus_sul.add_adjacent(Adjacent (irati, 57))
    sao_mateus_sul.add_adjacent(Adjacent (palmeira, 77))
    sao_mateus_sul.add_adjacent(Adjacent (lapa, 60))

    irati.add_adjacent(Adjacent (paulo_frontin, 75))
    irati.add_adjacent(Adjacent (palmeira, 75))
    irati.add_adjacent(Adjacent (sao_mateus_sul, 57))

    curitiba.add_adjacent(Adjacent (campo_largo, 29))
    curitiba.add_adjacent(Adjacent (balsa_nova, 51))
    curitiba.add_adjacent(Adjacent (araucaria, 37))
    curitiba.add_adjacent(Adjacent (sao_jose, 15))

    palmeira.add_adjacent(Adjacent (irati, 75))
    palmeira.add_adjacent(Adjacent (campo_largo, 55))
    palmeira.add_adjacent(Adjacent (sao_mateus_sul, 77))

    mafra.add_adjacent(Adjacent (tijucas_sul, 99))
    mafra.add_adjacent(Adjacent (canoinhas, 66))
    mafra.add_adjacent(Adjacent (lapa, 57))

    campo_largo.add_adjacent(Adjacent (curitiba, 29))
    campo_largo.add_adjacent(Adjacent (balsa_nova, 22))
    campo_largo.add_adjacent(Adjacent (palmeira, 55))

    balsa_nova.add_adjacent(Adjacent (campo_largo, 22))
    balsa_nova.add_adjacent(Adjacent (contenda, 19))
    balsa_nova.add_adjacent(Adjacent (curitiba, 51))

    lapa.add_adjacent(Adjacent (mafra, 57)) #
    lapa.add_adjacent(Adjacent (contenda, 26))
    lapa.add_adjacent(Adjacent (sao_mateus_sul, 60))

    tijucas_sul.add_adjacent(Adjacent (sao_jose, 49))#
    tijucas_sul.add_adjacent(Adjacent (mafra, 99))
    
    araucaria.add_adjacent(Adjacent (curitiba, 37))
    araucaria.add_adjacent(Adjacent (contenda, 18))

    sao_jose.add_adjacent(Adjacent (curitiba, 15))
    sao_jose.add_adjacent(Adjacent (tijucas_sul, 49))

    contenda.add_adjacent(Adjacent (balsa_nova, 19))
    contenda.add_adjacent(Adjacent (lapa, 26))
    contenda.add_adjacent(Adjacent (araucaria, 18))