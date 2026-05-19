# Problemas Identificados — Leitura Inicial do Código

Este arquivo é preenchido pelos estudantes na Aula 1 após a leitura do código legado.
Descreva em linguagem livre tudo que parecer estranho, errado ou difícil de entender.
Não é necessário usar termos técnicos neste momento.

---

## Minha leitura inicial

- O código parece concentrar muitas responsabilidades no mesmo lugar
- Existe dependência de variáveis globais
- Algumas partes parecem difíceis de testar separadamente
- A lógica do sistema e a interface estão misturadas
- Não está claro onde cada funcionalidade deveria ficar
- Há repetição de algumas ideias no código
- O sistema não parece preparado para crescer facilmente

---

## Revisão com vocabulário técnico

- O sistema apresentava baixa coesão, pois diferentes responsabilidades estavam concentradas no mesmo arquivo.

- Existia alto acoplamento entre os componentes do sistema, dificultando manutenção e reutilização.

- O código violava o princípio SRP, já que múltiplas responsabilidades estavam reunidas no mesmo módulo.

- A ausência de separação em camadas dificultava evolução do projeto.

- O sistema misturava regras de negócio com interação de interface.

- O modelo inicial dificultava testes isolados, contrariando o requisito RNF04.

- A estrutura em arquivo único dificultava modificações futuras, contrariando o requisito RNF03.

- O código apresentava características de dívida técnica relacionadas à organização e escalabilidade.
