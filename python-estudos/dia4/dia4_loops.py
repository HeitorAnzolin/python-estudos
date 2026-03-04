# EXERCÍCIO 1
"""
num = 1

while num <= 5:
    print(num)
    num = num + 1
"""

#EXERCÍCIO 2
"""

senha = "1234"
entrada = ""

while entrada != senha:
    entrada = input("Digite a senha: ")

print("Acesso liberado")
"""

#EXERCÍCIO 3
"""
import os
os.system('cls' if os.name == 'nt' else 'clear')

import random
inteiro = random.randint(1, 10)

entrada = ""

while entrada != "3":
    print(''' 
              1 - Dizer Olá
              2 - Mostrar número
              3 - Sair
        ''')
    entrada = input("Escolha uma opção: ")
    if entrada == "1":
        print("OLÁ!")
    elif entrada == "2":
        print(inteiro)
    elif entrada != "3":
        print("Opção inválida!")
    input("Pressione Enter para continuar ...")
    os.system('cls')
"""

#EXERCÍCIO 4
"""

num = range(0,21)

for i in num:
    print(i)
"""

#EXERCÍCIO 5
"""
num = int(input("Digite um número inteiro: "))

aux = range( 1, 11)

for i in  aux:
    print(f"{num} * {i} = {num * i}")
"""

#EXERCÍCIO 6
"""
for i in range(10, 0,  -1):
    print(i)
print("FIM")
"""

#EXERCÍCIO 7
"""
soma = 0

while True:
    num = int(input("Digite um número ou 0 caso queira parar: "))
    soma = soma + num
    if num == 0:
        break
print(f"Soma = {soma}")
"""