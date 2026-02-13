# 🐍 Aula: Introdução às f-strings (formatação de strings)

Nesta aula você vai aprender uma forma moderna e prática de **formatar strings** no Python: as **f-strings**.


A ideia é simples: em vez de ficar usando várias vírgulas no `print()` ou concatenando com `+`, você escreve uma string “normal” e **insere variáveis dentro dela**.

---

## 🧩 O que é uma f-string?
Uma f-string é uma string com um `f` antes das aspas:

```python
f"texto aqui"
```
Esse ```f``` habilita a interpolação: você pode colocar expressões dentro de ```{}```:
```python
f"Meu nome é {nome}"
```
✅ Dentro das chaves você pode usar:
- variáveis (```{nome}```)
- expressões (```{peso / altura**2}```)
- chamadas simples (```{nome.upper()}```)

---
## ✅ Por que f-strings são tão usadas?
Porque elas são:
- legíveis (fica “parecido com a frase final”)
- rápidas (em geral, mais performáticas do que concatenação repetida)
- poderosas (formatam números, datas, alinhamento, etc.)

Em código real, f-strings viram padrão.

---
## 🔧 O essencial: colocar variáveis dentro do texto
A regra é:
- ```f``` antes da string
- ```{}``` ao redor do que você quer renderizar

Exemplo mental:
- Sem ```f```: ```{nome}``` é só texto
- Com ```f```: ```{nome}``` vira o valor da variável
---
## 🎯 Formatando números com ```“:”```
O ponto forte das f-strings é a parte de formatação, que vem depois de ::
````python
f"{valor:formato}"
````
Você vai usar isso muito para:
### ✅ Casas decimais
- ```:.2f``` → 2 casas decimais (float)

Exemplos de leitura:
- ```:.1f``` → 1 casa decimal
- ```:.2f``` → 2 casas decimais
- ```:.10f``` → 10 casas decimais
---
## 💰 Separador de milhar (útil para dinheiro)
Você pode formatar com separador de milhar usando:
````python
:,.2f
````
Isso gera saída no padrão “internacional”:
- vírgula separa milhar
- ponto separa decimais

✅ É muito útil para logs, relatórios, dashboards, exports etc.

---
## 🚀 Dica profissional: f-strings aceitam expressões (com cuidado)
Exemplo:
````python
f"IMC: {peso / (altura ** 2):.2f}"
````
Isso é válido e prático.
### ⚠️ Em projetos maiores, é comum calcular antes em variáveis para manter legibilidade:
- melhor para testar
- melhor para debugar
- melhor para manter
---
## 🧠 O que aprendemos nesta aula?
Aprendemos que:
- f-strings são strings com ````f```` antes das aspas
- usamos ````{}```` para inserir variáveis e expressões
- ````:```` permite aplicar formatos (ex: casas decimais)
- ````:,.2f```` ajuda a exibir números grandes com separador de milhar
- f-strings tornam o código mais claro e profissional
---
## ✅ Resumo da aula
- ```f"..."``` habilita formatação
- ```{variavel}``` insere valores no texto
- ```{valor:.2f}``` controla casas decimais
- ```{valor:,.2f}``` adiciona separador de milhar
- ```f-strings``` são a forma mais comum e moderna de formatar strings em Python