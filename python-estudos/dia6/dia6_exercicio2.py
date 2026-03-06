lista = []

while True:
    numero = int(input("Digite um número, 0 para parar: "))
    if numero == 0:
        break
    lista.append(numero)

if len(lista) == 0:
    print("Nenhum número foi digitado")
else:
    print(f"Foram digitados {len(lista)}")
    print(f"O maior número digitado foi {max(lista)}")
    print(f"O menor número digitado foi {min(lista)}")
    print(f"A média é {sum(lista)/len(lista)}")
