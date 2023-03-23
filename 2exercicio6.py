u = int(input("Escolha o algarismo para ficar na casa das unidades:"))
d = int(input("Escolha o algarismo para ficar na casa das dezenas:"))


if u == 1:
    nu = "|"
    print("unidade igual 1")

elif u == 2:
    nu = "||"

elif u == 3:
    nu = "|||"

elif u == 4:
    nu = "|V"

elif u == 5:
    nu = "V"

elif u == 6:
    nu = "V|"

elif u == 7:
    nu = "V||"

elif u == 8:
    nu = "V|||"

elif u == 9:
    nu = "|X"

if d == 1:
    nd = "X"

elif d == 2:
    nd = "XX"

elif d == 3:
    nd = "XXX"

elif d == 4:
    nd = "XL"

elif d == 5:
    nd = "L"

elif d == 6:
    nd = "LX"

elif d == 7:
    nd = "LXX"

elif d == 8:
    nd = "LXXX"

elif d == 9:
    nd = "XC"

print("O seu número romano ficou assim:",nd,nu)
