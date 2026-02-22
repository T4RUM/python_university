valor = input('Digite algo: ')
print("========== EXEMPLO 1: input() sempre retorna string ==========\n")

print('Valor digitado: ',valor)
print('Tipo: ',type(valor))
print('valor * 2: ',valor * 2)

print("\n========== EXEMPLO 2: Usando eval() ==========\n")

def cpf():
    numero_cpf = '123456789'
    print('Função cpf() foi executada!')
    print('CPF:', numero_cpf)
    return numero_cpf

expressao = input('Digite uma expressão Python válida: ') # Se você chamar a função aqui com cpf() ele vai acessar a função

resultado = eval(expressao)
print('Resultado: ',resultado)
print('Tipo: ',type(resultado))
print('resultado * 2: ',resultado * 2)
print('Cha mando a função cpf(): ', resultado)