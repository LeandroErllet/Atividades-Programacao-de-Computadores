"""A magia (ou pesadelo) dos juros compostos é que eles crescem que uma maneira
inimaginável. Sabendo que o montante acumulado para um capital c, a uma taxa
i (em porcentagem), por um tempo t é dado por:
Montante = c . ( 1 + i / 100) t
Faça um programa que aceite os três parâmetros citados e informe o montante
gerado pelo capital.
"""
c, n, i = float(input("Digite o valor do Capital:"))\
    , float(input("Digite o valor do tempo em meses:"))\
    , float(input("Digite o valor da taxa:"))

montante = c * (1 + (i / 100)) ** n
print("O montante é R$", round(montante), "reais", sep=' ')
