# 🐍 Exercício: Checagem de carrinho (listas)

## 🧩 Desafio
Você está implementando uma etapa simples de validação para um **carrinho de compras** (e-commerce).

O carrinho é representado por uma **lista de strings**, onde cada string é o nome do produto digitado (ou capturado) pelo sistema.

Na prática, essa lista pode vir “bagunçada”:
- pode conter itens com espaços extras (ex.: `"  arroz  "`)
- pode conter letras maiúsculas e minúsculas misturadas (ex.: `"Feijao"`, `"feijao"`)
- pode conter entradas vazias (ex.: `""` ou `"   "`)
- pode conter itens repetidos (ex.: `"leite"` aparece duas vezes)

Seu objetivo é criar uma função que produza uma versão **limpa e padronizada** do carrinho para que as próximas etapas do sistema (checkout, cálculo de frete, estoque) funcionem corretamente.

### O que sua função deve fazer
Crie uma função chamada `limpar_carrinho(itens)` que recebe uma lista de strings e retorna **uma nova lista** com as seguintes regras:

1) Remover espaços no início e no fim de cada item (`strip`)  
2) Converter tudo para **minúsculas**  
3) Remover itens vazios (ex.: `""`, `"   "`)  
4) Manter a **ordem original** dos itens válidos  
5) **Não remover duplicados ainda** (neste exercício, repetição é permitida)

Exemplo (somente para entendimento do comportamento — não é para copiar como solução pronta):
- Entrada: `["  Arroz  ", "Feijao", "   ", "", "Leite", "leite"]`
- Saída esperada: `["arroz", "feijao", "leite", "leite"]`

> Importante: você não deve alterar a lista original recebida. Retorne uma nova lista.

---

## 📐 Conceitos usados
- Listas e iteração (`for`)
- Strings: `strip()` e `lower()`
- Condições (`if`) para filtrar itens vazios
- Criação de uma nova lista (evitar efeitos colaterais)

---

## 🧪 O que o exercício treina?
- Limpeza de dados (“data cleaning”) comum em sistemas reais
- Padronização de entradas do usuário
- Construção de listas filtradas
- Boas práticas: não modificar parâmetros diretamente

---

## 🚀 Desafio extra (opcional)
Crie uma segunda função chamada `contar_itens(itens_limpos)` que receba a lista limpa e retorne:
- um dicionário `{item: quantidade}` com a contagem de cada produto no carrinho

*(Essa parte é opcional e prepara o terreno para dicionários no próximo exercício.)*

---

## 🧠 O que aprendemos neste exercício?
- Uma lista pode representar dados reais de um sistema
- Antes de processar dados, é comum padronizar texto (caixa e espaços)
- Filtrar entradas vazias evita bugs em etapas posteriores

---

## ✅ Resumo do exercício
- Entrada: lista de strings (itens do carrinho)
- Saída: nova lista com itens **strip + lower**, sem vazios e mantendo a ordem
- Não remover repetidos ainda
