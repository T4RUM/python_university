# 🐍 Aula: Concatenação e repetição com operadores

Nesta aula aprendemos que alguns operadores aritméticos possuem comportamentos diferentes quando usados com **textos (strings)**.

Os operadores `+` e `*`, além de operações matemáticas, também podem ser usados com strings.

---
## ➕ Concatenação com o operador ```+```
Quando usamos `+` com strings, o Python **junta os textos**.

Esse processo é chamado de **concatenação**.

Exemplo:

```python
concatenacao = 'A' + 'B' + 'C'
print(concatenacao)
```
Resultado:
```python
ABC
```
Outro exemplo:
```python
nome_completo = "Guido" + " " + "van Rossum"
print(nome_completo)
```
Resultado:
```python
Guido van Rossum
```
Note que adicionamos " " para inserir um espaço entre os nomes.

---
## ⚠️ Cuidado com tipos diferentes
Se tentarmos misturar texto com número, ocorre erro:
```python
"Idade: " + 30
```
Isso gera erro porque:
- ```"Idade: "``` é string
- ```30``` é inteiro

Se for necessário, devemos converter:
```python
"Idade: " + str(30)
```
---
## ✖️ Repetição com o operador ```*```
O operador ```*``` pode repetir um texto várias vezes.
Exemplo:
```python
nome = "Guido "
print(nome * 3)
```
Resultado:
```python
Guido Guido Guido
```
Aqui usamos:
- uma string
- multiplicada por um número inteiro
---
## 🎨 Exemplo prático: criando um menu no terminal
Podemos usar repetição para criar divisores visuais:
```python
print("=" * 30)
print("       MENU PRINCIPAL")
print("=" * 30)
```
Resultado:
```text
==============================
       MENU PRINCIPAL
==============================
```
Isso é muito usado em programas de terminal.

---
## 🧠 O que aprendemos nesta aula?
Aprendemos que:

- ```+``` junta textos (concatenação)
- ```*``` repete textos
- devemos tomar cuidado com tipos diferentes
- operadores mudam de comportamento dependendo do tipo de dado

Esses recursos ajudam a formatar saídas no terminal e construir interfaces simples.

---
## ✅ Resumo da aula

- ```+``` concatena strings
- ```*``` repete strings
- tipos diferentes causam erro
- podemos converter números usando str()
- repetição ajuda a criar menus e separadores visuais