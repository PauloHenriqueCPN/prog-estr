n = int(input("Digite o número a ser transformado:"))

mr = ["", "M", "MM", "MMM",]
cr = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
dr = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ur = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

m = mr[n // 1000]
c = cr[(n % 1000) // 100]
d = dr[(n % 100) // 10]
u = ur[(n % 10)]

r = m + c + d + u

print("O seu número em romano é ", r)
