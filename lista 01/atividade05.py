"""Dados três números inteiros, mostre-os em ordem crescente.
"""
a, b, c = [float(input("Digite o valor de a:")), float(input("Digite o valor de b:")),
           float(input("Digite o valor de c:"))]
lista = [a, b, c]
lista.sort()
print(lista)
