# RELATÓRIO DE CUMPRIMENTO DO OBJETO ETAPA II - Ecossistemas de Software Livre - Abril 2018


# Introdução
 O presente relatório apresenta o acompanhamento do trabalho realizado no projeto "Ecossistemas de Software Livre", Termo de Cooperação para Descentralização de Crédito, Processo Ofício No 0646/2017/FUB-UnB, Vigência Outubro 2017 à Outubro 2019. O relatório apresentado é referente aos avanços realizados na Etapa II (Janeiro 2018 à Março 2018), de acordo com o cronograma do Plano de Trabalho.

## FASE DE PLANEJAMENTO/EXECUÇÃO
O período de Janeiro 2018 à Março de 2018 foi contemplado às fases de planejamento e execução. Abaixo serão apresentados, brevemente, os
principais avanços alcançados no período. Toda a documentação e acompanhamento do projeto está disponibilizado e pode ser acessado na organização do laboratório (https://github.com/lappis-unb)[https://github.com/lappis-unb], e no repositório específico do projeto (https://github.com/lappis-unb/EcossistemasSWLivre)[https://github.com/lappis-unb/EcossistemasSWLivre]. Todo o planejamento e execução das tarefas podem ser acompanhados tanto nas issues quanto na pagina da wiki.

Abaixo serão apresentados os principais avanços alcançados no período, por pacote de trabalho (de acordo com o Plano de Trabalho).
Os avanços apresentados de acordo com o pacote de trabalho e com cronograma, no período citado.

### Legado em Software Livre
Os repositórios presentes na organização MinC não possuem uma padronização: muitos
deles tem pouca ou nenhuma documentação, alguns nem possuem licenças de software, testes automatizados,
 integração contínua, metricas de qualidade de código. A pouca conformidade com os
modelos seguidos por comunidades de software livre, dificulta ou limita a contribuição de interessados
em coloborar com os sistemas MinC.

Muito sistemas legados carecem testes automatizados, boa documentação e práticas de desenvolvimento contínuo, o que dificulta enormemente qualquer forma de evolução. Estes também são fatores
críticos na curva de aprendizado de novos desenvolvedores e criam uma barreira para a existência
de comunidades de software livre/aberto colaborando com tais sistemas. Vários projetos mantidos pelo
Ministério da Cultura possuem as características acima citados.

A primeira etapa do projeto foi priorizado a visão "legacy in the box" (legado em uma caixa, tradução literal), no qual o foco foi isolar alguns projetos mantidos do Ministério da Cultura por meio de docker. Essa solução gera o benefício de criar ambientes de desenvolvimento e produção estáveis, fazendo com que diminua o tempo de configuração de ambiente. Essa abordagem traz um grande benefício pois possibilita o uso de práticas Devops mesmo em sistemas legados. Esse modelo de dockerizar softwares legados possibilita um pipeline de entrega contínua, deploy continuo, e diminui a fronteira entre a equipe de infraestrutura e equipe de desenvolvimento.
Já foram observados benefícios dessa abordagem, principalmente em feedback de desenvolvedores e mantenedores da infraestrutura, feito de forma espontânea.  Pretende-se ainda fazer tanto uma avaliação qualitativa quanto quantitativa dessa abordagem.

Nessa segunda etapa do projeto, usamos uma segunda forma de lidar com software legado, sempre com o intuito de aplicar técnicas modernas de engenharia de software e padrões de comunidade de software livre, a fim de viabilizar o uso desses projetos legados em comunidades de software livre e em pipelines automatizados. O foco então foi transformar um software legado em software livre, a partir de técnicas de refatoração de código, e suite de testes automatizados. Com isso, abordamos um dos objetivos desse pacote é "Pesquisa em metodologias de refatoração de sistemas legados". Para tal, os padrões de comunidades de software livre devem estar presente nos projetos: desde documentação técnica, quanto código de qualidade (respeitando métricas de qualidade de software), cobertura de testes, suite de testes automatizado, ferramenta de integração contínua, e pipeline de deploy contínuo. Para que pudessemos alcançar esses objetivos, foi escolhido a API do Salic como estudo de caso, uma vez que esse é um sistema relativamente pequeno, de grande relevância e impacto no ecossistema Salic. A compreensão da API do Salic também auxilia no pacote de trabalho "Aprendizado de Máquina Lei Rouanet", uma vez que grande parte do trabalho consiste em acessar e processar dados providos da API (e demanda de dados geram demandas para a evolução da mesma).

As ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudos de conteinerização
- [x] Realizar Estudo de refatoração em software legado
- [x] Realizar Estudos sobre práticas de DevOps aplicada a software legado


Grande parte do time foi alocado por dois meses nessa grande tarefa de refatorar a API do Salic, e as principais avanços alcançados nessa etapa foram:


1. Adicionada instalação automazada do ambiente de desenvolvimento através do Virtualenv e do Docker, a documentação está no README.
1. A qualidade do código foi melhorada através das seguintes atividades:
    1. Os SQL's em forma de textos foram refatorados, e agora é utilizado o SQLAlchemy. Essa refatoração melhora a manutenibilidade do código e também permite que o salic-api funcione com qualquer banco de dados que o SQLAlchemy oferece suporte.
    1. O Python utilizado no projeto foi atualizado para a versão 3 (originalmente era utilizado a versão 2 do python).
    1. Utilização do Flake8 para melhorar a estrutura do código.
    1. Adicionado banco de dados local para o ambiente de desenvolvimento.
    1. Classificação no Code Climate foi de "F" para "A", resultado da redução do débito técnico.
    1. Criados testes para os endpoints da API, onde é testado se os dados das requisições são recebidos corretamente.
    1. Adicionada integração, build e deploy contínuo.
    1. Documentação do projeto atualizada.

Todas as melhorias implementadas acima, fez com que o projeto da API do Salic atendesse todos os padrões de comunidades de software livre, além de atender os requisitos de Devops para entrega e deploy contínuo (build de testes). Para tal, foram realizados ao total 300 commits (no qual foi aberto um pull request para o projeto no repositório do MinC). A API foi  então colocado em um ambiente de homologação no laboratório, e após todos testes passarem nesse periodo de homologação, o projeto será entregue para o Minitério.

O acompanhamento do projeto realizado pode ser encontrado em [https://github.com/lappis-unb/salic-api](https://github.com/lappis-unb/salic-api).

### Catálogo de Softwares Culturais

O principal objetivo nessa etapa é exercitar em todo ciclo de projeto a experimentação e inovação contínua, de forma a subsidiar a pesquisa realizada na Etapa 5. Nesse período foram abordados dois objetivos desse pacote: "Aplicação de práticas de experimentação e inovação contínua no desenvolvimento do projeto de Catálogo de Software Culturais", e "Transferência de conhecimento e capacitar a equipe de servidores e técnicos do MinC em práticas de gestão e desenvolvimento de software aberto, colaborativo e contínuo". Enquanto no primeiro objetivo foi focado da execução de 2 **Design Sprints** para o levantamento de ideias e requisitos para protótipos do produto a ser construido.

Ações programadas para esta etapa de acordo com o plano de trabalho estão listados abaixo:

- [x] Realizar Estudos de tecnologias e práticas devops;
- [x] Realizar Estudos repositórios MINC;
- [x] Elaborar Relatório de Resultado dos Estudos;
- [x] Realizar estudos sobre funcionalidades de catálogo de software

Todas as atividades relacionadas as ações listadas acima foram 100% finalizadas. No último item, o foco do produto foi alterado de "catálogo de software" para "Promova Cultura". Tal mudança foi acordado com os gestores do Ministério. Apesar da mudança de foco do produto, a nova visão não altera o objetivo principal do pacote, que é a "Aplicação de práticas de experimentação e inovação contínua no desenvolvimento do projeto de Catálogo de Software Culturais", além da execução de um ciclo completo de projeto de software.

Grande parte do objetivo de transferência de conhecimento e capacitação da equipe de servidores técnicos do Minc foi concentrado nesse periodo em práticas devops. Para tal,



Prática devops - documentação do pipeline e elaboração dos seguintes tutoriais (disponiveis em anexo)

- GitLab CI/CD: Guides related to the usage of the GitLab's Continuous Integration and Continuous Deployment suite;

- Overview and Basic Example (pt-br): A guide which teaches how to use GitLab CI/CD to generate continuous integration and continuous deployment in a basic project;

- Using Docker Compose (pt-br): A guide which teaches how to use GitLab CI/CD to generate continuous integration with Docker Compose in a basic project.

- Integrating GitLab CI/CD on GitHub Project (pt-br): A procedure which allows to use GitLab CI/CD in a GitHub project.


- Using the cookbooks (en-us): a guide for installing and using Chake gem, a handle for Chef to help configure all LAPPIS's services.


Estudos dos repositórios minc --





### Práticas de gestão colaborativa

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudos sobre processo de planejamento conjunto
- [x] Identificar grupos de opinião

Todas as atividades relacionadas as ações listadas acima foram 100% finalizada

Proposta de colaboração entre os labs (anexo)

Proposta de agenda de eventos entre labs e minc e com a comunidade de software livre?

### Aprendizado de Máquina Lei Rouanet

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudo Lei Rouanet/SALIC

As seguintes etapas foram planejadas para a Etapa 2, mas foram repriorizadas para serem trabalhadas na Etapa 1

- [x] Realizar Estudo de aprendizado de máquina
- [x] Realizar Estudo processamento linguagem natural
- [x] Realizar Estudos de chatbots
- [x] Realizar Estudo Lei Rouanet/SALIC


Ambiente de homologação do chatbot - contribuição para o rocket.chat e escolha de mudança de arquitetura tecnologias a serem usadas para a próxima versão do chat.

Compreensão do processo de projetos incentivados via Lei Rouanet --

Testes de algoritmos de detecção de anomalias das planilhas orçamentárias.


### Aferição e aceitação de produtos de software

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Revisão da area
- [x] Diagnóstico sobre as práticas atualmente adotadas pelo MinC de garantia da qualidade de produto
- [ ] Elaborar Plano de Pesquisa-Ação

Aplicação de surveys com os gestores do MinC e desenvolvedores seniores do LAPPIS e MinC.


Resultados do survey com os alunos

# Acompanhamento Financeiro
![Detalhamento da execução do repasse na Etapa II.](figs/valores_executados_2.png)

O valor do repasse referente à Etapa I foi de R$598.000,00. Todo esse repasse foi na rubrica 30.90.20, referente à auxílio Financeiro a Pesquisa (Bolsas). Desse repasse, um total de R$161.100,00 foi executado na Etapa I, representando na prática que o orçamento foi consumido apenas na categoria mão-de-obra.. Todo esse valor foi executado no pagamento das bolsas do time, e o valor gasto por frente do projeto pode ser visto na figura abaixo.


![Neste gráfico é possível observar a representação do percentual do custo da mão-de-obra incidido em cada equipe do projeto. A maior alocação de recursos encontram-se nas equipes do Catálogo de Softwares Culturais(representado pela cor azul), uma vez que grande parte das  funcionalidades desenvolvidas são providas através desta
frente, e a equipe do Aprendizado de máquina(representado pela cor verde), que desenvolveu o chatbot.](figs/bolsas.png)

# Assinatura

Responsável pela Execução:
---
Nome:  Carla Silva Rocha Aguiar
             (Coordenadora do Projeto)

Assinatura:

Data: 06/04/2018


# Anexo I - Metodologia

# Anexo II - Alinhamento Estratégico



# Anexo IV - Pesquisa Devops Pesquisa  Survey de Acompanhamento
## Resultados parciais da revisão sistemática referente à Devops


## Estudo sobre a experiência dos alunos participantes do projeto MinC


[https://docs.google.com/forms/d/1SpZMX8qYLZGl7q6nTO4JPpI4eFbMHAJHP5NivG-jMhw/prefill](https://docs.google.com/forms/d/1SpZMX8qYLZGl7q6nTO4JPpI4eFbMHAJHP5NivG-jMhw/prefill)
