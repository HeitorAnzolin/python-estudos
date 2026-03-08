import os
tarefas = []

while True:

    # Interface
    print("""
    Menu:
    1 - Adicionar tarefa
    2 - Ver tarefas
    3 - Remover tarefa
    4 - Sair
""")
    entrada = input("Digite a opção desejada: ")

    if entrada == "1":
        tarefas.append(input("\nDigite a tarefa desejada: "))

    elif entrada == "2":
        print("\nTarefas: ")

        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}")

    elif entrada == "3":
        if not tarefas:
            print("\nNenhuma tarefa cadastrada.")
        else:
            remover = int(input("\nDigite o numero da tarefa que deseja remover da lista: "))
            if remover < 0 or remover >= len(tarefas):
                print("Opção inválida")
            else:
                tarefas.pop(remover)

    elif entrada == "4":
        break
    else:
        print("\nOpção  inválida, tente novamente.")
    
    input("\nPressione Enter para continuar ...")
    os.system('cls' if os.name == 'nt' else 'clear')
    