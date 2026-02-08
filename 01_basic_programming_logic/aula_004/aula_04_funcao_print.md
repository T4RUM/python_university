# 🐍 Aula 4 — Função `print()` em Python


## 🖨️ O que é a função `print()`?

A função `print()` é usada para **exibir informações na tela**.

Exemplo simples:

```python
print("Olá, mundo!")
```
Tudo que colocamos dentro dos parênteses é mostrado no terminal.

---

## 📦 Argumentos da função
Os valores enviados para a função são chamados de argumentos.
Podemos enviar vários valores:
```pyhton
print(1, 2, 3, 4)
```
Resultado:
```python
1 2 3 4
```
Note que o Python coloca um espaço automaticamente entre os valores.

---
## 🔹 Argumentos não nomeados
Quando apenas colocamos valores separados por vírgula:
```python
print(10, 20)
```
Esses são chamados de argumentos não nomeados.

---
## 🔹 Argumentos nomeados
Também podemos alterar o comportamento da função usando argumentos nomeados.

Eles têm o formato:
```
nome = valor
```
Exemplo:
````python
print(10, 20, sep="-")
````
Resultado:
```
10-20
```
---
## ⚙️ Parâmetro sep (separador)
O parâmetro sep define o que aparece entre os valores.
Exemplo padrão:
```python
print(1, 2)
```
Resultado:
```python
1 2
```
Alterando:
````python
print(1, 2, sep="-")
````
Resultado:
```python
1-2
```
Também podemos remover o separador:
````python
print(1, 2, sep="")
````
Resultado:
```python
12
```
---
## ⚙️ Parâmetro end (final da linha)
Por padrão, o print() quebra a linha ao final.
Exemplo:
```python
print("A")
print("B")
```
Resultado:
```python
A
B
```
Mas podemos mudar isso:
```python
print("A", end="")
print("B")
```
Resultado:
```python
AB
```
---
## 🔽 Quebra de linha (\n)
O caractere especial:
```python
\n
```
significa quebra de linha.
Exemplo:
```python
print("Linha 1\nLinha 2")
```
Resultado:
```python
Linha 1
Linha 2
```
---
## 🖥️ Diferença entre sistemas
Sistemas operacionais usam símbolos diferentes internamente:
- Windows → ```\r\n```
- Linux / Mac → ```\n```

Hoje o Windows normalmente aceita apenas \n.

---
## 🧠 Python diferencia maiúsculas e minúsculas
Python é case sensitive.
Isso significa:
```python
print()
```
é diferente de:
```python
Print()
```
O segundo gera erro:
```python
NameError: name 'Print' is not defined
```
---
## ✅ Resumo da aula

A função print():
- Exibe dados na tela
- Pode receber vários valores
- Usa espaço como separador padrão
- Quebra linha automaticamente
- Permite alterar separador (sep)
- Permite alterar o final (end)
- Python diferencia letras maiúsculas e minúsculas