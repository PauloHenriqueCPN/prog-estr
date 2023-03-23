print("Informe o nome do produto:")
p = input()

v = int(input("Informe o valor do produto:"))
q = int(input("Informe a quantidade comprada do produto:"))

if 3 == q < 5:
    d = (v * q) * 0.1
    vf = (v * q) - d
    print("Você obteve um desconto de 10%")

elif q >= 5:
    d = (v * q) * 0.2
    vf = (v * q) - d
    print("Você obteve um desconto de 20%")

else:
    vf = (v * q)
    print("Você não obteve desconto na compra")

print("O produto comprado foi", p)
print("O valor total é de", vf)