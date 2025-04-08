"""

Revisão de OO, relembrando injeção de dependências e estrutura de dados 'Grafo'.
"""

class State:
    """
    
    Classe que define estados de uma nação.
    """

    def __init__(self, state_name, size):
        self.state_name = state_name
        self.size = size

class Country:
    """
    
    Classe que define uma nação.
    """

    def __init__(self, country_name, flag):
        self.country_name = country_name
        self.flag = flag
        self.states = []

    def add_state(self, state: State):
        self.states.append(state)

    def list_states(self):
        for state in self.states:
            print(state.state_name)


class World_Map:
    """

    Classe que cria o mapa mundi.
    """

    brazil = Country("Brazil", "🇧🇷")
    south_africa = Country("South Africa", "🇿🇦")

    brazil.add_state(State("São paulo", 10))
    brazil.add_state(State("Rio de Janeiro", 8))
    brazil.add_state(State("Minas Gerais", 5))

world_map = World_Map()

print(world_map.brazil.flag)
print(world_map.brazil.list_states())