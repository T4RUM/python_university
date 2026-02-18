# 🐍 Aula 14: Formatação de strings com `str.format()`

## 🎯 Por que isso importa?
Em Python, *montar textos com variáveis* é uma das tarefas mais frequentes: mensagens de log, relatórios, telas, geração de arquivos, etc.

Nesta aula você vai dominar o **`str.format()`**, uma forma poderosa (e ainda muito usada) de formatar strings e entender quando ele é útil mesmo hoje, com f-strings.

---

## 🧩 O que é `str.format()`?
`format()` é um **método** de `str` (string).  
Isso significa: ele é uma “ação” disponível em qualquer string.

✅ A ideia é simples:
- você escreve uma string com **marcadores** (placeholders)
- e entrega valores para preencher esses marcadores

Os marcadores ficam dentro de `{ }`.

---

## 🧠 Marcadores: 3 formas de preencher

### 1) 🧷 Por ordem (posicional implícito)
Quando você usa `{}` sem nada dentro, o preenchimento acontece **na ordem dos argumentos** passados.

✅ Bom para casos rápidos, mas pode ficar confuso quando a string cresce.

---

### 2) 🔢 Por índice (posicional explícito)
Você pode usar `{0}`, `{1}`, `{2}`… para decidir exatamente qual valor vai em cada lugar.

✅ Vantagens:
- você pode **repetir** o mesmo valor várias vezes
- você não fica “refém” da ordem

🚀 Dica profissional: índices são úteis, mas **nomes costumam ser mais legíveis** em código real.

---

### 3) 🏷️ Por nome (placeholders nomeados)
Você escreve `{nome}` e passa `nome=valor` no `format()`.

✅ Isso deixa o texto muito mais claro, principalmente em mensagens longas:
- `{usuario}`
- `{saldo:.2f}`
- `{data}`

🧠 Em código profissional, placeholders nomeados geralmente vencem por legibilidade.

---

## 🎛️ Format spec: controlar números, alinhamento e mais
Dentro das chaves você pode usar:

`{variavel:especificacao}`

Exemplo comum:
- `:.2f` → **2 casas decimais** (float)
- `:,` → separador de milhar
- `>10` / `<10` / `^10` → alinhamento e largura
- `0` + largura → preenchimento com zeros (ex: `05d`)

✅ Isso faz `format()` ser ótimo para:
- relatórios alinhados
- tabelas simples no terminal
- valores monetários
- logs padronizados

---

## ⚠️ Armadilhas comuns (e como evitar)

### ⚠️ 1) Chaves demais (ou valores de menos)
Se você pede 4 placeholders e passa 3 valores, aparece erro de índice.

✅ Solução: conte placeholders e valores, ou prefira placeholders nomeados.

---

### ⚠️ 2) Misturar posicional com nomeado do jeito errado
No `format()`, existe uma regra importante:

✅ **argumentos posicionais vêm antes de nomeados** na chamada.

Exemplo do que dá erro:
- `format(nome="Ana", 10)` ❌

✅ Faça:
- `format(10, nome="Ana")` ✅  
ou use tudo nomeado.

---

### ⚠️ 3) Nome errado gera `KeyError`
Se a string tem `{cliente}` e você passa `format(usuario="...")`, dá erro.

✅ Solução: mantenha os nomes consistentes e, se possível, use um padrão de nomes.

---

### ⚠️ 4) Esquecer que `{` e `}` são especiais
Se você precisa escrever chaves literais no texto, escape duplicando:

✅ `{{` vira `{`  
✅ `}}` vira `}`

Isso é super comum ao gerar JSON, templates e exemplos de código.

---

## 🚀 Quando usar `format()` vs f-string?
Hoje, em Python moderno:

✅ **f-strings** costumam ser a primeira escolha:
- mais curtas
- mais legíveis
- mais rápidas

Mas `format()` ainda é excelente quando:
- você tem um **template** pronto e quer preencher depois
- você quer reutilizar uma string padrão em vários lugares
- você quer passar dados dinamicamente (ex: dicionário)
- você precisa compatibilidade com versões antigas (legado)

---

## 🧠 O que aprendemos nesta aula?
- Que `format()` é um método de string usado para preencher `{}`.
- Três formas de placeholders: por ordem, por índice e por nome.
- Como formatar floats com `:.2f` e aplicar outras especificações.
- Erros comuns: placeholders a mais, nomes errados, mistura de argumentos.
- Como escrever chaves literais com `{{` e `}}`.
- Quando `format()` faz mais sentido do que f-strings.

## ✅ Resumo da aula
- Use `{}` + `format(...)` para montar textos com variáveis.
- Prefira **placeholders nomeados** em strings maiores.
- Use `:...` para controlar apresentação (decimais, alinhamento, milhar).
- Se aparecer erro “fora do range” (índice), você pediu mais placeholders do que valores.
- `format()` continua útil em templates e cenários dinâmicos, mesmo com f-strings.
