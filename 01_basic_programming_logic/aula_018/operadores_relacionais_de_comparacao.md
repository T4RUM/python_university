# 🐍 Aula 18: Operadores de comparação (relacionais) em Python

Operadores de comparação servem para **comparar dois valores** e obter uma resposta lógica: **`True` ou `False`**. Eles são a base de praticamente toda tomada de decisão em código (como validações e condições).

---

## 🧩 Operadores de comparação

| Operador | Significado | Exemplo que dá `True` |
|---|---|---|
| `>`  | maior que | `2 > 1` |
| `>=` | maior ou igual | `2 >= 2` |
| `<`  | menor que | `1 < 2` |
| `<=` | menor ou igual | `2 <= 2` |
| `==` | igual (comparação) | `'a' == 'a'` |
| `!=` | diferente | `'a' != 'b'` |

✅ Qualquer expressão com esses operadores retorna um **booleano** (`True`/`False`).

---

## ⚠️ Armadilha: `=` não compara, `=` atribui

- `=` **atribui** um valor a uma variável (leia como “recebe”).
- `==` **compara** dois valores (leia como “é igual?”).

✅ Use `=` para guardar valores e `==` para comparar.

---

## ✅ Como pensar em `>=` e `<=` sem confusão

- `x >= y` significa: **x é maior que y OU x é igual a y**
- `x <= y` significa: **x é menor que y OU x é igual a y**

🧠 Dica mental útil: `>=` e `<=` são “duas possibilidades” no significado, mas você escreve **um único operador**.

---

## 🧩 Comparar números: o caso mais comum

Comparações com números aparecem o tempo todo:

- validar se uma nota passou (`>= 7`)
- checar limites (`0 <= x <= 10`)
- ordenar valores (`a > b`)

---

## 🧠 Comparações encadeadas (bem estilo Python)

Python permite escrever comparações em cadeia:

- `0 <= x <= 10`

🚀 Dica profissional: isso melhora legibilidade e evita repetições como `x >= 0 and x <= 10`.

---

## ⚠️ Comparar strings: funciona, mas pode surpreender

Strings podem ser comparadas, mas o critério é **ordem lexicográfica** (tipo “ordem de dicionário”), baseada nos **code points Unicode**.

Exemplos típicos:
- `"a" < "b"` → `True`
- `"A" < "a"` → geralmente `True` (maiúsculas vêm antes de minúsculas em Unicode)

⚠️ Armadilha comum: acentos, maiúsculas/minúsculas e variações podem gerar resultados inesperados.

✅ Boas práticas quando o objetivo é “comparar texto” no sentido humano:
- padronizar com `.lower()`/`.upper()` antes de comparar
- ou usar comparações de igualdade (`==`) com regras bem definidas

---

## ⚠️ Armadilha importante: `==` vs `is`

- `==` compara **valor**
- `is` compara **identidade** (se é o mesmo objeto na memória)

✅ Para comparar valores, use `==`.  
🚀 Uso comum de `is`: checar `None` (`x is None`).

---

## ⚠️ Armadilha: ponto flutuante (float) pode falhar no `==`

Nem todo decimal é representável exatamente em binário. Por isso, contas com `float` podem gerar pequenas diferenças:

- `0.1 + 0.2` pode não ser exatamente `0.3`
- então `0.1 + 0.2 == 0.3` pode dar `False`

✅ Boa prática: usar comparação com tolerância (`math.isclose`).

---

## 🧪 Usando o Python de forma interativa com seu arquivo

Para experimentar as variáveis do arquivo sem ficar adicionando `print` o tempo todo:

- `python -i aula_operadores_comparacao.py`

Isso executa o arquivo e deixa o interpretador aberto para você testar expressões e ver resultados.

🚀 Dica profissional: evite `print` “solto” quando quiser reaproveitar o arquivo como módulo no futuro. Uma forma padrão é proteger a execução com `if __name__ == "__main__":` (você vai entender melhor isso quando chegar em módulos/organização de código).

---

## 🧠 O que aprendemos nesta aula?
- Quais são os operadores de comparação (`>`, `>=`, `<`, `<=`, `==`, `!=`)
- Que toda comparação retorna `True` ou `False`
- Diferença entre atribuição (`=`) e comparação (`==`)
- Como interpretar corretamente `>=` e `<=`
- Comparações encadeadas (`0 <= x <= 10`)
- Comparação de strings e por que pode surpreender
- Diferença entre `==` e `is`
- Por que comparar `float` com `==` pode falhar e como fazer melhor

## ✅ Resumo da aula
Operadores relacionais comparam valores e retornam booleanos. Eles são essenciais para validações e lógica. Além de números, strings também podem ser comparadas (com atenção à ordem Unicode). Para código mais claro, comparações encadeadas ajudam bastante. E, em situações reais, cuidado com `is` (identidade) e com `float` (imprecisão).
