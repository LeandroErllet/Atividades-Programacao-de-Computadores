import time
print("====================================================================")
print("            Bem-vindo ao Jogo do Triângulo 2.000 versão: 1.0 ")
print("            Por Leandro(20191014050014) e Josymar(20191014050011)")
print("====================================================================")
time.sleep(1)

num = int(input("Digite um número: "))
num1 = 1
num2 = 2
num3 = 3
mult = num1 * num2 * num3

while mult < num:
    num1 += 1
    num2 += 1
    num3 += 1
    mult = num1 * num2 * num3
    div = mult // num1
    div = mult // num2
    div = mult // num3

if num == mult:
    print(num, "É o triangulo de:", num1, ",", num2, "e", num3)
else:
    print("Esse número não tem triangulo.")
