n1 = int(input("Vamos somar dois números para que fiquem entre 10 e 50. Escolha o primeiro número:"))
n2 = int(input("Agora escolha o segundo número:"))

s = n1 + n2

if 10 <= s <= 50:
    print("Parabéns, a sua soma deu", s)

else:
    print("Tente denovo, a sua soma de", s)