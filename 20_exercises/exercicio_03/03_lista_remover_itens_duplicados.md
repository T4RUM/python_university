# 🐍 Exercício: Removendo itens duplicados do carrinho (listas)

## 🧩 Desafio
Após a validação do estoque, o time decide oferecer uma visualização simplificada do carrinho, exibindo apenas **um item por produto**, sem repetições.

Por exemplo, se o cliente adicionou o mesmo item várias vezes, o sistema exibirá apenas um registro visual, mas o cálculo de quantidade continuará sendo feito em outra etapa.

Seu objetivo é criar uma lista sem itens duplicados, preservando a ordem original.

---

## 📌 O que sua função deve fazer
Crie uma função:

````python
remover_duplicados(carrinho)
````

Ela deve:

1) Receber uma lista de produtos.
2) Retornar uma nova lista sem itens repetidos.
3) Manter a primeira ocorrência de cada item.
4) Não modificar a lista original.

Exemplo:

Entrada:
````python
["arroz", "leite", "arroz", "cafe", "leite"]
````

Saída:
````python
["arroz", "leite", "cafe"]
````

---

## 📐 Conceitos usados
- Listas
- Controle manual de duplicação
- Verificação de pertencimento
- Criação de lista auxiliar

---

## 🧪 O que o exercício treina?
- Remoção de duplicatas
- Controle de inserção condicional em listas
- Pensamento de fluxo de dados

---

## 🚀 Desafio extra (opcional)
Faça uma versão que também retorne quantos itens foram removidos.

---

## 🧠 O que aprendemos neste exercício?
- Listas não evitam duplicatas automaticamente
- Muitas vezes precisamos controlar manualmente o que entra na coleção
- Ordem dos dados pode ser importante

---

## ✅ Resumo do exercício
- Entrada: lista com possíveis duplicados
- Saída: nova lista sem repetições
- Ordem mantida
