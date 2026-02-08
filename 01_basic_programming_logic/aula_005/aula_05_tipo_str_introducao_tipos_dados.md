# 🐍 Aula 5 — Tipo `str` (string) e introdução aos tipos de dados
---

## 📦 O que são tipos de dados?
Tipos de dados representam **o tipo da informação** que estamos usando no programa.

Exemplos comuns:
- Texto → string (`str`)
- Número inteiro → (`int`)
- Número decimal → (`float`)
- Verdadeiro ou falso → (`bool`)

Nesta aula focamos em **strings**.

---
## 🧠 Tipagem dinâmica e forte
Python é uma linguagem com tipagem:

- **Dinâmica** → não precisamos declarar o tipo da variável; o Python detecta automaticamente.
- **Forte** → o Python não mistura tipos incompatíveis automaticamente.

---
## 🔤 O que é uma string (str)?
Strings são textos.
Em Python, textos ficam dentro de:

- Aspas simples ```'```
- Aspas duplas ````"````

Exemplo:
```python
print('Guido')
print("Guido")
```
Ambos funcionam da mesma forma.

---
## 🔁 Misturando aspas
Podemos usar aspas diferentes dentro do texto:
```python
print("Guido 'Rossum'")
print('Guido "Rossum"')
```
Isso evita erros e deixa o código mais limpo.

---
## 🔐 Caractere de escape
Quando precisamos usar a mesma aspa dentro do texto, usamos o caractere de escape:
```
\
```
Exemplo:
```python
print("Guido \"Rossum\"")
```
O Python entende que a aspa faz parte do texto.

---
## 🧱 Strings raw (r"")
Podemos usar r antes do texto para impedir que o Python interprete caracteres especiais:
```python
print(r"Guido \"Rossum\"")
```
Nesse caso, a barra aparece no resultado.

---
## 🔢 Texto x Número
Compare:
```python
print("123")  # texto
print(123)    # número inteiro
```
Mesmo parecendo iguais, são tipos diferentes.

---
## 🧠 Dica prática
Quando precisar colocar aspas dentro do texto, prefira inverter o tipo de aspas:
```python
print('Texto com "aspas" internas')
```
Fica mais limpo e legível.

---
## ✅ Resumo da aula
- Python possui tipagem dinâmica e forte.
- str representa textos.
- Strings ficam dentro de aspas.
- Podemos usar aspas simples ou duplas.
- Caracteres de escape permitem usar aspas internas.
- Strings são diferentes de números.