"""Em tempos de reforma da previdência, é fundamental ser previdente. Uma
estratégia é aplicar um capital inicial c e todo mês fazer um novo depósito d que
em conjunto (capital inicial e depósitos) renderão a uma taxa de juros mensal i.
Após n meses, o saldo da conta será dado por:
Saldo = c . (1 + i/100)n
 + d . ((1 + i/100)n
 – (1 + i/100)) / (i/100)
Faça um programa que calcule o saldo, dados os quatro parâmetros. Teste várias
situações, por exemplo: para uma aplicação inicial de 1000 e aporte mensal de 500,
com taxa de 2%, depois de quantos anos o investidor terá 100000?"""

c = int(input("Digite o valor do Capital aplicado:"))
i = float(input("Digite o valor da taxa:"))
d = int(input("Digite o valor do depósito mensal:"))
l = float(input("Digite qual valor deseja chegar: "))

parar = False
n = 1
while not parar:
    saldo = c * (1 + i/100)**n + d * ((1 + i/100)**n - (1+i/100)) / (i/100)
    if saldo < l:
        n += 1
    else:
        parar = True

print("em", n, "meses você terá R$", l, sep=' ')
