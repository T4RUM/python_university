# 🐍 Exercício: Relatório de vendas do dia (listas)

## 🧩 Desafio
Você trabalha em um sistema que recebe todas as vendas realizadas durante o dia.

Cada venda contém:
````python
(nome_do_produto, quantidade, preco_unitario)
````

O gestor deseja saber quanto foi vendido no total em dinheiro.

Seu objetivo é calcular o valor total faturado.

---

## 📌 O que sua função deve fazer
Crie uma função:
````python
calcular_total_vendas(vendas)
````

Ela deve:

1) Receber uma lista de vendas.
2) Cada venda é uma tupla contendo:
   - produto
   - quantidade vendida
   - preço unitário
3) Calcular o valor total do faturamento.
4) Retornar o valor final.

Exemplo:

Entrada:
````python
[
("arroz", 2, 25.0),
("leite", 3, 8.5)
]
````

Saída:
````python
75.5
````

---

## 📐 Conceitos usados
- Listas contendo tuplas
- Iteração
- Acumuladores
- Operações matemáticas básicas

---

## 🧪 O que o exercício treina?
- Processamento de dados estruturados
- Uso de acumuladores
- Simulação de relatórios reais de vendas

---

## 🚀 Desafio extra (opcional)
Retorne também o produto que mais gerou faturamento no dia.

---

## 🧠 O que aprendemos neste exercício?
- Listas podem representar registros reais
- Relatórios são operações comuns em sistemas
- Processamento de dados é base para análises

---

## ✅ Resumo do exercício
- Entrada: lista de vendas
- Saída: valor total faturado
- Uso de acumulador para soma final
