c1 = int(input("Informe o primeiro número de cadastro:"))
v1 = int(input("Informe o valor gasto na compra deste primeiro cadastro:"))
c2 = int(input("Informe o segundo número de cadastro:"))
v2 = int(input("Informe o valor gasto na compra deste segundo cadastro:"))
c3 = int(input("Informe o terceiro número de cadastro:"))
v3 = int(input("Informe o valor gasto na compra deste terceiro cadastro:"))
g1 = 0
g2 = 0
g3 = 0


vt = v1 + v2 + v3
cm = (v1 + v2 + v3) / 3

if v1 > 100:
    print("O cadastro número", c1, "obteve um gasto maior que R$100")

elif v2 > 100:
    print("O cadastro número", c2, "obteve um gasto maior que R$100")

elif v3 >100:
    print("O cadastro número", c3, "obteve um gasto maior que R$100")

if v1 < 50:
    g1 = 1

elif v2 < 50:
    g2 = 1

elif v3 < 50:
    g3 = 1

else:
    g1 = 0
    g2 = 0
    g3 = 0

gt = g1 + g2 + g3

print("O valor total pago pelos três clientes foi de", vt, "reais")
print("O valor médio das compras é de R$", cm)
print(gt, "clientes efetuaram compras abaixo de 50 reais")