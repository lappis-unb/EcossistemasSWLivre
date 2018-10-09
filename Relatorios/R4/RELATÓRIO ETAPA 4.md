---
title: RELATÓRIO DE CUMPRIMENTO DO OBJETO ETAPA III - Ecossistemas de Software Livre - Agosto 2018
author: Carla Silva Rocha Aguiar (Coordenadora do Projeto)
date: 08 de outubro de 2018
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
colorlinks: true
---

# Introdução

O presente relatório apresenta o acompanhamento do trabalho realizado no
projeto "Ecossistemas de Software Livre", Termo de Cooperação para
Descentralização de Crédito, Processo Ofício No 0646/2017/FUB-UnB, Vigência
Outubro 2017 à Outubro 2019. O relatório apresentado é referente aos avanços
realizados na Etapa III (Julho 2018 à Setembro 2018), de acordo com o cronograma
do Plano de Trabalho.

Toda alteração no cronograma proposto foi realizada  a partir de renegociação
com a CGTEC do Ministério da Cultura, e tais alterações estão descritas no
relatório.

## FASE DE PLANEJAMENTO/EXECUÇÃO

O período de Abril 2018 à Junho de 2018 contemplou as fases de
planejamento e execução. Abaixo serão apresentados, brevemente, os principais
avanços alcançados no período. Toda a documentação e acompanhamento do projeto
está disponibilizado e pode ser acessado na organização do laboratório
[lappis-unb](https://github.com/lappis-unb), e no
repositório específico do projeto
[lappis-unb/EcossistemasSWLivre](https://github.com/lappis-unb/EcossistemasSWLivre).
Todo o planejamento e execução das tarefas podem ser acompanhados tanto nas
_issues_ quanto nas páginas _wiki_.


Abaixo serão apresentados os principais avanços alcançados no período, por
pacote de trabalho de acordo com o Plano de Trabalho
e cronograma.

### Legado em Software Livre <!-- {{{ -->

As macro atividades referentes a essa etapa de acordo com o cronograma do plano de trabalho são:

- [x] Realizar Estudo de Refatoração em software legado
- [x] Realizar Estudos sobre práticas de DevOps aplicada a software legado

Durante a primeira etapa do projeto foi priorizado a visão "legacy in the box" (legado em uma caixa, tradução literal), no qual o foco foi isolar alguns projetos mantidos pelo Ministério da Cultura por meio de Docker[^docker]. Essa solução gera o benefício de criar ambientes de desenvolvimento e produção estáveis, fazendo com que diminua o tempo de configuração de ambiente. Essa abordagem traz um grande benefício pois possibilita o uso de práticas DevOps mesmo em sistemas legados. Esse modelo de isolar pacotes de software legados através de containers Docker possibilita um pipeline de entrega contínua, deploy contínuo, e diminui a fronteira entre a equipe de infraestrutura e equipe de desenvolvimento.

[^docker]: Docker fornece uma camada adicional de abstração e automação de virtualização de nível de sistema operacional. [http://www.docker.com](http://www.docker.com)

Na segunda etapa do projeto, usamos uma segunda forma de lidar com software legado, sempre com o intuito de aplicar técnicas modernas de Engenharia de Software e padrões de comunidade de software livre, a fim de viabilizar o uso desses projetos legados em outros contextos e em pipelines automatizados. O foco então foi transformar um software legado em software livre, a partir de técnicas de refatoração de código, e suite de testes automatizados. Foi escolhido a API do Salic como estudo de caso, uma vez que esse é um sistema relativamente pequeno, de grande relevância e impacto no ecossistema Salic.

As ações realizadas  na terceira etapa (referente ao presente relatório) para atender os objetivos do plano de trabalho foram:

- [x] Homologar a API do Salic no ambiente do MinC;
- [x] Estudo de estratégias possíveis para a implementação de novas funcionalidades em um sistema legado/monolítico;
- [x] Proposta de uma estratégia pra implementação de novas funcionalidades no SALIC (Estudo de caso).

A terceira etapa do projeto teve como objetivo inserir o software refatorado na etapa passada em um pipeline de entrega e deploy contínua. Após uma homologação interna na própria infraestrutura do laboratório LAPPIS, realizada na etapa anterior, foi realizada a entrega técnica ao ministério, no qual foi apresentada a estratégia de refatoração e a versão inicial da API do Salic. A API foi então homolagada na infraestrutura do Ministério da Cultura. Foi configurado um pipeline de deploy/entrega contínua, no qual toda a mudança no código da API passa por um pipeline no Gitlab-CI automatizado até um ambiente de homologação no MinC. Todo o pipeline pode ser acompanhado em [https://github.com/lappis-unb/salic-api](https://github.com/lappis-unb/salic-api).

Nessa etapa também teve como objetivo principal a realização de uma pesquisa teórica e prática sobre alternativas para lidar com sistemas legados para a adição de novas funcionalidades. Foram estudadas duas possíveis abordagens: (a) adição de novas funcionalidades mantendo a arquitetura monolítica (b) adição de novas funcionalidades utilizando o modelo arquitetural microserviços.

Uma primeira estratégia é manter um repositório e sistema monolítico, somente acrescentando novas funcionalidades respeitando boas práticas de software  (qualidade de software, testes unitários, testes de aceitação, etc). Dentre as vantagens dessa abordagem estão:

- **Centralização**: toda a base de código é contido em um único repositório com suas diversas funcionalidades;
- **Visibilidade**: código é visível e pesquisável por todos os engenheiros da organização e contribuidores externos;
- **Sincronização**: o processo de desenvolvimento é orientado a branches, e colaboradores contribuem para branches especificas no repositório;
- **Completude**: qualquer projeto/funcionalidade do repositório pode ser compilado a partir das dependências presentes no próprio repositório. Dependências são versionadas, projetos  devem usar a versão de suas dependências no repositório;
- **Padronização**: um conjunto de ferramentas compartilhadas governam como colaboradores interagem com o código, incluindo testes, pesquisa e revisão de código.

Uma segunda estratégia é adotar uma arquitetura de microserviços, no qual a componentização de novas funcionalidades é feita por meio de serviços. Microserviços  são componentes executados de forma independente (out-of-process), que comunicam entre si com mecanismos como requisição de serviço web, ou chamadas de processos remotos. Uma das principais razões de usar serviços como componentes é que serviços são disponibizados (deploy) de forma independente. Se uma aplicação monolítica (executando apenas um processo) alterar um único componente, isso resulta na necessidade de realizar o deploy de toda a aplicação. Dentre as vantagens dessa abordagens estão:

- **Serviços organizados como capabilidade de negócio**: cada serviço é responsável por uma capabilidade do negócio, e é desenvolvida full stack (do design, requisitos, implementação, implantação). Mais próximo ao movimento DevOps;
- **Produtos, não projetos**: time é responsável por todo o ciclo de vida do produto, do projeto à implantação;
- **Endpoints inteligentes**: Comunicação entre microserviços tende a ser altamente desacoplados e altamente coesos. Protocolos mais utilizados HTTP, protocolos RESTful;
- **Governança Descentralizada**: decisões técnicas e negociais são realizadas localmente, dependendo da necessidade de cada microserviço;
- **Gestão de dados descentralizados**: cada microserviço gerencia seu próprio banco de dados e lógica de armazenamento;
- **Automação da Infraestrutura**:  todo o pipeline de deploy e entrega contínuos pode ser feito de forma automatizada, filtrada por meio de testes realizados em vários estágios do pipeline;
- **Projetado para falhas**: aplicações são projetadas para serem tolerantes à falha de serviços;
- **Design Evolutivo**: a aplicação pode ser evoluida gradativamente e contiuamente, ao contrário de arquitetura componentizada que requer um projeto de como as funcionalidades serão dividas em componentes.

A arquitetura microserviço é um padrão dos sistemas de software modernos, e tem se tornado um padrão nas grandes empresas.  Após essa revisão literária e  revisão técnica sobre possíveis soluções arquiteturais para lidar com a adição de novas funcionalidades optamos por abordar a solução via arquitetura microserviços. Como estudo de caso, optamos por utilizar as funcionalidades desenvolvidas no pacote de trabalho "aprendizagem de máquina" que serão integradas ao Salic. Ou seja, as funcionalidades de aprendizagem de máquina que serão integradas ao Salic vão ser implementadas como microserviços. A próxima etapa do projeto essa abordagem de tratar com sistemas legados será implementado, colocado em ambiente de homologação/produção, e avaliado.

<!-- }}} -->

### Práticas de gestão colaborativa <!-- {{{ -->

O objetivo de estudar os movimentos, organizações, desenvolvedores e demais stakeholders que atuam na gestão colaborativa de software livre é manter um conjunto de ações de governança digital e comunicação que aproveite ao máximo esse potencial em favor das necessidades do órgão e das metas comuns às organizações parte das comunidades. Esse esforço envolve um trabalho de mapeamento de atores de cada comunidade (atuais e potenciais futuros), assessoria para planejamento conjunto, facilitação de fluxos de comunicação e mobilização, realização de atividades conjuntas para integração, identificação de oportunidades externas, assessoria para comunicação e divulgação ao público externo à comunidade e apoio para solução de conflitos.

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Identificar grupos de opinião.

As ações realizadas  nesta etapa para atender os objetivos do plano de trabalho foram:

- [x] Labconf
- [x] Visita Técnica do prof. Hilmer Neri
- [x] Governança interna entre o LAPPIS, CGTEC, SEFIC


<!-- }}} -->

