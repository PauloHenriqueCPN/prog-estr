x = int(input("Digite o valor de x:"))
y = int(input("Digite o valor de y:"))

if x == 0:
    if y > 0 or y < 0:
        q = -1

    elif y == 0:
        q = 0

elif y == 0:
    if x > 0 or x < 0:
        q = -1

elif x > 0:
    if y > 0:
        q = 1

    elif y < 0:
        q = 4

elif y > 0:
    if x < 0:
        q = 2

elif x < 0 and y < 0:
    q = 3

print("A coordenado do ponto adiquirido é", q)