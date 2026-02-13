nome = "Uncle Bob"
idade = 73
peso = 95.0
altura = 1.80
formacao = "Engenharia de Software"
cidade = "Chicago"
salario = 150000.40

# 1) f-string básica
print(f"Nome: {nome}")
print(f"{nome} tem {idade} anos e mora em {cidade}.")

# 2) Inserindo múltiplos valores
print(f"{nome}, {idade}, {peso}, {formacao}, {cidade}, {altura}, {salario}")

# 3) Casas decimais (float)
print(f"Peso com 1 casa decimal: {peso:.1f}")
print(f"Altura com 2 casas decimais: {altura:.2f}")

# Exemplo com muitas casas (apenas para ver o efeito)
print(f"Altura com 10 casas decimais: {altura:.10f}")

# 4) Separador de milhar (útil para dinheiro)
print(f"Salário (com separador de milhar): {salario:,.2f}")

# 5) f-strings aceitam expressões
imc = peso / (altura ** 2)
print(f"IMC calculado: {imc:.2f}")

# Também funcionaria assim (expressão direto), mas nem sempre é o melhor estilo:
print(f"IMC direto na f-string: {peso / (altura ** 2):.2f}")