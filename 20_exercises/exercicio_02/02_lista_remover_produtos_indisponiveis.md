# 🐍 Exercício: Removendo produtos indisponíveis do carrinho (listas)

## 🧩 Desafio
Após limpar os dados do carrinho, o sistema precisa verificar se todos os produtos ainda estão disponíveis para venda.

Em lojas online, é comum que um item fique sem estoque enquanto o cliente ainda navega no site. Nesse caso, o produto precisa ser removido automaticamente antes do fechamento do pedido.

Você recebe:

- Uma lista representando o carrinho já limpo
- Uma lista contendo os produtos que **estão disponíveis em estoque**

Seu objetivo é gerar uma nova lista contendo apenas os itens que realmente podem ser comprados.

---

## 📌 O que sua função deve fazer
Crie uma função chamada:

````python
filtrar_produtos_disponiveis(carrinho, estoque_disponivel)
````

Ela deve:

1) Receber duas listas:
   - lista de itens do carrinho
   - lista de itens disponíveis

2) Retornar uma nova lista contendo apenas produtos que existem no estoque.

3) Manter a ordem original dos itens no carrinho.

4) Não modificar nenhuma das listas recebidas.

Exemplo de comportamento:

Carrinho:

````python
["arroz", "feijao", "leite", "cafe"]
````

Estoque disponível:
````python
["arroz", "leite"]
````

Resultado:
````python
["arroz", "leite"]
````


---

## 📐 Conceitos usados
- Listas
- Laços de repetição
- Teste de pertencimento (`in`)
- Construção de lista filtrada

---

## 🧪 O que o exercício treina?
- Filtragem de dados baseada em outra coleção
- Operações comuns de validação em sistemas reais
- Uso correto de listas como filtros de dados

---

## 🚀 Desafio extra (opcional)
Retorne também uma lista com os produtos removidos do carrinho por falta de estoque.

---

## 🧠 O que aprendemos neste exercício?
- Listas podem ser usadas como filtros de dados
- Sistemas reais frequentemente validam dados antes de concluir operações
- A ordem dos dados muitas vezes precisa ser preservada

---

## ✅ Resumo do exercício
- Entrada: carrinho e lista de estoque
- Saída: nova lista apenas com produtos disponíveis
- Ordem preservada
- Nenhuma lista original deve ser alterada