### Aprendizado de Máquina Lei Rouanet <!-- {{{ -->

O principal objetivo é o estudo de técnicas de Aprendizado de Máquina que possam apoiar o sistema de recomendação e fiscalização da Lei Federal de Incentivo à Cultura (Lei Rouanet). Nessa etapa será realizada uma pesquisa exploratória em técnicas de aprendizado de máquina e processamento de linguagem natural. Tais técnicas e algoritmos serão aplicados para melhorar a experiência de usuário (UX) por meio da proposta de chatbots como interface entre os proponentes na Lei Rouanet e o Ministério da Cultura.

Além disso, técnicas de aprendizado de máquinas serão estudadas para automatizar processos nas trilhas de auditorias, tanto na etapa de habilitação e aprovação, quanto na etapa de prestação de contas. O objetivo é auxiliar auditores a encontrar erros, inconsistências e detectar anomalias nas submissões.

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudo da Lei Rouanet/SALIC;
- [x] Realizar Estudo de aprendizado de máquina;
- [x] Realizar Estudo de processamento linguagem natural;
- [x] Realizar Estudo de chatbots.

As ações realizadas  nesta etapa para atender os objetivos do plano de trabalho foram:

<!-- }}} -->
### Visualização de dados e criação de Dashboards <!-- {{{ -->

