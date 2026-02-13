# Exemplo sem parênteses
conta_1 = 1 + 1 ** 5 + 5
print("Resultado da conta sem parênteses:", conta_1)

# O Python resolve assim:
# 1 ** 5 -> 1
# Depois: 1 + 1 + 5 -> 7

# Exemplo com parênteses
conta_2 = (1 + 1) ** (5 + 5)
print("Resultado com parênteses:", conta_2)

# Agora:
# (1 + 1) -> 2
# (5 + 5) -> 10
# 2 ** 10 -> 1024

# Parênteses internos e externos
resultado = ((0.5 + 0.5) + 1) * 12
print("Exemplo com parênteses aninhados:", resultado)