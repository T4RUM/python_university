# 🐍 Exercício: Comparando dois valores informados pelo usuário

## 🧩 Desafio

Crie um programa que:

1. Peça ao usuário dois valores.
2. Compare esses valores.
3. Informe qual deles é maior.
4. Caso sejam iguais, informe que os valores são iguais.

O programa deve utilizar:

- `input()`
- Operadores de comparação (`>`, `<`, `==`)
- Estruturas condicionais (`if`, `elif`, `else`)

---

## 📌 Regras do exercício

Você deve:

- Criar duas variáveis
- Cada uma deve receber um valor digitado pelo usuário
- Comparar os valores utilizando operadores de comparação
- Exibir uma mensagem clara informando:
  - Se o primeiro valor é maior
  - Se o segundo valor é maior
  - Ou se ambos são iguais

---

## 🧠 Conceitos importantes antes de começar

### 🔹 1) `input()` sempre retorna string

Mesmo que o usuário digite números, o tipo será:
````python
str
````

Isso significa que, neste exercício, você **não deve converter os valores para número**.
A comparação será feita entre strings.

---
### 🔹 2) Comparação entre strings
Quando você compara strings, o Python utiliza a tabela Unicode para determinar ordem.

Exemplo:
````python
"A" < "B"
````
Isso funciona porque cada caractere possui um valor numérico interno.

> ⚠️ Isso significa que a comparação não é matemática, e sim baseada na ordem dos caracteres.

---
### 🔹 3) Operadores de comparação

Você pode usar:
- `>`  maior que
- `<`  menor que
- `==` igual

Esses operadores retornam `True` ou `False`.

---
## 🏗 Estrutura esperada
Você deve usar algo como:
````python
if condição:
...
elif condição:
...
else:
...
````
A lógica deve garantir que apenas um dos blocos seja executado.

---
## 🧪 Exemplos de comportamento esperado
Se o usuário digitar:
````python
1
2
````

> O programa deve informar que o segundo valor é maior.

Se digitar:
````python
2
1
````
> O programa deve informar que o primeiro valor é maior.

Se digitar:
````python
A
B
````
> O programa deve informar que `"B"` é maior que `"A"`.

Se digitar valores iguais, deve informar que são iguais.

---
## ⚠️ Armadilhas comuns

- Esquecer que `input()` retorna string.
- Usar apenas `if` sem tratar o caso de igualdade.
- Escrever condições que se sobrepõem.
- Não testar com letras para entender como a comparação funciona.

---

## 🚀 Desafio extra (opcional)

Após resolver utilizando strings:

- Faça uma segunda versão convertendo os valores para números.
- Compare os comportamentos.
- Observe a diferença entre comparação textual e numérica.

---

## 🧠 O que aprendemos neste exercício?

- Como usar operadores de comparação
- Como estruturar decisões com `if`, `elif`, `else`
- Como o Python compara strings internamente
- A importância de entender o tipo de dado antes de comparar

---

## ✅ Resumo do exercício

- Entrada: dois valores digitados pelo usuário
- Processamento: comparação usando operadores relacionais
- Saída: mensagem informando qual valor é maior ou se são iguais
- Objetivo: treinar lógica condicional e entendimento de tipos