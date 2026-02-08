# Conversão de tipos (type casting)
# Tipos imutáveis e primitivos: str, int, float, bool

print(1 + 1)          # soma de inteiros
print('a' + 'b')      # concatenação de strings

# print('1' + 1)      # erro: tipos incompatíveis

# Exibindo valor e tipo
print('1', type('1'))

# Convertendo string para inteiro
print(int('1'), type(int('1')))
print(int('1') + 1)

# Conversão para float
print(type(float('1') + 1))

# Conversão para boolean
print(bool('1'))   # True
print(bool(''))    # False
print(bool(-1))    # True

# Convertendo número para string
print(str(11) + 'b')