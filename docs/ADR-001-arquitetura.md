# ADR-001 — Escolha da Arquitetura

## Contexto

O sistema atual apresenta uma estrutura simples, porém com diversos problemas de organização. 
As funcionalidades estão concentradas em um único arquivo, o que dificulta a manutenção.

Os requisitos não funcionais indicam que:
- RNF03: o sistema deve ser fácil de modificar
- RNF04: deve ser possível testar as regras de forma isolada

No modelo atual, essas condições não são atendidas.

---

## Opções consideradas

Foram analisadas três possibilidades de organização:

### Arquivo único
- Fácil de começar
- Difícil de manter com o crescimento do sistema
- Mistura várias responsabilidades

### Arquitetura em camadas
- Divide o sistema em partes com funções específicas
- Facilita manutenção e testes
- Organiza melhor o código

### MVC
- Estrutura bem conhecida
- Mais complexo para implementar
- Pode ser exagero para aplicações simples

---

## Decisão

Foi escolhida a arquitetura em camadas por ser mais adequada ao tamanho e complexidade do sistema.

As camadas definidas são:
- domain: responsável pelas regras de negócio
- service: coordena o funcionamento do sistema
- data: gerencia os dados
- ui: interface com o usuário

---

## Consequências

- O sistema ficará mais organizado
- Será mais fácil identificar erros
- A manutenção será simplificada
- Possibilita testes mais eficientes
