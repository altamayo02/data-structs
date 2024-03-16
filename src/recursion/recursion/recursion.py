def cant_digitos(n: int) -> int:
    '''
    Cuenta la cantidad de dígitos en un número natural N.
    '''
    if n < 10:
        return 1
    else:
        return cant_digitos(n // 10) + 1

def ocurrencias(n: int, d: int) -> int:
    '''
    Cuenta las ocurrencias de un dígito D en un número natural N.
    '''
    if n < 10:
        return 1 if n == d else 0
    elif n % 10 == d:
        return ocurrencias(n // 10, d) + 1
    else:
        return ocurrencias(n // 10, d)

def invertir(n: int, m: str = "") -> int:
    '''
    Invierte los dígitos de un número natural N
    '''
    if n < 10:
        return n
    else:
        return (n % 10) * (10 ** (cant_digitos(n) - 1)) + invertir(n // 10)
    """
        return f"{m}{n}"
    else:
        return invertir(n // 10, f"{m}{n % 10}")
    """
    
def cant_pares(n: int) -> int:
    '''
    Cuenta las ocurrencias de dígitos pares en un número natural N
    '''
    if n < 10:
        return 1 if n % 2 == 0 else 0
    else:
        if n % 2 == 0:
            return cant_pares(n // 10) + 1
        else:
            return cant_pares(n // 10)

def menor(lista: list) -> int:
    '''
    Encuentra el elemento menor dentro de una lista
    '''
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[1] < lista[0]:
            del lista[0]
        else:
            del lista[1]
        return menor(lista)
    
def mcd(a: int, b: int) -> int:
    '''
    Algoritmo de Euclides para calcular el MCD de dos números.
    '''
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
    
def suma(vector: list, res: int = 0) -> int:
    '''
    Suma los elementos de un vector de manera recursiva
    '''
    if len(vector) == 1:
        return res + vector[0]
    else:
        value = vector.pop()
        return suma(vector, res + value)