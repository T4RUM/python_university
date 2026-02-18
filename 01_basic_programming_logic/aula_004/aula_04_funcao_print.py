# Exibindo valores
print(1, 2, 3, 4)

# Separador padrão (espaço)
print(10, 20)

# Mudando o separador
print(10, 20, sep="-")

# Sem separador
print(10, 20, sep="")

# Múltiplos valores
print(1, 2, 3, 4, sep=" | ")

# Controle do final da linha
print("Olá", end=" ")
print("mundo!")

# Sem quebra de linha
print("A", end="")
print("B")

print()  # linha vazia

# Quebra de linha manual
print("Linha 1\nLinha 2")

# Exemplo combinando separador e final
print(100, 200, sep="-", end=" *** ")
print("Fim")

# Exemplo de erro (comentado para não quebrar o código)
# Print("Erro")  # Python diferencia maiúsculas de minúsculas