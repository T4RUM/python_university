# 🐍 Aula 15: Coletando dados do usuário com `input()`

## 🎯 Objetivo da aula
Nesta aula você vai aprender a **pausar o programa e pedir dados ao usuário** usando `input()`, entender **o que essa função realmente retorna** (sempre `str`) e por que a conversão de tipos (ex: `int(...)`) vira necessária quando queremos fazer contas.

---

## 🧩 O que é `input()`?
`input()` é uma **função embutida do Python** (built-in) que:

- mostra um texto (opcional) para o usuário (o “prompt”)
- **pausa o programa**
- espera o usuário digitar algo e pressionar **Enter**
- devolve o que foi digitado **como string (`str`)**

✅ Importante: o texto do prompt é só uma “pergunta” exibida no terminal. O que entra no código é **o retorno do `input()`**.

---

## 🖥️ Onde `input()` funciona?
`input()` funciona em um ambiente que permite entrada interativa.

✅ Funciona:
- Terminal (Prompt/PowerShell)
- Terminal do VS Code
- Terminal do Linux/Mac

⚠️ Pode não funcionar como esperado:
- “Output” read-only (por exemplo: algumas configurações do Code Runner)

**Regra prática:** se o cursor não está te esperando digitar, você não está em um terminal interativo.

---

## 🧠 O retorno do `input()` é sempre `str`
Mesmo que o usuário digite `10`, o Python recebe `"10"`.

🧩 Isso explica um comportamento clássico:

- `input()` → `"1"` e `"5"`
- `"1" + "5"` → `"15"` (concatenação)

✅ Ou seja: o `+` com strings junta textos, não faz soma numérica.

---

## ✅ Convertendo para número (coerção / type casting)
Se você quer somar números, precisa converter:

- `int("10")` → `10` (inteiro)
- `float("1.5")` → `1.5` (ponto flutuante)

✅ Após converter, o `+` vira soma de verdade.

---

## ⚠️ Armadilha importante: converter “cedo demais” pode atrapalhar
É tentador fazer tudo numa linha:

```py
n = int(input("Digite um número: "))
```

Funciona… até o usuário digitar algo inválido (ex: "a", "10.5" para int, vazio, espaços…).

⚠️ Quando a conversão falha, o Python levanta ValueError e o programa para exatamente naquela linha.

---
## ✅ Boas práticas profissionais (sem tratar erro ainda)
Mesmo antes de aprender tratamento de erros, você já pode estruturar melhor:

- guarde primeiro o que o usuário digitou (string)
- depois converta para um novo nome

### ✅ Isso é mais organizado e abre espaço para validação depois:
- primeiro_numero_str → o texto original
- primeiro_numero → o inteiro convertido

Essa separação deixa claro:

- o que veio do usuário (texto)
- o que o programa validou/convertiu (número)
---
## 🧪 “Truque” útil: nome=
Em f-strings existe um recurso ótimo para depurar (ver valores):
````python
print(f"{nome=}")
````
✅ Isso imprime o nome da variável e o valor automaticamente, útil para acompanhar o que está acontecendo no programa enquanto você aprende.

---
## 🔮 Introdução: como vamos evitar erros mais pra frente?
Ainda não é o momento de tratar erros “de verdade”, mas é importante entender o que vem aí.

Nas próximas aulas, você vai aprender formas de lidar com entrada inválida, como:

- validar antes de converter (ex: checar se parece número)
- repetir a pergunta até o usuário digitar corretamente
- usar try/except para capturar ValueError sem derrubar o programa

🧠 Pense nisso como “programas que não quebram quando o usuário erra”.

---
## 🧠 O que aprendemos nesta aula?
- ```input()``` pausa o programa e espera o usuário digitar.
- Tudo que vem do ```input()``` chega como ```str```.
- Somar strings concatena`````("1" + "5" = "15")```, não soma.
- Para somar números, precisamos converter (```int```, ```float```).
- Converter “cedo demais” pode derrubar o programa se a entrada for inválida.
- Separar ```texto_digitado``` e ```valor_convertido``` é uma prática melhor.
- ```f"{variavel=}"``` ajuda a enxergar rapidamente valores no código.

---
## ✅ Resumo da aula
- Use input("pergunta: ") para coletar dados do usuário.
- Lembre sempre: entrada do usuário é string.
- Faça conversão quando precisar de número.
- Prefira separar o valor digitado (string) do valor convertido (int/float).
- Tratamento de erro ainda não, mas já sabemos por que ele vai ser necessário.