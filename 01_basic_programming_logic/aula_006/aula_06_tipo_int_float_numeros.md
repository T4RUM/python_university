# 🐍 Aula 6: Tipos `int` e `float` (números)
---
## 🔢 Tipo `int` números inteiros
O tipo `int` representa números **sem casas decimais**.

Podem ser:
- Positivos
- Negativos
- Zero

Exemplos:

```python
print(11)
print(-11)
print(0)
```
Se não houver sinal, o número é considerado positivo.

---
## 🔹 Tipo float números decimais
O tipo float representa números com ponto decimal.
Exemplos:

```python
print(1.1)
print(0.0)
print(-1.5)
```
### ⚠️ Importante:
Na programação usamos ponto (.) e não vírgula para separar casas decimais.

---
## 📌 Vírgula não separa casas decimais
Na programação, a vírgula é usada para separar argumentos:

```python
print(1.1, 10.11)
```
Aqui estamos exibindo dois valores, não um número decimal.

---
## 🔍 Descobrindo o tipo com type()
A função type() mostra o tipo de um valor.
Exemplo:
```python
print(type(5))
print(type(1.5))
print(type("texto"))
```
Saída:
```python
<class 'int'>
<class 'float'>
<class 'str'>
```
---
## 🧠 Dica prática
- Se o número possui casas decimais → ```float```
- Se não possui casas decimais → ```int```
---
## ✅ Resumo da aula
- int representa números inteiros.
- float representa números com casas decimais.
- Números podem ser positivos, negativos ou zero.
- O ponto é usado para separar casas decimais.
- A vírgula separa argumentos.
- A função type() mostra o tipo de um valor.