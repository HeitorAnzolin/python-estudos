"""
#Exercício 1
dicionario = {  #Inicializando um dicionário. Dicionários são uma forma de armazenar valores a designados termos
    "nome": "",
    "preco": 0,
    "quantidade": 0
    }

dicionario["nome"] = input("Digite o nome do produto: ")
dicionario["preco"] = float(input("Digite o preço: "))
dicionario["quantidade"] = int(input("Digite a quantidade: "))

dicionario["valort"] = dicionario["quantidade"] * dicionario["preco"]

print(f'''
      Produto: {dicionario["nome"]}
      Preço: {dicionario["preco"]}
      Quantidade: {dicionario["quantidade"]}
      Valor total: {dicionario["valort"]}
      ''')
"""

#Exercício 2
import os

lista_de_alunos = []

while True:
    print("""
    1 - Adicionar aluno
    2 - Ver alunos
    3 - Sair
""")
    entrada = int(input("Digite a opção desejada: "))
    
    if entrada == 3:
        break
    elif entrada == 1:      
        aluno = {
        "nome": "",
        "idade": 0,
        "nota": 0
        }

        aluno["nome"] = input("\nDigite o nome do aluno: ")
        aluno["idade"] = int(input("Digite a idade do aluno: "))
        aluno["nota"] = float(input("Digite a nota do aluno: "))

        lista_de_alunos.append(aluno)
    elif entrada == 2:
        for estudante in lista_de_alunos:
            print(f"\n{estudante["nome"]} - {estudante["idade"]} - {estudante["nota"]}")
    else:
        print("Opção inválida")
    input("Digite uma tecla para continuar....")
    os.system('cls' if os.name == 'nt' else 'clear')
