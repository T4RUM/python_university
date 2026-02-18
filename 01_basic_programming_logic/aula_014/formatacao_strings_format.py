print("\n=== 1) Por ordem (posicional implícito) ===")
a = "AAAAA"
b = "BBBBBB"
c = 1.1

msg = "a={} b={} c={}"
print(msg.format(a, b, c))

print("\n=== 2) Por índice (posicional explícito) + repetição ===")
msg = "b={1} a={0} a={0} c={2}"
print(msg.format(a, b, c))

print("\n=== 3) Por nome (mais legível) + float com 2 casas ===")
template = "b={nome2} a={nome1} a={nome1} c={nome3:.2f}"
formato = template.format(nome1=a, nome2=b, nome3=c)
print(formato)

print("\n=== 4) Format spec útil: alinhamento, largura, milhar, zeros ===")
nome = "João"
saldo = 12345.6789
codigo = 42

# Alinhamento e largura (10 caracteres)
print("Esquerda : |{:<10}|".format(nome))
print("Direita  : |{:>10}|".format(nome))
print("Centro   : |{:^10}|".format(nome))

# Separador de milhar + 2 casas decimais
print("Saldo    : R$ {:,.2f}".format(saldo))

# Inteiro com zeros à esquerda (5 dígitos)
print("Código   : {:05d}".format(codigo))

print("\n=== 5) Chaves literais: {{ e }} ===")
# Para imprimir { e } de verdade, use {{ e }}
print("Exemplo de JSON: {{\"nome\": \"{}\"}}".format("Ana"))