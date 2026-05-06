# Resenha Aula 3 — Modelagem e Design de Software  
**Aluno:** JOAO VICTOR PORTILHO SANTOS 
**Data:** 29/04/2026  

---

## Questão 1 — Modelos UML como ferramentas de modelagem  

### (a) Estrutura × comportamento  

Quando se fala em UML, é importante entender que nenhum diagrama sozinho consegue representar todo o sistema. Cada tipo de diagrama tem um foco específico.  

O diagrama de classes, por exemplo, é mais voltado para a organização interna do sistema. Ele mostra quais são os elementos principais, como eles se relacionam e quais dados estão envolvidos. Porém, ele não mostra o que acontece durante a execução do programa.  

Já o diagrama de sequência tem uma proposta diferente. Ele mostra como os objetos interagem ao longo do tempo, destacando a ordem das ações. Isso ajuda a entender o comportamento do sistema, mas não revela toda a sua estrutura.  

Como discutido por Valente, diferentes representações são necessárias porque cada uma evidencia um aspecto específico. Por isso, é comum utilizar mais de um tipo de diagrama para ter uma visão mais completa.  

---

### (b) Consequência prática  

Essa diferença entre os diagramas influencia diretamente no desenvolvimento. O diagrama de classes ajuda a pensar na organização do sistema, enquanto o de sequência auxilia na compreensão de como as funcionalidades realmente acontecem.  

Na prática, isso significa que um desenvolvedor pode usar o diagrama de classes para estruturar o sistema e o de sequência para validar o fluxo das operações.  

Segundo Valente, escolher bem as representações é importante porque elas orientam o raciocínio durante o desenvolvimento.  

---

### (c) Aplicação ao UC01  

No caso do UC01 (Registrar Empréstimo), o uso de um diagrama de sequência tornaria o processo mais claro. Ele permitiria visualizar quais partes do sistema estão envolvidas e em que ordem as ações acontecem.  

Seria possível identificar, por exemplo, a verificação de disponibilidade, o registro do empréstimo e outras etapas do processo. Isso ajuda a entender melhor o funcionamento do sistema, algo que não fica totalmente evidente apenas com a descrição textual.  

---

## Questão 2 — Arquitetura, design e os princípios de decomposição  

### (a) Definições  

Coesão está relacionada com o nível de organização interna de um módulo. Um módulo com alta coesão executa funções que fazem sentido juntas.  

Acoplamento representa o grau de dependência entre diferentes partes do sistema. Quanto maior essa dependência, mais difícil se torna realizar mudanças.  

O ocultamento de informação tem como objetivo esconder detalhes internos e expor apenas o necessário, evitando que outras partes do sistema dependam da implementação.  

De acordo com Valente, esses conceitos são fundamentais para criar sistemas mais bem estruturados.  

---

### (b) Relações entre os princípios  

Esses princípios não funcionam isoladamente. Quando o ocultamento de informação é bem aplicado, o acoplamento tende a diminuir, já que os módulos ficam mais independentes.  

Além disso, a coesão contribui para uma melhor organização, facilitando o entendimento do sistema.  

Valente destaca que um bom design busca equilibrar esses fatores, garantindo que o sistema seja ao mesmo tempo organizado e flexível.  

---

### (c) Aplicação ao projeto v2.0  

No projeto desenvolvido, a divisão em camadas mostra uma tentativa de aplicar esses conceitos. Cada camada possui uma função específica, o que melhora a organização.  

A camada **domain** concentra a lógica principal, enquanto a **service** organiza o fluxo das operações. A camada **data** cuida dos dados e a **ui** da interação com o usuário.  

Essa separação reduz a dependência entre partes do sistema e facilita futuras modificações, o que está alinhado com os princípios apresentados por Valente.  

---

## Questão 3 — Crítica fundamentada à documentação do sistema legado  

### (a) Pontos frágeis  

Ao analisar o sistema, é possível perceber alguns problemas claros. Um deles é o uso de variáveis globais, que aumenta a dependência entre diferentes partes do código.  

Outro ponto é a falta de divisão das responsabilidades. Como tudo está em um único arquivo, o sistema acaba ficando desorganizado e difícil de entender.  

Segundo Valente, esse tipo de estrutura dificulta a manutenção e evolução do software.  

---

### (b) Ponto forte  

Apesar dos problemas, a documentação apresenta um aspecto positivo: o reconhecimento da dívida técnica. Isso mostra que existe consciência sobre as limitações do sistema.  

---

### (c) Síntese  

Mesmo com falhas estruturais, o fato de identificar os problemas já é um passo importante. Isso permite que o sistema evolua de forma mais planejada.  

Seguindo os conceitos apresentados por Valente, é possível reorganizar o sistema para torná-lo mais modular e fácil de manter.  

---

## Questão 4 — Tipos como contratos: dicionários × classes  

### (a) Prevenção de erros  

O uso de dicionários pode gerar erros simples, como chaves incorretas ou ausência de dados. Esses problemas costumam aparecer apenas em tempo de execução.  

Já as classes permitem uma definição mais clara da estrutura dos dados, reduzindo a chance de erros.  

---

### (b) Capacidade de evolução  

As classes oferecem maior flexibilidade para evolução do sistema, pois permitem adicionar novos comportamentos sem alterar toda a estrutura.  

Dicionários, por outro lado, são mais limitados nesse sentido.  

---

### (c) Comunicação do design  

Classes ajudam a representar melhor os conceitos do sistema, tornando o código mais compreensível.  

Como Valente aponta, um bom design também depende da clareza com que o sistema é representado, e o uso de classes contribui para isso.  
