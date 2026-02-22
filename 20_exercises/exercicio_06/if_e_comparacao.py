primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor informado {primeiro_valor} é maior que o segundo valor informado {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'O segundo valor informador {segundo_valor} é maior que o primeiro valor informado {primeiro_valor}')
else:
    print(f'O primeiro valor informado {primeiro_valor} é igual ao segundo valor informado {segundo_valor}')