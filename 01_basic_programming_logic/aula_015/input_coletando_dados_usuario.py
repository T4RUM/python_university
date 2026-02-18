# 1) Coletando texto do usuário
nome = input("Qual o seu nome? ")
print(f"O seu nome é {nome}")
print(f"O seu nome é {nome=}")  # mostra nome da variável e o valor (útil para aprender)

print("\n--- Agora vamos pedir dois números ---")

# 2) Lembrete importante: input() SEMPRE retorna string
primeiro_numero_str = input("Digite um número: ")
segundo_numero_str = input("Digite outro número: ")

# Se você "somar" strings, acontece concatenação:
print(f"Somando como texto (concatenação): {primeiro_numero_str + segundo_numero_str}")

# 3) Convertendo para int (pode dar erro se o usuário digitar algo inválido)
primeiro_numero = int(primeiro_numero_str)
segundo_numero = int(segundo_numero_str)

print(f"A soma dos dois números é {primeiro_numero + segundo_numero}")

# Experimente:
# - digitar 1 e 5 (vai mostrar concatenação 15 e soma 6)
# - digitar 10 e 20 (concatenação 1020 e soma 30)
# - digitar algo como "a" (vai quebrar na conversão: isso será tratado nas próximas aulas)