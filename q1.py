
import time
print("====================================================================")
print("            Bem-vindo ao Jogo do Robô 2.000 versão: 1.0 ")
print("            Por Leandro(20191014050014) e Josymar(20191014050011)")
print("====================================================================")
time.sleep(1)
pix, piy = int(input("Digite a posição inicial de X: ")),  int(input("Digite a posição inicial de Y: "))

print("----------------------------------------------------------")
print("Movimentos disponíveis:")
print(" U = Cima "
      "\n D = Baixo "
      "\n R = Direita "
      "\n L = Esquerda "
      "\n O = noroeste(cima-esquerda) "
      "\n N = Nordeste(cima-direita) "
      "\n E = Sudeste(baixo-direita) "
      "\n W = Sudoeste(baixo-esquerda) ")
print("----------------------------------------------------------")
movs = input("Digite um conjunto de movimentos para mover o robô:")

tempx, tempy, cont = pix, piy, 0


for l in movs:
    if l.isalpha():
        if l == 'U' or l == "u":
            tempy += 1
            cont += 1
        elif l == 'D' or l == 'd':
            tempy -= 1
            cont += 1
        elif l == 'R' or l == 'r':
            tempx += 1
            cont += 1
        elif l == 'L' or l == 'l':
            tempx -= 1
            cont += 1
        elif l == 'O' or l == 'o':
            tempy += 1
            tempx -= 1
            cont += 1
        elif l == 'N' or l == 'n':
            tempy += 1
            tempx += 1
            cont += 1
        elif l == 'E' or l == 'e':
            tempy -= 1
            tempx += 1
            cont += 1
        elif l == 'W' or l == 'w':
            tempy -= 1
            tempx -= 1
            cont += 1
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("A posição final de X é:", tempx, "e a posição final de Y é: ", tempy, sep=' ')
print("Seu robô se movimentou por:", cont, "pontos.", sep=' ')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")