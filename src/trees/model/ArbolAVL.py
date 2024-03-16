# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:07:24 2024

@author: JVelez
"""
class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.altura = 1
        self.izquierda = None
        self.derecha = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if not nodo:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotacion_simple_derecha(self, nodo):
        nueva_raiz = nodo.izquierda
        nodo.izquierda = nueva_raiz.derecha
        nueva_raiz.derecha = nodo
        nodo.altura = max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1
        nueva_raiz.altura = max(self.altura(nueva_raiz.izquierda), self.altura(nueva_raiz.derecha)) + 1
        return nueva_raiz

    def rotacion_simple_izquierda(self, nodo):
        nueva_raiz = nodo.derecha 
        nodo.derecha = nueva_raiz.izquierda
        nueva_raiz.izquierda = nodo
        nodo.altura = max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1
        nueva_raiz.altura = max(self.altura(nueva_raiz.izquierda), self.altura(nueva_raiz.derecha)) + 1
        return nueva_raiz

    def insertar(self, raiz, valor):
        if not raiz:
            return NodoAVL(valor)
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)

        raiz.altura = max(self.altura(raiz.izquierda), self.altura(raiz.derecha)) + 1
        balance = self.balance(raiz)

        if balance > 1:
            if valor < raiz.izquierda.valor:
                return self.rotacion_simple_derecha(raiz)
            else:
                raiz.izquierda = self.rotacion_simple_izquierda(raiz.izquierda)
                return self.rotacion_simple_derecha(raiz)
        if balance < -1:
            if valor > raiz.derecha.valor:
                return self.rotacion_simple_izquierda(raiz)
            else:
                raiz.derecha = self.rotacion_simple_derecha(raiz.derecha)
                return self.rotacion_simple_izquierda(raiz)
        return raiz

    def insertar_valor(self, valor):
        self.raiz = self.insertar(self.raiz, valor)
    
    def pre_order(self,raiz):
        if raiz is not None:
            print(raiz.valor,end=" ")
            self.pre_order(raiz.izquierda)
            self.pre_order(raiz.derecha)

# Ejemplo de uso
arbol = ArbolAVL() 
arbol.insertar_valor(10)
arbol.insertar_valor(20)
arbol.insertar_valor(5)
arbol.insertar_valor(15)
arbol.insertar_valor(18)
arbol.insertar_valor(25)
arbol.pre_order(arbol.raiz)