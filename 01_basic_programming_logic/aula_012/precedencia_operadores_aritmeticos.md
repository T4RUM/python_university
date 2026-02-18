# 🐍 Aula 12: Precedência entre operadores aritméticos

Nesta aula vamos entender como o Python decide **qual parte de uma conta deve ser executada primeiro**.

Esse conceito é chamado de **precedência de operadores**.

Mesmo quem já programa pode se confundir quando não presta atenção na ordem de execução das operações.

O objetivo aqui é entender:
- por que algumas contas dão resultados inesperados
- como o Python resolve expressões matemáticas
- como usar parênteses para controlar a ordem
- e como evitar erros comuns em código real

---

## 🧩 Por que isso é importante?
Observe a expressão:

```python
1 + 1 ** 5 + 5
```

Muitas pessoas imaginam que o Python calcula da esquerda para a direita:
```python
(1 + 1) → 2
2 ** 5 → 32
32 + 5 → 37
```

Mas não é isso que acontece.

O Python segue regras de prioridade entre operadores.

E entender isso evita muitos erros.

---
## 🥇 Ordem de precedência dos operadores
Em expressões aritméticas, a ordem é:
- ```( )``` → parênteses
- ```**``` → potenciação
- ```* / // %``` → multiplicação, divisão, divisão inteira e módulo
- ```+ -``` → soma e subtração

Quando operadores possuem a mesma prioridade, o Python resolve da esquerda para a direita.

---
## ❓ Por que o resultado foi 7?
Na expressão:
````python
1 + 1 ** 5 + 5
````
O Python executa:
1. Primeiro a potência:
```
1 ** 5 → 1
```
2. Depois soma:
````python
1 + 1 + 5 → 7
````
3. Resultado final:
````python
7
````
---
## ✅ Usando parênteses para controlar a conta
Se queremos que as somas aconteçam antes:
````python
(1 + 1) ** (5 + 5)
````
Agora temos:
```python
2 ** 10 → 1024
```
Os parênteses permitem forçar a ordem desejada.

---
## 🧠 Parênteses são resolvidos de dentro para fora
Quando há parênteses dentro de outros, o Python resolve:
1. primeiro os mais internos
2. depois os externos
3. e só então o restante da expressão

Isso permite montar expressões complexas sem ambiguidades.

---
## ⚠️ Armadilha comum com operadores iguais
Observe:
````python
10 / 2 * 5
````
Algumas pessoas pensam que isso vira:
````python
10 / (2 * 5)
````
Mas operadores de mesma precedência são resolvidos da esquerda para a direita:
````python
10 / 2 → 5
5 * 5 → 25
````
Resultado final:
````python
25
````
## 🚀 Boa prática usada por programadores experientes
Mesmo sabendo a precedência, profissionais costumam escrever:
````python
resultado = (salario + bonus) * taxa
````
em vez de:
````python
resultado = salario + bonus * taxa
````
Porque código claro é melhor que código curto.

Parênteses evitam dúvidas futuras.

---
## 🧠 Curiosidade: potenciação funciona diferente
A potenciação é avaliada da direita para a esquerda.

Exemplo:
````python
2 ** 3 ** 2
````
O Python calcula:
````python
2 ** (3 ** 2)
````
Resultado:
````python
2 ** 9 → 512
````
E não:
````python
(2 ** 3) ** 2 → 64
````
Esse detalhe costuma surpreender até programadores experientes.

---

## 🧠 O que aprendemos nesta aula?
Aprendemos que:
- operadores possuem prioridade de execução
- potenciação acontece antes de soma
- operadores iguais executam da esquerda para a direita
- parênteses controlam a ordem da conta
- expressões podem gerar resultados inesperados sem parênteses
- variáveis podem receber novos valores ao longo do programa

---

## ✅ Resumo da aula
- ```( )``` executa primeiro
- ```**``` vem depois
- ```* / // %``` vêm em seguida
- ```+ -``` executam por último
- operadores iguais executam da esquerda para a direita
- parênteses evitam ambiguidades
- código claro é melhor do que código compacto


