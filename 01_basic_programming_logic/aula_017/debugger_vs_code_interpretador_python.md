# 🐍 Aula 17: Debugger no PyCharm e como o interpretador lê o código

## 🎯 Objetivo da aula
Nesta aula você vai aprender a **enxergar o Python executando seu código**, linha por linha, usando o **Debugger** no **PyCharm**.

Você vai entender:
- como o interpretador “caminha” pelo código (de cima para baixo)
- como **breakpoints** pausam a execução
- como usar **Step Over / Step Into / Resume**
- como observar variáveis, expressões e o fluxo de um `if/elif/else`
---

## 🐞 Debug e “bug”
- **Bug**: erro/problema no programa.
- **Debugging (depuração)**: processo de investigar o que o programa está fazendo para encontrar a causa do bug.

🧠 O debugger não “adivinha o erro”. Ele te dá **visibilidade**: estado do programa + caminho executado.

---

## 🧩 A ideia central do Debugger
O Python normalmente executa o arquivo inteiro “direto”.

Com debug, você consegue:
- **parar** antes de uma linha executar
- avançar **uma linha por vez**
- ver os valores das variáveis **a cada passo**
- confirmar o caminho real tomado por condicionais

---

## 🛠️ Debug no PyCharm: configuração fácil (recomendado)
No PyCharm, a maneira mais simples de começar é **nem abrir a tela de configurações**.

### ✅ Passo a passo (do zero)
1) **Abra o arquivo `.py`** que você quer depurar (no editor).

2) **Crie um breakpoint**:
   - Clique na **margem esquerda** (gutter) ao lado do número da linha.
   - Vai aparecer uma **bolinha vermelha**.

3) **Inicie o Debug pelo arquivo**:
   - Clique com o **botão direito** dentro do arquivo (no editor).
   - Escolha **Debug 'nome_do_arquivo'**.

4) O PyCharm vai automaticamente:
   - criar uma **Run/Debug Configuration temporária**
   - abrir a janela de **Debug**
   - **parar no breakpoint** quando o interpretador chegar naquela linha

✅ Pronto. Você já está depurando sem configurar nada manualmente.

---

## 🧩 Run/Debug Configurations (o que é, sem complicar)
O PyCharm trabalha com **Run/Debug Configurations** para definir:
- qual arquivo rodar
- qual interpretador usar
- argumentos
- diretório de execução

✅ Mas o importante aqui é: **você não precisa criar isso agora**, porque o PyCharm cria uma configuração temporária automaticamente quando você escolhe “Debug”.

📌 Mais pra frente, quando você quiser passar argumentos, rodar scripts específicos ou organizar projetos maiores, aí sim faz sentido configurar manualmente.

---

## 🧱 Breakpoint
**Breakpoint** é um marcador que diz:

> “Antes de executar esta linha, pause aqui.”

✅ Boas práticas para breakpoints:
- coloque antes do trecho “suspeito”
- coloque no começo de um `if/elif/else` para ver qual caminho será tomado
- evite breakpoints em linhas que não executam (comentários, linhas vazias)

---

## 🧭 Botões essenciais do Debugger (o que você realmente usa)
Quando o programa pausar no breakpoint, você vai usar principalmente:

- ▶️ **Resume Program**: continua até o próximo breakpoint (ou até terminar).
- ↷ **Step Over**: executa a linha atual e vai para a próxima (o mais usado).
- ↓ **Step Into**: entra numa chamada (quando houver) para ver por dentro.
- ⏹ **Stop**: encerra a depuração.

📌 Na janela de Debug, você também vai ver:
- **Variables**: variáveis e valores atuais
- **Frames/Call Stack**: onde o programa está executando
- **Console**: saída do programa
- **Watches**: expressões que você quer acompanhar (opcional)

---

## 🧪 Watches e Evaluate Expression
Quando você quiser entender uma condição em tempo real (ex.: `condicao_1 and condicao_2`), você pode:

- **Evaluate Expression**: testar uma expressão na hora.
- **Watches**: manter expressões “fixas” monitoradas enquanto você dá Step Over.

🚀 Dica profissional: coloque Watches para condições do `if/elif/else`. Ajuda muito a “enxergar” a lógica.

---

## 🧠 O interpretador e o `if/elif/else` na prática
O interpretador:
- executa de cima para baixo
- quando encontra `if/elif/else`, avalia condições em ordem
- **no primeiro bloco verdadeiro**, ele executa o bloco e **pula o resto do encadeamento**

✅ Consequência importante:
- em `if/elif/else`, **apenas um bloco executa**
- em vários `if` separados, **mais de um pode executar**

---

## 🧷 Superpoder do Debug: mudar valores durante a execução
Quando o programa está pausado, você pode:
- inspecionar variáveis
- **alterar valores** para simular cenários diferentes
- continuar e ver o fluxo mudar

⚠️ Isso é incrível para aprender e testar rapidamente. Mas em código real, a correção final sempre é no código (não “na variável do debug”).

---

## ⚠️ Armadilhas comuns ao debugar
### ⚠️ Breakpoint no lugar errado
Se o trecho nunca executa, o debugger nunca para.

✅ Solução: coloque breakpoint em linhas que você tem certeza que serão alcançadas.

### ⚠️ Confundir Resume com Step Over
- **Resume** corre até o próximo breakpoint
- **Step Over** é “lupa”: linha por linha

✅ Solução: use Step Over para entender o fluxo.

### ⚠️ Achar que o debugger “conserta”
O debugger é um raio-x. Quem corrige é você.

---

## 🧠 O que aprendemos nesta aula?
- O que é debug e por que ele existe.
- Como o breakpoint pausa o interpretador antes de uma linha executar.
- Como iniciar o debug no PyCharm do jeito mais simples (sem configurar nada).
- Como usar Step Over / Resume para enxergar o fluxo real do programa.
- Como `if/elif/else` escolhe apenas um caminho e pula os demais.
- Como observar variáveis para entender o estado do programa.

## ✅ Resumo da aula
- Debug é depuração: ver o programa executando passo a passo.
- Breakpoint é o ponto de parada.
- No PyCharm, o jeito mais fácil é: **breakpoint → botão direito → Debug arquivo**.
- Step Over avança linha a linha; Resume corre até o próximo breakpoint.
- `if/elif/else` executa só o primeiro bloco verdadeiro.
- Variáveis e Watches ajudam a enxergar o estado do programa.
