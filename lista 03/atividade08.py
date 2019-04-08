texto = input("digite um texto: ")
cont = 0
for letra in texto:
    if letra.isupper():
        cont += 1

print("Você digitou", cont, "letras maiúsculas.", sep=' ')
