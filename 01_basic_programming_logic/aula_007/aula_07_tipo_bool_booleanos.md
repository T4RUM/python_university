# 🐍 Aula 7: Tipo `bool` (boolean)

---
## 🔘 O que é o tipo booleano?
O tipo `bool` representa valores lógicos usados para responder perguntas dentro do programa.

Em programação, só existem duas respostas possíveis:

- `True` → Verdadeiro
- `False` → Falso

Esses valores permitem que o programa tome decisões.

---
## ❓ Fazendo perguntas ao programa
Programas frequentemente precisam verificar condições:

- Um valor é igual a outro?
- Um número é maior que outro?
- Algo aconteceu ou não?

Essas verificações retornam sempre:

```True``` ou ```False```

---
## ⚙️ Operador de comparação `==`
O operador `==` verifica se dois valores são iguais.

Exemplo:

```python
print(10 == 10)
```
Resultado:
```
True
```
Outro exemplo:
```python
print(10 == 11)
```
Resultado:
````
False
````
### ⚠️ Importante:
- ```==``` é comparação.
- ```=``` será usado depois para atribuição de valores.
---
## 🔍 Descobrindo o tipo booleano
Podemos usar type() para ver o tipo do valor retornado:
````python
print(type(10 == 10))
````
Resultado:
```
<class 'bool'>
```
Isso mostra que o resultado é do tipo booleano.

---
## 🧠 Dica prática
Sempre que o programa precisa responder sim ou não, ele usa valores booleanos:
- ```True```
- ```False```

Esse tipo será muito usado quando começarmos a controlar o fluxo do programa.

---
## ✅ Resumo da aula
- O tipo bool possui apenas dois valores: True e False.
- Valores booleanos representam respostas lógicas.
- O operador == compara valores.
- Comparações retornam True ou False.
- A função type() pode mostrar o tipo booleano.
- Booleanos serão usados para controlar decisões no programa.