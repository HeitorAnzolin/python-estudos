"""num = float(input("Digite um número:"))

if num > 0:
    print(f"O número {num} é positivo")
elif num < 0:
    print(f"O número {num} é negativo")
else:
    print("O número é zero")
    """

valor = input("Digite algo: ")
valor = valor.strip()
if valor:
    print("Você digitou algo")
else:
    print("Você não digitou nada")