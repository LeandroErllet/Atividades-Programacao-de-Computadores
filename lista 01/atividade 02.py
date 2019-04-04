"""Receba como entrada os coeficientes (inteiros) de uma equação de segundo
grau: a, b e c, e apresente as raízes reais. (fase2: observe que a não pode ser
zero. Verifique também se as raízes existem e se são iguais)."""

a, b, c = int(input("valor de a")), int(input("valor de b")), int(input("valor de c"))
parar = False  # variável para gerenciar laço do programa

while not parar:  # enquanto parar for igual a False o programa ficará repetindo.
    if a == 0:
        print("a não pode ser zero!")
        a = int(input("valor de a: "))
    delta = b ** 2 - 4 * a * c
    print("Delta =", delta, sep=' ')
    if delta < 0:
        print("a equação não possui resultados reais")
        a, b, c = int(input("valor de a: ")), int(input("valor de b: ")), int(input("valor de c: "))
    if delta == 0:
        print("a equação possui apenas um resultado real ou possui dois resultados iguais (essas duas afirmações são "
              "equivalentes)")
    if delta > 0:
        print("a equação possui dois resultados distintos reais")
    raizdelta = delta ** (1 / 2)
    x1 = (- b + raizdelta) / (2 * a)
    x2 = (- b - raizdelta) / (2 * a)

    print("X' =", int(x1), "x'' =", int(x2), sep=' ')
    parar = True
if a * (x1 ** (1/2)) + b * x1 + c == 0:
    print("logo x =", int(x1), sep=' ')
elif a * (x2 ** (1/2)) + b * x2 + c == 0:
    print("logo x =", int(x2), sep=' ')
