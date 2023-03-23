h = int(input("Digite um valor correspondente à horas:"))
m = int(input("Digite um valor correspondente à minutos:"))
s = int(input("Digite um valor correspondente à segundos:"))

hs = (h * 60) * 60
ms = m * 60
st = hs + ms + s

print("O total de segundos no tempo que você escolheu é de", st)