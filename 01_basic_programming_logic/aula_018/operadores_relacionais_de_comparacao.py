# ----------------------------
# Comparações básicas
# ----------------------------
maior = 2 > 1
maior_ou_igual = 1 >= 2
menor = 1 < 2
menor_ou_igual = 1 <= 2
igual = "a" == "a"
diferente = "a" != "b"

print("maior:", maior)
print("maior_ou_igual:", maior_ou_igual)
print("menor:", menor)
print("menor_ou_igual:", menor_ou_igual)
print("igual:", igual)
print("diferente:", diferente)

print("-" * 40)

# ----------------------------
# Comparações encadeadas
# ----------------------------
x = 7
print("x =", x)
print("0 <= x <= 10:", 0 <= x <= 10)
print("x está fora de 0..10?", not (0 <= x <= 10))

print("-" * 40)

# ----------------------------
# Strings: comparação lexicográfica (Unicode)
# ----------------------------
print('"a" < "b":', "a" < "b")
print('"A" < "a":', "A" < "a")
print('"casa" < "casaco":', "casa" < "casaco")  # prefixo costuma ser "menor"

# Padronizando texto (útil quando a intenção é comparar "sem ligar" para maiúsculas/minúsculas)
texto1 = "Python"
texto2 = "python"
print('texto1 == texto2:', texto1 == texto2)
print('texto1.lower() == texto2.lower():', texto1.lower() == texto2.lower())

print("-" * 40)

# ----------------------------
# == (valor) vs is (identidade)
# ----------------------------
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)   # mesmo conteúdo
print("a is b:", a is b)   # objetos diferentes
print("a is c:", a is c)   # mesmo objeto

print("-" * 40)