# Objetivo: usar o Debugger para ver o interpretador executando linha por linha.
# Dica: coloque breakpoints nas linhas marcadas com "BREAKPOINT".

print("=== Início do programa ===")

# Cenário: mude esses valores (ou altere durante o debug) e observe o caminho do código
condicao_1 = True
condicao_2 = False
condicao_3 = True
condicao_1 = False

print(f"{condicao_1=}")
print(f"{condicao_2=}")
print(f"{condicao_3=}")

# BREAKPOINT: coloque aqui e faça Step Over para ver as variáveis aparecerem no Debug
if condicao_1:
    # BREAKPOINT: veja que se este bloco executar, o interpretador vai pular os elif/else abaixo
    print("Bloco do IF: condição_1 foi verdadeira")

elif condicao_2:
    print("Bloco do ELIF 1: condição_2 foi verdadeira")

elif condicao_3:
    print("Bloco do ELIF 2: condição_3 foi verdadeira")

else:
    print("Bloco do ELSE: nenhuma condição foi verdadeira")

print("=== Fim do programa ===")