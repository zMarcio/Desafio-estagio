"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverte_string(string: str):
    return string[::-1]

def inverte_no_dedo(string:str):
    aux = ""
    p = 1
    k = 0
    """ 
    0(k) + 1(p) = 1 | len(string) - 1 = 5
    1(k) + 1(p) = 2 | len(string) - 2 = 4
    2(k) + 1(p) = 3 | len(string) - 3 = 3
    
    """
    for i in range(len(string)):
        k += p
        temp = len(string) - k
        aux += string[temp]
        p = 1
        
    return aux

print(inverte_string("string"))
print(inverte_no_dedo("string"))
