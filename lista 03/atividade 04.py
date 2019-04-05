""" Faça um programa que pergunta o dia e mês corrente e mostra o dia anterior.
Considere apenas datas entre 15/01 e 15/12.
Ex: dia: 01
 mês: 08
o programa deve responder 31/07."""

dia, mes = int(input("Digite um dia:")), int(input("Digite um mês:"))

if dia < 1 or dia > 31:  # caso o dia seja menor que 1 ou maior que 31 irá finalizar.
    print("Digite um dia valido")
    exit(0)
elif mes < 1 or mes > 12:  # caso o mês seja menor que 1 ou maior que 12 irá finalizar.
    print("Digite um mês valido")
    exit(0)

if (dia < 15 and mes == 1) or (dia > 15 and mes == 12):  # caso a data seja menor que 15/01 ou maior que 15/12 irá finalizar.
    print("O sistema ainda não suporta esta data!")
    exit(0)

if dia == 1:  # se o dia for igual a 1 então irá retornar o mês anterior.
    mes -= 1
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:  # caso o resultado do mês seja de 31 dias irá retornar 31
        dia = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:  # caso o resultado do mês seja 30 irá retornar 30.
        dia = 30
    else:  # se não for nenhum será fevereiro com 28 dias!
        dia = 28
else:  # se não for nenhuma anterior irá tirar 1 dia.
    dia -= 1
# irá imprimir o dia e mes formatado para mostrar 0 antes em numeros menores que 10
if dia < 10 and mes < 10:
    print("%02d/%02d" % (dia, mes))
elif dia > 10 and mes < 10:
    print(dia, "%02d" % (mes,), sep='/')
elif dia < 10 and mes > 10:
    print("%02d" % (dia,), mes, sep='/')
else:
    print(dia, mes, sep='/')

