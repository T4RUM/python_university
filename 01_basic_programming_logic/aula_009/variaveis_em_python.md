# 🐍 Aula 9: Variáveis em Python

## 🧠 O que são variáveis?
Variáveis são usadas para **guardar valores na memória do computador**.

---

Você pode imaginar uma variável como:
- uma **caixinha**
- um **apelido**
- uma **etiqueta** que aponta para um valor

Quando usamos o nome da variável, o Python nos entrega o valor guardado nela.

---
## 📝 Como criar uma variável
Em Python, usamos o sinal `=` para **atribuir um valor** a uma variável.

```python
nome = "Guido"
```
Aqui:

- ```nome``` → é o nome da variável
- ```=``` → operador de atribuição
- ```"Guido"``` → valor guardado
---
## 🎨 Regras de nomes (PEP 8)
O Python segue um guia de estilo chamado PEP 8.

Algumas regras importantes:
- usar letras minúsculas
- palavras compostas usam ```_```
- evitar nomes confusos

Exemplos corretos:
````python
nome_completo = "Guido van Rossum"
idade = 67
````
Esse estilo é chamado de snake_case 🐍

---
## 🧱 Tipos de dados mais comuns
Até agora, vimos alguns tipos básicos:

| Tipo  | Exemplo          |
| ----- | ---------------- |
| str   | `"texto"`        |
| int   | `10`             |
| float | `3.14`           |
| bool  | `True` / `False` |

---
## 🧮 Variáveis podem guardar expressões
Uma variável não precisa receber apenas um valor fixo.

Ela pode receber o resultado de uma conta ou pergunta:
```python
idade = 20
maior_de_idade = idade >= 18
```
Aqui estamos perguntando algo ao programa.

O resultado será:

- ```True``` se for maior ou igual a 18
- ```False``` se não for
---
## 📢 Exibindo valores com print
Para mostrar algo na tela, usamos ```print()```:
```python
print(nome)
print(idade)
print(maior_de_idade)
```
---
## 🔗 Usando variáveis dentro de textos
Podemos misturar texto com variáveis usando f-strings:
```python
nome = "Uncle Bob"
print(f"Olá, meu nome é {nome}")
```
Isso deixa o código mais claro e organizado.

---
## 🔁 Por que usar variáveis?
Variáveis não servem para abreviar código.

Elas servem para:
- tornar o código mais legível
- evitar repetição
- facilitar manutenção

Exemplo ruim:
```python
print(10 * 2)
print(10 * 2)
```

Exemplo bom:
```python
numero = 10
print(numero * 2)
print(numero * 2)
```
Agora, se o valor mudar, você altera em um único lugar.

----
## ⚠️ Nomes precisam fazer sentido
O nome da variável deve refletir o valor que ela guarda.

Errado:
````python
numero = True
````
Melhor:
````python
tem_permissao = True
````
Isso evita confusão para você e para outros desenvolvedores.

---
## 🧠 Pensando como programador
Quando criamos variáveis:
- guardamos algo na memória
- damos um nome claro
- usamos esse nome sempre que precisarmos do valor

Esse conceito é fundamental e será usado durante toda a nossa vida como programadores.

---
## ✅ Resumo da aula
- Variáveis guardam valores na memória.
- Usamos = para atribuir valores.
- PEP 8 define boas práticas de nomes.
- Variáveis deixam o código legível.
- Podemos guardar valores, contas e perguntas.
- Bons nomes evitam bugs e confusão.
