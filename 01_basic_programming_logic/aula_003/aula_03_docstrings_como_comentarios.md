# 🐍 Aula 03: Docstrings como “comentários”

Nesta aula aprendemos a diferença entre:

- **comentários de verdade** (com `#`)
- **docstrings** (com `"""` ou `'''`)

> **Importante:** docstring **não é comentário**.  
> O Python **lê** docstrings (ele cria uma string), mas muitas vezes “não faz nada” com ela se não estiver sendo usada.
---
## Docstring (""" ou ''')

Docstring é uma string de documentação.

Ela pode ser escrita com:
* """ (aspas duplas triplas)
* ''' (aspas simples triplas)

Docstrings podem ter múltiplas linhas, então muita gente usa isso como se fosse um “comentário multilinha”, principalmente para:
* anotações de estudo
* explicações longas
* documentação de funções e módulos (mais pra frente)
---
## Regras importantes das docstrings

* Se abrir com """, tem que fechar com """
* Se abrir com ''', tem que fechar com '''
* Não pode misturar aspas duplas e simples para abrir/fechar

✅ Certo:
```
"""Abriu com duplas, fechou com duplas"""
```
❌ Errado:
```
"""Abriu com duplas, fechou com simples'''
```
---
## O que acontece quando executamos?

Linhas com # são ignoradas.

Docstrings são lidas, viram uma string na memória, mas se não estiverem sendo usadas, o programa apenas segue em frente.

---

## ✅ Resumo da aula
- Comentários reais usam # e são ignorados pelo Python.
- Docstrings são textos criados com """ ou '''.
- Docstrings não são comentários; elas são strings lidas pelo Python.
- Podem ser usadas para documentação e explicações longas.
- Permitem múltiplas linhas de texto.
- Devem abrir e fechar com o mesmo tipo de aspas triplas.
- Quando não utilizadas, o programa simplesmente continua a execução.