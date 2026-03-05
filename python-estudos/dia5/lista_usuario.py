lista = []
i = 0

while i < 5:
    lista.append(int(input("Digite um número: ")))
    i += 1

print("Você digitou: ")
for num in lista:
    print(num)

if 5 in lista:
    print("5 ESTA NA LISTA")