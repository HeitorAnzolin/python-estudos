lista = []

for n in range(5):
    lista.append(int(input("Digite um número: ")))

print(f"Lista digitada: {lista}\n")
print(f"Maior valor: {max(lista)}\n")
print(f"Menor valor: {min(lista)}\n")
print(f"Soma dos números: {sum(lista)}")