"""

Revisão sobre classes em python
"""

class Pessoa:
    """

    Classe Pessoa, que ...
    """


    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        """
        
        Este método faz a pessoa falar
        """

        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

    @property
    def pessoa_nome(self) -> str:
        return self.nome
    
    @pessoa_nome.setter
    def pessoa_nome(self, nome):
        self.nome = nome


romulo = Pessoa('Rômulo', '19')

romulo.falar()

print(romulo.pessoa_nome())

romulo.pessoa_nome = 'Rômulo Moraes'

print(romulo.pessoa_nome())