Devido à mudanças de escopo do pacote de trabalho "Catálogo de Software", o pacote "Visualização de dados e criação de Dashboards" foi adiantado no cronograma, e a equipe do catálogo foi realocada para essa frente de trabalho.

As seguintes atividades foram desenvolvidas nesse período:

-[x] Execução do método Design Sprint para elaborar propostas de visualização
-[x] Desenvolvimento de protótipos em código usando a prática de desenvolvimento em power trios


### Aferição e aceitação de produtos de software <!-- {{{ -->

O objetivo geral desta frente de pesquisa é auxiliar os times de
desenvolvimento e gestores de TI do MinC a aprimorarem sua capacidade em tomar
decisões acerca da qualidade das versões dos produtos de software entregues por
seus fornecedores.

As atividades referentes a essa frente foram replanejadas para iniciar a execução dos ciclos de estudos experimentais  a partir das entregas continuas, previstas para serem amadurecidas no final da próxima etapa. A alteração de planejamento está evidenciada na nova proposta de cronograma para o projeto.


<!-- }}} -->

# Acompanhamento Financeiro


O valor do repasse referente à Etapa IV foi de R$202.600,00. Todo esse repasse
foi na rubrica 30.90.20, referente à auxílio Financeiro a Pesquisa (Bolsas).
Desse repasse, um total de R$190.635,90 foi executado na Etapa II, representando
na prática que o orçamento foi consumido apenas na categoria mão-de-obra. Todo
esse valor foi executado no pagamento das bolsas do time, e o valor gasto por
frente do projeto pode ser visto na Figura 2 abaixo.

![Neste gráfico é possível observar a representação do percentual do custo da mão-de-obra incidido em cada equipe do projeto. A maior alocação de recursos encontram-se nas equipes do Catálogo de Softwares Culturais(representado pela cor azul), uma vez que grande parte das  funcionalidades desenvolvidas são providas através desta frente, e a equipe do Aprendizado de máquina(representado pela cor verde), que desenvolveu o chatbot.](figs/Planilha_de_Custos_MinC_2017-2019 - Entrega_3.png){width=400px}

# Assinatura

Responsável pela Execução:
---
Nome:  Carla Silva Rocha Aguiar
             (Coordenadora do Projeto)

Assinatura:
![assinatura](figs/assinatura.png)

Data: 08/10/2018

# Anexo I - Resultado da homologação com a Rouana
