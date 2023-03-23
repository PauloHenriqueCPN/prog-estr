L = int(input("Informe o valor do lado maior do retângulo:"))
l = int(input("Informe o valor do lado menor do retângulo:"))
r = int(input("Informe o valor do raio dp círculo:"))

ar = L * l
ac = r**2 * 3.14

af = ar - ac

print("A área não ocupada pelo círculo é de", af)