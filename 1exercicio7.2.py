n1 = int(input("Escreva um número entre 10 e 50: "))

if 10 <= n1 <= 50:
    print("Parabéns!")

else:
    n2 = int(input("Vamos tentar denovo:"))
    if 10 <= n2 <= 50:
        print("Parabéns!")

    else:
        print("Eu desisto")