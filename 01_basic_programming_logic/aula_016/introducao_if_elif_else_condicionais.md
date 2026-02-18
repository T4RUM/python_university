# 🐍 Aula 16: Introdução ao if / elif / else (condicionais)

## 🎯 Objetivo da aula
Nesta aula começamos a controlar o **fluxo do programa** usando condicionais. Até agora, todo código executava linha por linha. Agora, o programa passa a **tomar decisões**.

Você vai aprender:

- O que são blocos condicionais
- Como usar `if`, `elif` e `else`
- Como organizar blocos de código corretamente
- Como tratar diferentes respostas do usuário
- Como evitar erros comuns de digitação do usuário
- Introdução ao uso de operadores lógicos em decisões

---

## 🧩 O que é uma estrutura condicional?
Uma condicional permite que o programa execute algo **somente se uma condição for verdadeira**.

Exemplo mental:

- Se chover → levo guarda-chuva.
- Senão → não levo.

O Python faz exatamente isso usando:

```python
if
elif
else
```
---
## 🔀 Como o fluxo do programa muda?
Sem condicional:
````python
print("Linha 1")
print("Linha 2")
````
Sempre executa tudo.

Com condicional:
`````python
if condição:
    executa isso
`````
O código só roda se a condição for verdadeira.

---
## 🧱 Blocos de código e indentação
Python usa indentação (recuo) para definir blocos.

````python
if condição:
    print("Está dentro do bloco")
````
Tudo que estiver com indentação pertence ao bloco.

⚠️ Sem indentação correta, o programa gera erro.

Regra prática:
- Use TAB ou 4 espaços.
- Nunca misture espaços e tabs manualmente.

---
## 🧠 Estrutura completa: if / elif / else
A estrutura básica é:
````python
if condição:
    código

elif outra_condição:
    código

else:
    código padrão
````
Fluxo:
1. Python testa o ```if```
2. Se for falso, testa o ```elif```
3. Se nenhum for verdadeiro, executa ```else```

Apenas um bloco é executado.

---
## 🧩 Por que usar .lower() na entrada?
Usuários digitam de qualquer forma:

- ```ENTRAR```
- ```entrar```
- ```Entrar```
- ```eNtRaR```

Se compararmos direto, falha.

Usando:
````python
entrada = input(...).lower()
````

Tudo vira minúsculo:
````python
ENTRAR → entrar
Entrar → entrar
````
Assim evitamos erros comuns.

🚀 Isso melhora muito a experiência do usuário.

---
## 🧩 Usando operador lógico ```!=```
Você adiciona uma melhoria excelente:

````python
entrada != 'entrar' and entrada != 'sair'
````
Isso significa:

Se não for "entrar" e não for "sair".

Ou seja, qualquer outro valor é inválido.

Isso usa operadores lógicos:

- ```!=```→ diferente de
- ```and``` → E lógico

Essa combinação é muito usada em validações.

---
## ⚠️ Armadilhas comuns
### ❌ Esquecer indentação
````python
if x == 1:
print("Erro")
````
Gera erro de sintaxe.

---

### ❌ Usar vários if quando deveria usar elif
Se usar apenas ```if```, todos podem executar.

```elif``` evita múltiplas execuções.

---

### ❌ Não tratar entrada do usuário
Usuário pode digitar qualquer coisa.

Por isso criamos uma opção inválida.

---
## 🚀 Boa prática profissional
Sempre normalize entrada do usuário:
- usar .lower()
- remover espaços com .strip() (veremos depois)
- validar respostas

Isso evita bugs e melhora UX.

----
## 🔮 O que vem nas próximas aulas?
Em breve aprenderemos:

- operadores lógicos mais avançados
- validação de dados
- repetição de perguntas até resposta válida
- tratamento de erros
- estruturas mais complexas de decisão

Ou seja, programas que não quebram com erro do usuário.

---
## 🧠 O que aprendemos nesta aula?
- O que são condicionais
- Como ```if```, ```elif``` e ```else``` funcionam
- Como blocos dependem da indentação
- Que apenas um bloco é executado
- Como normalizar texto com ```.lower()```
- Como validar opções usando ```!=``` e ```and```

---
## ✅ Resumo da aula
- ```if``` executa código se condição for verdadeira.
- ```elif``` testa novas condições.
- ```else``` é o padrão final.
- Indentação define blocos.
- ```.lower()``` evita erro de comparação.
- Operadores lógicos ajudam a validar entradas.
- Programas começam a tomar decisões.