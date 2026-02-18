# Pergunta ao usuário e normaliza para minúsculas
entrada = input("Você quer entrar ou sair? ").lower()

# Se usuário quiser entrar
if entrada == "entrar":
    print("Você entrou no sistema")

# Se usuário quiser sair
elif entrada == "sair":
    print("Você saiu do sistema")

# Qualquer outra coisa digitada
elif entrada != "entrar" and entrada != "sair":
    print('Opção inválida, escolha "entrar" ou "sair"')