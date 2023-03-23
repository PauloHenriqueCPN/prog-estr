si = int(input("Informe o salário fixo do vendedor:"))
v = int(input("Informe o total de vendas feitas no mês por este vendedor:"))

if 1000 < v <= 5000:
    p = 500
    print("Você conseguiu superar as vendas normais, parabéns! Receba esse bônus de R$500")

elif 5000 < v <= 7500:
    p = 700
    print("Você superou as expectativas, incrível! Receba esse bônus de R$700")

elif v > 7500:
    p = 1000
    print("Você vendeu quase a loja inteira! Receba esse bônus de 1000")

else:
    p = 0
    print("Se esforce no próximo mês para receber um prêmio")

sf = si + p

print("O salário final do vendedor é de", sf)