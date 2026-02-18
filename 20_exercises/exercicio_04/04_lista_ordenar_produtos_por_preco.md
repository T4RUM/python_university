# 🐍 Exercício: Ordenando produtos por preço (listas)

## 🧩 Desafio
Você está trabalhando na página de resultados de busca de um e-commerce.

O sistema recebe uma lista de produtos, onde cada item é representado por:

````python
(nome_do_produto, preco)
````

Seu objetivo é ordenar os produtos pelo preço para exibir primeiro os mais baratos.

---

## 📌 O que sua função deve fazer
Crie uma função:
````python
ordenar_por_preco(produtos)
````

Ela deve:

1) Receber uma lista de tuplas `(produto, preco)`
2) Retornar uma nova lista ordenada pelo preço crescente
3) Não alterar a lista original

Exemplo:

Entrada:
````python
[("arroz", 25.0), ("leite", 8.5), ("cafe", 15.0)]
````

Saída:
````python
[("leite", 8.5), ("cafe", 15.0), ("arroz", 25.0)]
````

---

## 📐 Conceitos usados
- Listas de tuplas
- Função `sorted`
- Ordenação por chave (`key`)

---

## 🧪 O que o exercício treina?
- Ordenação de dados
- Manipulação de listas com estruturas internas
- Preparação de dados para interface

---

## 🚀 Desafio extra (opcional)
Permita ordenar também do maior para o menor.

---

## 🧠 O que aprendemos neste exercício?
- Listas podem conter estruturas complexas
- Ordenação é fundamental em aplicações reais
- Dados frequentemente precisam ser preparados para exibição

---

## ✅ Resumo do exercício
- Entrada: lista de produtos e preços
- Saída: lista ordenada por preço
- Lista original permanece intacta

