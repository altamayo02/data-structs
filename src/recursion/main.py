import copy

from diagnostic import *
from recursion.recursion.recursion import *
import backtracking.maze as maze
import backtracking.chess_horse as chess_horse
import src.root3.root3 as root3
import backtracking.skippers as skippers

# 0.
print("DIAGNÓSTICO\n")

sumar_enteros(1, 2)

print(f'La suma de los enteros es: {sumar_enteros(5, 10)}\n')
print(f'El número {"no" if not es_primo(16) else ""} es primo.\n')

imprimir_pares(10)
imprimir_impares(10)

print(f'{sumar_elementos(list(range(1, 11)))}\n')

# 1.
print("RECURSIÓN\n")

print(suma([1, 2, 3, 4, 5]))
print(ocurrencias(14345, 4))
print(f'1627384950 invertido es {invertir(1627384950)}')
print(f'1230 invertido es {invertir(1230)}')
print(f'108509 invertido es {invertir(108509)}')
print(f'1627384950 tiene {cant_pares(1627384950)} pares')
print(f'1230 tiene {cant_pares(1230)} pares')
print(f'108509 tiene {cant_pares(108509)} pares')
print(menor([5, 2, 7, 4, 3, 1]))
print(mcd(36, 78))
print(suma([1, 2, 3, 4, 5, 4, 1, 3]))
print(cuadrado(12))
print(fibonacci(12))
print(binario(127))
print(invertir("desmadre"))
print(primera_ocurrencia([1, 2, 3, 4, 5, 4, 1, 3], 3))
print(ultima_ocurrencia([1, 2, 3, 4, 5, 4, 1, 3], 4))
print(mas_frecuente_letra(
	["a", "e", "i", "o", "u"],
	"esternocleidomastoideo"
))

# Classwork - Intro to backtracking
print("Trabajo de clase - Backtracking\n")
maze.backtrack(maze.maze)
print()
chess_horse.backtrack(chess_horse.table)
print()

# 2.
print("BACKTRACKING\n")