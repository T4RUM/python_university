# 🐍 Aula: Operadores aritméticos em Python (matemática)

Nesta aula, aprendemos os **operadores aritméticos**, ou seja, os símbolos que usamos para fazer contas no Python.

Eles são bem parecidos com a matemática que usamos na escola, mas com alguns detalhes importantes.

---
## ➕ Adição (`+`)
Soma dois valores.

Exemplo:
```python
adicao = 10 + 10
print(adicao)
```
---
## ➖ Subtração (```-```)
Subtrai um valor do outro.
```python
subtracao = 10 - 5
print(subtracao)
```
---
## ✖️ Multiplicação (```*```)
Multiplica dois valores.
```python
multiplicacao = 10 * 10
print(multiplicacao)
```
---
## ➗ Divisão (```/```)
A divisão com ```/``` sempre retorna um número decimal (```float```), mesmo que os números sejam inteiros.

Exemplo:
```python
divisao = 10 / 2
print(divisao)  # 5.0
```
Se tiver um número quebrado na conta, também funciona:
```python
divisao = 10 / 2.2
print(divisao)
```
✅ Regra importante:

```10 / 2``` → ```5.0``` (float)

---
## ➗ Divisão inteira (```//```)
A divisão com ```//``` faz uma divisão cortando as casas decimais (isso se chama truncar).
Exemplo:
```python
divisao_inteira = 10 // 3
print(divisao_inteira)  # 3
```
E se tiver float:
```python
divisao_inteira = 10 // 2.2
print(divisao_inteira)  # 4.0
```
✅ Resumo:

- ```/``` → retorna float com casas decimais
- ```//``` → corta as casas decimais

---
## 🔥 Exponenciação (```**```)
Serve para elevar um número ao outro (potência).
Exemplo:
```python
exponenciacao = 2 ** 10
print(exponenciacao)  # 1024
```
### ⚠️ Cuidado:

Potências podem crescer muito rápido e gerar números gigantes.

---
## 🧩 Módulo (```%```)  resto da divisão
O operador % retorna o resto de uma divisão.
Exemplo:
```python
resto = 55 % 2
print(resto)  # 1
```
Isso significa:
 - ```55 / 2``` dá ```27``` e sobra ```1```

---
## ✅ Usos muito úteis do módulo (%)
### 🔸 Saber se um número é par
Um número é par quando é divisível por 2, ou seja, o resto da divisão por 2 é zero:
```python
numero = 10
eh_par = numero % 2 == 0
print(eh_par)  # True
```

Se fosse 15:
```python
numero = 15
eh_par = numero % 2 == 0
print(eh_par)  # False
```
---
### 🔸 Saber se um número é múltiplo de outro
Um número é múltiplo de outro quando o resto da divisão é zero.
Exemplo: 16 é múltiplo de 8?
```python
numero = 16
eh_multiplo_de_8 = numero % 8 == 0
print(eh_multiplo_de_8)  # True
```
---
✅ Resumo da aula
- ```+``` soma
- ```-``` subtrai
- ```*``` multiplica
- ```/``` divide e sempre retorna float
- ```//``` divide e corta as casas decimais
- ```**``` faz potência
- ```%``` retorna o resto da divisão