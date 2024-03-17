import copy


def cant_digitos(n: int) -> int:
	'''
	Cuenta la cantidad de dígitos en un número natural N.
	'''
	if n < 10:
		return 1
	else:
		return 1 + cant_digitos(n // 10)

def ocurrencias(n: int, d: int) -> int:
	'''
	Cuenta las ocurrencias de un dígito D en un número natural N.
	'''
	if n < 10:
		return 1 if n == d else 0
	elif n % 10 == d:
		return 1 + ocurrencias(n // 10, d)
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

def cuadrado(n: int):
	'''
	Calcula el cuadrado de un número N entero positivo de manera recursiva,
	como la sumatoria de los primeros N números impares.
	'''
	if n < 1:
		return 0
	else:
		return (2 * n - 1) + cuadrado(n - 1)

def fibonacci(n: int):
	'''
	Calcula el n-ésimo término de la sucesión de Fibonacci.
	'''
	if n > 0:
		if n in [1, 2]:
			return 1
		else:
			return fibonacci(n - 1) + fibonacci(n - 2)
	else:
		return 0

def binario(n: int):
	'''
	Retorna la representación binaria de un número decimal como entero.
	'''
	if n < 2:
		return n
	else:
		return binario(n // 2) * 10 + (n % 2)

def invertir(s: str):
	'''
	Invierte una cadena de texto recursivamente.
	'''
	if len(s) == 1:
		return s
	else:
		return s[-1] + invertir(s[:-1])

def primera_ocurrencia(vector: list, n: int):
	'''
	Encuentra la primera posición en la que aparece un valor dado en una lista de enteros.
	'''
	if vector[0] == n:
		return 0
	else:
		return primera_ocurrencia(vector[1:], n) + 1

def ultima_ocurrencia(vector: list, n: int):
	'''
	Encuentra la última posición en la que aparece un valor dado en una lista de enteros.
	'''
	if vector[-1] == n:
		return len(vector) - 1
	else:
		return ultima_ocurrencia(vector[:-1], n)
	
def _mas_frecuente_letra(letras: list[str], s: str, sln: list = []):
	if len(s) == 0:
		return letras[sln.index(
			mayor(copy.deepcopy(sln))
		)]
	else:
		if s[0] in letras:
			sln[letras.index(s[0])] += 1
		return _mas_frecuente_letra(letras, s[1:], sln)

def mas_frecuente_letra(letras: list[str], s: str):
	'''
	Encuentra la letra con mayor número de instancias en una cadena de texto.
	'''
	return _mas_frecuente_letra(letras, s, len(letras) * [0])

def mayor(lista: list) -> int:
	'''
	Encuentra el elemento mayor dentro de una lista
	'''
	if len(lista) == 1:
		return lista[0]
	else:
		if lista[1] > lista[0]:
			del lista[0]
		else:
			del lista[1]
		return mayor(lista)