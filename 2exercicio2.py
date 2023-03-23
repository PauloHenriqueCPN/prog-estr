print("""[1] celsius para fahrenheint
[2] fahrenheit para celsius
[3] polegadas para milímetros
[4] milímetros para polegadas
[5] terminar programa""")
escolha = int((input("O que você quer fazer a seguir? ")))

if escolha == 1:
    c1 = float(input("Digite a temperatura em celsius:"))
    f1 = ((c1 / 5) * 9) + 32
    print("A temperatura escolhida inicialmente em Celsius foi para", f1, "graus fahrenheit")

elif escolha == 2:
    f2 = float(input("Digite a temperatura em fahrenheint:"))
    c2 = ((f2 - 32) / 9) * 5
    print("A temperatura escolhida inicialmente em Fahrenheit foi para", c2, "graus celsius")

elif escolha == 3:
    p1 = float(input("Digite uma medida em polegadas:"))
    m1 = p1 * 25.4
    print("A medida inicialmente em polegadas foi para", m1, "milímetros")

elif escolha == 4:
    m2 = float(input("Digite uma medida em milímetros:"))
    p2 = m2 / 25.4
    print("A medida inicialmente em milímetros foi para", p2, "polegadas")

elif escolha > 5:
    print("Desculpe, não temos essa opção")

else:
    print("Obrigado, volte sempre!")











