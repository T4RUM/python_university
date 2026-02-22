# 🐍 Aula 20: `eval()`  Interpretando entradas dinamicamente em Python

Quando trabalhamos com entrada de dados no Python, existe um comportamento fundamental que precisa ser entendido profundamente:

> `input()` sempre retorna uma string.

A partir disso surgem diversos efeitos colaterais, alguns esperados, outros surpreendentes.

Nesta aula, vamos entender:
- por que `"5" * 2` resulta em `"55"`
- por que converter com `int()` ou `float()` nem sempre resolve
- o que `eval()` realmente faz
- quais são os riscos reais do seu uso
- qual é a alternativa profissional segura

---

## 🧩 Conceito: o comportamento real do `input()`

Independentemente do que o usuário digite:

```python
valor = input("Digite algo: ")
```
O tipo de valor será sempre:
````python
str
````
Mesmo que o usuário digite:
- ```5```
- ```2.5```
- ```True```
- ```[1, 2, 3]```

Tudo chega como texto.

---
## 🧩 Por que ```"5" * 2``` vira ```"55"```?
Em Python, o operador * tem comportamentos diferentes dependendo do tipo:

- número × número → multiplicação matemática
- string × inteiro → repetição de string

Exemplo:
````python
"5" * 2  # "55"
````
Não é erro. É o comportamento esperado do tipo str.

---
## 🧩 Conversão com int() e float()
Converter manualmente resolve alguns casos:
````python
int("5")      # 5
float("2.5")  # 2.5
````

Mas não é solução universal:

| Entrada   | int() | float() |
| --------- | ----- | ------- |
| `"5"`     | ✅     | ✅       |
| `"2.5"`   | ❌     | ✅       |
| `"1+2"`   | ❌     | ❌       |
| `"David"` | ❌     | ❌       |

> Essas funções convertem literais numéricos, não expressões ou estruturas.

---
## 🧠 Conceito: o que eval() faz de verdade
````eval()```` recebe uma string e:
> Interpreta essa string como uma expressão Python válida e retorna o resultado da avaliação.

Exemplos:
```python
eval("5")          # 5
eval("2.5")        # 2.5
eval("'David'")    # "David"
eval("1 + 2")      # 3
eval("[1, 2, 3]")  # lista
```
Ou seja:
- Não é apenas conversão.
- É execução de expressão Python.

> ⚠️ Isso é poderoso e perigoso.
---
## ⚠️ Armadilha 1: nomes sem aspas
Se alguém digitar:
```python
David
```
```eval("David")``` interpreta isso como:
````python
David
````
Ou seja, um identificador.
Se não existir variável com esse nome:
```
NameError
```
Strings precisam estar entre aspas para serem reconhecidas como literais.

---
## ⚠️ Armadilha 2: risco de segurança
````eval()```` executa código Python.

Se usado diretamente com entrada do usuário, pode executar qualquer expressão válida.

Em ambientes reais isso pode:
- acessar variáveis
- chamar funções
- executar operações inesperadas
- comprometer segurança

> 🔴 Regra profissional:
> 
> Nunca use ````eval()```` com entrada de usuário em sistemas reais.

---
## ✅ Alternativa segura: ast.literal_eval()
Se o objetivo é interpretar apenas literais Python, existe alternativa segura:
````python
from ast import literal_eval
````
````literal_eval()```` aceita apenas:
- números
- strings
- listas
- tuplas
- dicionários
- booleanos
- None

Não executa:
- chamadas de função
- expressões arbitrárias
- código dinâmico

É a opção correta quando você quer interpretar estruturas digitadas.

---
## 🚀 Estratégia profissional para entrada de dados
A decisão depende do que você quer permitir:

### 🎯 Se você quer apenas números:
Use conversão controlada:
- tente ````int()````
- se falhar, tente ````float()````
- se falhar, rejeite

### 🎯 Se você quer aceitar estruturas (listas, dicts etc):
Use ````ast.literal_eval()````

### 🎯 Se você quer avaliar expressões matemáticas:
- Não use eval() diretamente.
- Use bibliotecas específicas ou crie um parser controlado.
  - sympy
  - asteval
  - numexpr

| Biblioteca | Melhor para                        | Segurança  | Complexidade |
| ---------- | ---------------------------------- | ---------- | ------------ |
| `sympy`    | Matemática simbólica               | Média/Alta | Alta         |
| `asteval`  | Avaliação controlada estilo `eval` | Alta       | Média        |
| `numexpr`  | Expressões numéricas rápidas       | Alta       | Média        |

## 🧠 Diferença entre eval() e exec()
- eval() → avalia expressões
- exec() → executa blocos de código

Exemplo:
````python
eval("1 + 2")        # funciona
exec("x = 10")       # executa atribuição
````
> ⚠️ ````exec()```` é ainda mais perigoso com entrada externa.

---
## 🧠 O que aprendemos nesta aula?
- ````input()```` sempre retorna ````str````
- O operador ````*```` em string repete conteúdo
- ````int()```` e ````float()```` não interpretam expressões
- ````eval()```` avalia expressões Python
- Nomes sem aspas geram ````NameError````
- ````eval()```` é perigoso em produção
- ````ast.literal_eval()```` é alternativa segura para literais
- Escolher estratégia correta de parsing é decisão de arquitetura

---
## ✅ Resumo da aula
- Entrada de usuário chega como texto
- Multiplicação depende do tipo
- ````eval()```` executa expressão, não apenas converte
- Nunca use ````eval()```` com entrada externa em sistemas reais
- Prefira conversão controlada ou ````literal_eval()```` dependendo do caso
- Entender tipos e avaliação dinâmica é fundamental para escrever código seguro e profissional