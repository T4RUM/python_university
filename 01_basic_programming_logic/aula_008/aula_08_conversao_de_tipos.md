# 🐍 Aula 8: Conversão de tipos (type casting)

## 🔄 O que é conversão de tipos?
Conversão de tipos é o processo de transformar um tipo de dado em outro.

Esse processo também pode ser chamado de:
- Conversão de tipos
- Type conversion
- Type casting
- Coerção de tipos

Todos significam basicamente a mesma coisa.

---
## 🧠 Por que converter tipos?
Muitas vezes precisamos usar valores juntos em operações.
Exemplo válido:
```python
print(1 + 1)
```
Resultado:
```
2
```
Mas veja:
````python
print('a' + 'b')
````
Resultado:
```
ab
```
Aqui ocorre concatenação, não soma.

---
## ⚠️ Tipos incompatíveis geram erro
Se tentarmos misturar tipos diferentes:
````python
print('1' + 1)
````
O Python gera erro, porque:
- ```'1'``` é string
- ```1``` é inteiro

Python possui **tipagem forte**, então não mistura tipos automaticamente.

--- 
## 🧱 Tipos primitivos imutáveis
Os tipos básicos aprendidos até agora são:
- str
- int
- float
- bool

Esses tipos são chamados de **imutáveis**, ou seja, seu valor não pode ser alterado depois de criado.

---
## 🔧 Convertendo tipos
Python possui funções para converter tipos:

| Conversão     | Função    |
| ------------- | --------- |
| Para inteiro  | `int()`   |
| Para decimal  | `float()` |
| Para texto    | `str()`   |
| Para booleano | `bool()`  |

---
## 🔢 Convertendo string para inteiro
````python
print(int('1'))
````

Agora é possível somar:
````python
print(int('1') + 1)
````
Resultado:
````python
2
````
---
## 🔢 Convertendo para float
```python
print(float('1') + 1)
```
Resultado:
````python
2.0
````
Quando misturamos inteiro e float, o resultado vira float.

---
## 🔍 Verificando o tipo resultante
Podemos confirmar com type():
````python
print(type(float('1') + 1))
````
Resultado:
````python
<class 'float'>
````
---
## 🔘 Conversão para boolean
Algumas regras importantes:
### Valores considerados False
- ```''``` (string vazia)
- ```0```
- ```0.0```
- ```False```

Exemplo:
```python
print(bool(''))
```
Resultado:
````python
False
````
---
### Valores considerados True
Qualquer valor diferente dos anteriores:
````python
print(bool('1'))
print(bool(-1))
````
Resultado:
```python
True
True
```
----
## 🔤 Convertendo número para texto
Se quisermos juntar número com texto:
````python
print(str(11) + 'b')
````
Resultado:
````python
11b
````
---
## 🧠 Regra importante
Nem todo valor pode ser convertido.
Exemplo inválido:
````python
int('abc')
````
Isso gera erro, pois o texto não representa número.

---
## 🧠 Ordem de execução
Quando temos várias funções juntas:
````python
print(type(float('1') + 1))
````
O Python executa de dentro para fora:
1. ```'1'```
2. ```float('1')```
3. ```soma com 1```
4. ```type(...)```
5. ```print(...)```

---
## ✅ Resumo da aula

- Conversão de tipos transforma um tipo em outro.
- Python não converte tipos automaticamente.
- int(), float(), str() e bool() fazem conversões.
- Nem todo valor pode ser convertido.
- Misturar tipos sem conversão gera erro.
- Valores vazios ou zero viram False.
- Outros valores normalmente viram True.