from recursion.ws1 import *
from recursion.ws2 import *
import backtracking.maze as maze
import backtracking.chess_horse as chess_horse


#1.
print("Taller 1 - Diagnóstico\n")

sumar_enteros(1, 2)

print(f'La suma de los enteros es: {sumar_enteros(5, 10)}\n')
print(f'El número {"no" if not es_primo(16) else ""} es primo.\n')

imprimir_pares(10)
imprimir_impares(10)

print(f'{sumar_elementos(list(range(1, 11)))}\n')

#2.
print("Taller 2 - Recursión\n")

print(suma([1, 2, 3, 4, 5]))
print(ocurrencias(14345, 4))
print(f'1627384950 invertido es {invertir(1627384950)}')
print(f'1230 invertido es {invertir(1230)}')
print(f'108509 invertido es {invertir(108509)}')
print(f'1627384950 tiene {cant_pares(1627384950)} pares')
print(f'1230 tiene {cant_pares(1230)} pares')
print(f'108509 tiene {cant_pares(108509)} pares')
print(menor([5, 2, 7, 4, 3, 1]))

# Classwork - Intro to backtracking
print("Trabajo de clase - Backtracking\n")
maze.backtrack(maze.maze)
print()
chess_horse.backtrack(chess_horse.table)

# 3.
print("Taller 3 - Backtracking\n")
