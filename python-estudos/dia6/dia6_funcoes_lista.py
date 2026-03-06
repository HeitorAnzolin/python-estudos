lista_numeros = [1, 2, 3, 4, 5, 6, 8, 9, 11]

# A função insert adiciona um item na lista em determinada posição : lista.insert(posição, item)
lista_numeros.insert(6, 7)

# A função append adiciona um item no final da lista: lista.append(item)
lista_numeros.append(10)

# A função pop remove e retorna o item em determinada posição: item = lista.pop(posição), ou lista.pop() que remove e retorna o último valor
print(f"Foi removido {lista_numeros.pop(9)} da lista {lista_numeros}\n")

# A função remove, remove a primeira ocorrencia de um valor específico e gera erro se não existir o valor
lista_numeros.remove(10)

print(lista_numeros)

# A função len retorna o tamanho da lista: len(lista)
print(f"O tamanho da lista é {len(lista_numeros)}\n")

# A função sum retorna a soma dos valores numéricos da lista, funciona apenas com números: sum(lista)
print(f"A soma dos termos da lista é {sum(lista_numeros)}\n")

# A função max retorna o valor máximo da lista: max(lista)
print(f"O valor máximo da lista é {max(lista_numeros)}\n")

# A função min retorna o valor mínimo da lista: min(lista)
print(f"O valor mínimo da lista é {min(lista_numeros)}")