num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

operador = input("Digite a operação que deseja executar(+,-,*,/): ")

if operador == '+':
    print(f"{num1} {operador} {num2} = {num1 + num2}")
elif operador == '-':
    print(f"{num1} {operador} {num2} = {num1 - num2}")
elif operador == '-':
    print(f"{num1} {operador} {num2} = {num1 * num2}")
elif operador == '-':
    print(f"{num1} {operador} {num2} = {num1 / num2}")
else:
    print("Esse operador não é aceito!")