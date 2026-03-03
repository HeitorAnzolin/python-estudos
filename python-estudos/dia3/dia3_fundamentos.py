# EXERCÍCIO 1
"""
idade = int(input("Digite sua idade: "))
cnh = False

if idade >= 18:
    cnh = input("Você tem carteira de motorista? ")
    if cnh.lower() != 'yes':
        cnh = False

if idade >= 18 and cnh:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir")

"""

#EXERCÍCIO 2

usuario = 'admin'
senha = '1234'

user = input("USUÁRIO: ")
password = input("SENHA: ")

if user == usuario and password == senha:
    print("Acesso liberado")
else:
    print("Acesso negado")