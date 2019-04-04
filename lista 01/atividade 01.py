"""Dados o valor de uma conta em um restaurante (valor inteiro) e o valor do
pagamento, apresente o número mínimo de cédulas e moedas que deve ser
retornado como troco (fase2: mostre apenas as cédulas e moedas que devem ser
devolvidas no troco).
"""


notas = [100, 50, 20, 10, 5, 2, 1]  # uma lista com todas as notas.
moedas = [0.50, 0.25, 0.10, 0.05]  # uma lista com todas as moedas.
conta = float(input("quanto deu a conta?"))  # pergunta quanto deu a conta.
pago = float(input("quanto você deu?"))  # pergunta quanto o usuário deu para pagar.

parar = False  # variável para gerenciar laço do programa

while not parar:  # enquanto parar for igual a False o programa ficará repetindo.
    if pago < conta:  # caso a conta for menor do que o valor pago irá perguntar os valores novamente.
        print("Digite um valor que de para pagar a conta!")
        conta = float(input("quanto deu a conta?"))  # pergunta quanto deu a conta.
        pago = float(input("quanto você deu?"))  # pergunta quanto o usuário deu para pagar.
    troco = pago - conta  # o troco vai ser o resultado do valor pago menos a conta.
    print("o Troco vai ser de:", troco, sep=' R$')
    for nota in notas:  # irá fazer um laço com todas as notas.
        if nota <= troco:  # caso a nota seja menor ou igual ao troco irá executar.
            tempnotas = troco // nota  # as notas serão o resultado dadivisão inteira de troco pela nota.
            #  irá formatar o texto de acordo com o total de notas.
            if tempnotas > 1:
                print(int(tempnotas), "notas de", nota, "reais", sep=' ')
            else:
                if nota == 1:  # caso a nota seja de 1 real irá mudar o texto para moeda
                    print(int(tempnotas), "moeda de", nota, "real", sep=' ')
                else:
                    print(int(tempnotas), "nota de", nota, "reais", sep=' ')
            troco %= nota  # o troco vai ser o resto da divisão entre troco e nota.
    for moeda in moedas:  # irá fazer um laço com todas as moedas.
        if moeda <= troco:  # caso a moeda seja menor ou igual ao troco irá executar.
            tempmoeda = troco // moeda  # as moedas serão o resultado dadivisão inteira de troco pela moeda.
            #  irá formatar o texto de acordo com o total de moedas.
            if tempmoeda > 1:
                print(int(tempmoeda), "moedas de", int(moeda * 100), "centavos", sep=' ')
            else:
                print(int(tempmoeda), "moeda de", int(moeda * 100), "centavos", sep=' ')
            troco %= moeda  # o troco vai ser o resto da divisão entre troco e moeda.

    # caso o troco seja maior que 0 irá mostrar quantos centavos o usuário perdeu.
    if troco > 0:
        print("Você perdeu", int(round(troco * 100)), " centavos por falta de moedas de 1 centavo.")
    parar = True # mudou ovalor de parar para True para finalizar o programa.
