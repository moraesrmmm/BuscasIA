"""
Projeto1 - Revisão:
Converter números inteiros para Romanos.
"""

def int_to_roman(number: int) -> str:
    """

    Função que recebe um valor int e retorna o valor em romano, como string.
    """

    symbols: dict = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman = ""
    
    for symbol in sorted(symbols.keys(), reverse=True):
        while number >=  symbol:
            roman += symbols[symbol]
            number -= symbol
        
    return roman

number = int(input("Digite um valor inteiro: "))
roman = int_to_roman(number) 

print(roman)


