""" 

Exemplo de Busca Binária, utilizando o conceito
de 'Divisão e Conquista'.
"""


def search(elements: list, element: int, end: int, start: int=0):
    """ 
    
    Função que recebe uma lista, valor, indice do final da lista e indice do inicio da lista, para que 
    o algoritimo faça a busca. 
    """

    while start <= end:
        mid = start + (end - start) // 2

        #caso base
        if(elements[mid]) == element:
            return mid
        elif elements[mid] < element:
            start = mid + 1
        else:
            end = mid - 1
            
    return "Elemento não encontrado."


# Lista ordenada
elements = [4,6,8,9,13,14,21,40,43,45,78,98,103,152] 
element = 13

result = search(elements, element, len(elements) - 1)

print(f"O índice do elemento procurado é: {result}")