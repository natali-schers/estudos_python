#python.exe .\manipulacao_listas.py

numeros_pares = [2, 4, 6, 8, 10]
print(numeros_pares)

numeros_pares.append(12)
print(numeros_pares)

numeros_pares.remove(2)
print(numeros_pares)

# -1 acessa o último elemento da lista
print(numeros_pares[-1])

# Alterar o valor de um índice específico
numeros_pares[1] = 24
print(numeros_pares)