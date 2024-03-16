# Apartado 1: Operaciones binarias
def sumar_enteros(num1, num2):
    return num1 + num2

def restar_enteros(num1, num2):
    return num1 - num2

def multiplicar_enteros(num1, num2):
    return num1 * num2

def division_entera(num1, num2):
    # Integer division! //
    return num1 // num2

def residuo_division(num1, num2):
    return num1 % num2


# Apartado 2: Condicionales
def verificar_con_cero(n):
    if n > 0:
        return 'El número es positivo'
    elif n < 0:
        return 'El número es negativo'
    else:
        return 'El número es cero'

def es_par(n):
    if (n % 2) == 0:
        return True
    return False

def es_bisiesto(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def numero_mayor(num1, num2, num3):
    mayor = num1
    if num2 > mayor: mayor = num2
    elif num3 > mayor: mayor = num3
    return mayor

def es_primo(n):
    return all(n % i != 0 for i in range(2, (n+1) // 2))

# 'Cuz, why not
def es_perfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n


# Apartado 3: Ciclos
def imprimir_naturales(tope):
    for i in range(1, tope + 1):
        print(i)
    print()

def sumar_naturales(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def imprimir_pares(n):
    for i in range(1, n + 1):
        print(2 * i)
    print()

def imprimir_impares(n):
    i = 1
    while i <= n:
        print(2 * i - 1)
        i += 1
    print()

def factorial(n):
    fact = 1
    i = 2
    while i <= n:
        fact *= i
        i += 1

    return fact


# Apartado 4: Vectores
def sumar_elementos(vect):
    suma = 0
    for elem in vect:
        suma += elem
    return suma

def contiene(vect, n):
    for elem in vect:
        if n == elem:
            return True
    return False
    #return any(n == elem for elem in vect)
    #return n in vect

def ordenar_elementos(vect):
    for i in range(len(vect) - 1):
        for j in range(1, len(vect)):
            if vect[i] > vect[j]:
                vect[i], vect[j] = vect[j], vect[i]
    return vect
    #return sorted(vect)

def promedio_elementos(vect):
    return sumar_elementos(vect) / len(vect)

def sumar_matrices(mat1, mat2):
    suma = []
    for row in range(len(mat1)):
        suma.append([])
        for col in range(len(mat1[0])):
            suma[row].append(mat1[row][col] + mat2[row][col])
    return suma

def restar(mat1, mat2):
    return sumar_matrices(mat1, -mat2)

def multiplicar_escalar(mat, e):
    res = []
    for i in range(len(mat)):
        res.append([])
        for j in range(len(mat[0])):
            res[i].append(mat[i][j] * e)
    return res

def transpuesta(mat):
    res = []
    for i in range(len(mat[0])):
        res.append([])
        for j in range(len(mat)):
            res[i].append(mat[j][i])
    return res

def es_simetrica(mat):
    return mat == transpuesta(mat)