
""" 

Exemplo de Busca Linear
"""

def search(elements: list, element: int) -> int:

    """ 

    Função que recebe uma lista e um valor, para que 
    o algoritimo faça a busca. 
    """
    for index,value in enumerate(elements):
        # caso base - condição que faz o loop parar.
        if value == element:
            return index
        
    return "Elemento não encontrado."



elements = [3,4,1,6,14]
result = search(elements, 6)
print(result)
