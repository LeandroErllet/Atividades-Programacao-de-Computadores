"""Faça um programa que recebe um número (n) e mostra uma sucessão de somas,
assim definidas: a soma de 0 até n; a soma de 1 até n-1; a soma de 2 até n-2 e
assim sucessivamente.
Ex: se n = 7
o programa deve mostrar (pode ser uma por linha):
28 21 14 7"""

n = int(input("Digite um número: "))  # pegar o valor de n e s
s = 0

for i in range(n + 1):  # para i no range de 0 ate n + 1
    s += i  # adciona mais 1 em S
print(s)  # mostrar s
while s > n:  # enquanto s for maior que n
    s -= n  # tirar 1 de s
    print(s)  # mostrar s
