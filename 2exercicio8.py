n1 = int(input("Digite o valor do primeiro número:"))
n2 = int(input("Digite o valor do segundo número:"))

print("""[1] soma
[2] subtração
[3] multiplicação
[4] divisão
[5] desistir""")

e = int(input("Escolha o que você quer fazer com os valores inseridos:"))

if e == 1:
    nt = n1 + n2
    print("O resultado da sua conta é", nt)

elif e == 2:
    nt = n1 - n2
    print("O resultado da sua conta é", nt)

elif e == 3:
    nt = n1 * n2
    print("O resultado da sua conta é", nt)

elif e == 4:
    nt = n1 / n2
    print("O resultado da sua conta é", nt)

elif e == 5:
    nt = print("Obrigado por tentar!")

else:
    print("Desculpe não temos essa opção")

