---
title: RELATÓRIO DE CUMPRIMENTO DO OBJETO ETAPA III - Ecossistemas de Software Livre - Agosto 2018
author: Carla Silva Rocha Aguiar (Coordenadora do Projeto)
date: 08 de Agosto de 2018
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
colorlinks: true
---

# Introdução

O presente relatório apresenta o acompanhamento do trabalho realizado no
projeto "Ecossistemas de Software Livre", Termo de Cooperação para
Descentralização de Crédito, Processo Ofício No 0646/2017/FUB-UnB, Vigência
Outubro 2017 à Outubro 2019. O relatório apresentado é referente aos avanços
realizados na Etapa III (Abril 2018 à Julho 2018), de acordo com o cronograma
do Plano de Trabalho.

Toda alteração no cronograma proposto foi realizada  a partir de renegociação
com a CGTEC do Ministério da Cultura, e tais alterações estão descritas no
relatório.

## FASE DE PLANEJAMENTO/EXECUÇÃO

O período de Janeiro 2018 à Março de 2018 contemplou as fases de
planejamento e execução. Abaixo serão apresentados, brevemente, os principais
avanços alcançados no período. Toda a documentação e acompanhamento do projeto
está disponibilizado e pode ser acessado na organização do laboratório
[lappis-unb](https://github.com/lappis-unb), e no
repositório específico do projeto
[lappis-unb/EcossistemasSWLivre](https://github.com/lappis-unb/EcossistemasSWLivre).
Todo o planejamento e execução das tarefas podem ser acompanhados tanto nas
_issues_ quanto nas páginas _wiki_.

Abaixo serão apresentados os principais avanços alcançados no período, por
pacote de trabalho (de acordo com o Plano de Trabalho),
de acordo com o cronograma, no período citado.

### Legado em Software Livre <!-- {{{ -->

Os repositórios presentes na organização MinC não possuem uma padronização:
muitos deles tem pouca ou nenhuma documentação, alguns nem possuem licenças de
software, testes automatizados, integração contínua, métricas de qualidade de
código. A pouca conformidade com os modelos seguidos por comunidades de
software livre, dificulta ou limita a contribuição de interessados em coloborar
com os sistemas MinC.

Muitos sistemas legados carecem de testes automatizados, boa documentação e
práticas de desenvolvimento contínuo, o que dificulta enormemente qualquer
forma de evolução. Estes também são fatores críticos na curva de aprendizado de
novos desenvolvedores e criam uma barreira para a existência de comunidades de
software livre/aberto colaborando com tais sistemas. Vários projetos mantidos
pelo Ministério da Cultura possuem as características acima citados.

Durante a primeira etapa do projeto foi priorizado a visão "legacy in the box" (legado
em uma caixa, tradução literal), no qual o foco foi isolar alguns projetos
mantidos pelo Ministério da Cultura por meio de Docker[^docker]. Essa solução gera o
benefício de criar ambientes de desenvolvimento e produção estáveis, fazendo
com que diminua o tempo de configuração de ambiente. Essa abordagem traz um
grande benefício pois possibilita o uso de práticas DevOps mesmo em sistemas
legados. Esse modelo de isolar pacotes de software legados através de containers Docker possibilita um pipeline de
entrega contínua, deploy contínuo, e diminui a fronteira entre a equipe de
infraestrutura e equipe de desenvolvimento.
Já foram observados benefícios dessa abordagem, principalmente em feedback de
desenvolvedores e mantenedores da infraestrutura, feito de forma espontânea.
Pretende-se ainda fazer tanto uma avaliação qualitativa quanto quantitativa
dessa abordagem.

[^docker]: Docker fornece uma camada adicional de abstração e automação de virtualização de nível de sistema operacional. [http://www.docker.com](http://www.docker.com)

Nessa segunda etapa do projeto, usamos uma segunda forma de lidar com software
legado, sempre com o intuito de aplicar técnicas modernas de Engenharia de
Software e padrões de comunidade de software livre, a fim de viabilizar o uso
desses projetos legados em outros contextos e em pipelines
automatizados. O foco então foi transformar um software legado em software
livre, a partir de técnicas de refatoração de código, e suite de testes
automatizados.

Com isso, abordamos um dos objetivos do pacote que é "Pesquisa em
metodologias de refatoração de sistemas legados", adotando padrões de
comunidades de software livre: desde
documentação técnica, quanto código de qualidade (respeitando métricas de
qualidade de software), cobertura de testes, suite de testes automatizado,
ferramenta de integração contínua, e pipeline de deploy contínuo. Para que
pudéssemos alcançar esses objetivos, foi escolhido a API do Salic como estudo
de caso, uma vez que esse é um sistema relativamente pequeno, de grande
relevância e impacto no ecossistema Salic. A compreensão da API do Salic também
auxilia no pacote de trabalho "Aprendizado de Máquina Lei Rouanet", uma vez que
grande parte do trabalho consiste em acessar e processar dados providos da API
(e demanda de dados geram demandas para a evolução da mesma).

As ações programadas para esta etapa de acordo com o plano de trabalho foram:

- [x] Realizar Estudos de conteinerização;
- [x] Realizar Estudo de refatoração em software legado;
- [x] Realizar Estudos sobre práticas de DevOps aplicada a software legado.

Grande parte do time foi alocado por dois meses nessa grande tarefa de
refatorar a API do Salic, e os principais avanços alcançados nessa etapa foram:

1. Adicionada instalação automazada do ambiente de desenvolvimento através do
   Virtualenv[^venv] e do Docker, a documentação está no [README](https://github.com/lappis-unb/salic-api/blob/master/README.rst).
1. A qualidade do código foi melhorada através das seguintes atividades:
    * Os SQL's em forma de textos foram refatorados, agora é utilizado o
      SQLAlchemy[^sqlalchemy]. Essa refatoração melhora a manutenibilidade[^manutenibilidade] do código e
      também permite que a API do Salic funcione com qualquer banco de dados que o
      SQLAlchemy oferece suporte;
    * O Python utilizado no projeto foi atualizado para a versão 3
      (originalmente era utilizado a versão 2 do Python);
    * Utilização do Flake8[^flake] para melhorar a estrutura do código;
    * Adicionado banco de dados local para o ambiente de desenvolvimento;
    * Classificação no Code Climate foi de "F" para "A", resultado da redução
      do débito técnico;
    * Criados testes para os endpoints da API, onde é testado se os dados das
      requisições são recebidos corretamente;
    * Adicionada integração, build e deploy contínuo;
    * Documentação do projeto atualizada.

[^manutenibilidade]: Manutenibilidade é uma característica de produtos de software referente à facilidade, precisão, segurança e economia na execução de ações de manutenção. [https://pt.wikipedia.org/wiki/Manutenibilidade](https://pt.wikipedia.org/wiki/Manutenibilidade)

[^venv]: Virtualenv é um simulador de ambientes virtuais isolados para projetos Python. [http://virtualenv.pypa.io/](http://virtualenv.pypa.io/)
[^sqlalchemy]: SQLAlchemy é uma biblioteca Python de mapeamento objeto-relacional SQL. [http://www.sqlalchemy.org/](http://www.sqlalchemy.org/)
[^flake]: [http://flake8.pycqa.org](http://flake8.pycqa.org)

A mudança da utilização de strings SQL para o código Python usando SQLAlchemy
ocorreu para que além de melhorar a manutenção do código, o SQLAlchemy possui
otmizações e suporte para se conectar com outros sistemas de banco de dados,
por exemplo, caso o Salic passe a utilizar o PostgreSQL todo o sistema da
API Salic continuará funcionando corretamente.

O Flake8 é uma ferramenta de análise estática de código que confere algumas
normas que deixam o código mais legível, padronizado e manutenível, a
refatoração do código utilizando o Flake8 visou melhorar a manutenção do
API adequando o código as normas do Flake8.

Antes da refatoração não era possível levantar um ambiente de desenvolvimento,
pois era necessário estar conectado ao banco de dados do Salic, porém agora,
com o banco de dados local quem quiser contribuir com o projeto pode levantar
o ambiente em seu próprio computador e usar um banco SQLite local, além disso,
para se conectar a um banco de dados basta setar algumas variáveis de ambiente
e o desenvolvedor pode conectar a um banco de dados remoto, como
por exemplo um banco de dados de homologação.

Foi utilizado o Code Climate, um sistema que analisa a qualidade do
código-fonte e atribui uma classificação ao projeto, essa ferramenta verifica
diversas métricas de qualidade de software, como por exemplo duplicação de código informando em quais pontos estão estas duplicações.

Os testes da API foram criados para que ao realizar manutenção no código
seja possivel ter uma garantia de que não foi introduzido bugs no sistema,
anteriormente era difícil saber se o
sistema está funcionando corretamente após o término de uma manutenção. Também
foram criados testes que comparam os resultados das requisições ao novo projeto de API
refatorado com a API original que está atualmente em produção, para se ter uma
garantia de que ao atualizar para a nova versão em produção os sistemas que usam a API
irão continuar funcionando.

Afim de facilitar a adição de novas funcionalidades ao
sistema em produção de forma mais rápida e prática, foi criado uma pipeline de
deploy contínuo, onde é executado os testes do projeto, é checado se a build
está sendo gerada corretamente e depois é feito o deploy para o servidor.

Todas as melhorias implementadas acima, fez com que o projeto da API do Salic
atendesse os padrões de comunidades de software livre, além de atender os
requisitos de DevOps para entrega e deploy contínuo (build de testes). Para
tal, foram realizados ao total 300 commits (no qual foi aberto um pull request
para o projeto no repositório do MinC). A API foi  então colocado em um
ambiente de homologação no laboratório Lappis, e após todos testes passarem nesse
periodo de homologação, o projeto será entregue para o Ministério.

O acompanhamento do projeto realizado pode ser encontrado em
[https://github.com/lappis-unb/salic-api](https://github.com/lappis-unb/salic-api).

<!-- }}} -->

### Catálogo de Softwares Culturais <!-- {{{ -->

O principal objetivo nessa etapa é exercitar em todo ciclo de projeto a
experimentação e inovação contínua, de forma a subsidiar a pesquisa realizada
na Etapa 5. Nesse período foram abordados dois objetivos desse pacote:
"Aplicação de práticas de experimentação e inovação contínua no desenvolvimento
do projeto de Catálogo de Software Culturais", e "Transferência de conhecimento
e capacitar a equipe de servidores e técnicos do MinC em práticas de gestão e
desenvolvimento de software aberto, colaborativo e contínuo".

Ações programadas para esta etapa de acordo com o plano de trabalho estão
listados abaixo:

- [x] Realizar Estudos de tecnologias e práticas devops;
- [x] Realizar Estudos repositórios MinC;
- [x] Elaborar Relatório de Resultado dos Estudos;
- [ ] Realizar estudos sobre funcionalidades de catálogo de software.



Grande parte do objetivo de transferência de conhecimento e capacitação da
equipe de servidores técnicos do MinC foi concentrado nesse período em práticas
DevOps. Para tal, além de encontros técnicos para apresentação das práticas
experimentadas no laboratório, alguns documentos técnicos foram elaborados para
tal fim. Grande parte do time ficou focado em amadurecer o pipeline devops, atualizar
o pipeline dos softwares do Minc trabalhados no laboratório (Salic API, Salic, Mapas culturais), além de
gerar a documentação técnica do conhecimento adquirido.
 Toda a documentação foi disponibilizada no repositório do laboratório em
[https://gitlab.com/lappis-unb/docs](https://gitlab.com/lappis-unb/docs),
disponibilizada também como anexo no final deste documento, os documentos
cobrem tanto a primeira quanto a terceira meta do período.

Foi elaborado documentação/relatório descrevendo todo o pipeline usado para
deploy contínuo no laboratório com os seguintes tutoriais, que podem ser aplicados em diversos contextos:

1. GitLab CI/CD: Guia relacionado ao uso da Integração Contínua e Deploy
   contínuo no Gitlab;
1. Overview e exemplo básico(pt-br): Um guia que ensina como usar o gitlab
   CI/CD para gerar integração contínua e deploy contínuo em um projeto básico;
1. Usando Docker Compose (pt-br): Um guia que ensina como usar o GitLab CI/CD
   para gerar integração contínua com o Docker Compose em um projeto ágil;
1. Integrando GitLab CI/CD com projeto GitHub(pt-br): Um procedimento que
   possibilita o uso do GitLab CI/CD no projeto GitHub.

Toda a documentação foi realizada em português e disponibilizada para acesso.

Referente à segunda meta "Realizar Estudos repositórios MinC" nesse período foram finalizadas
o checklist dos projetos/repositórios priorizados pelo ministério e também aprofundado o estudo sobre
 as funcionalidades do Salic e como a execução da lei
Rouanet é realizada no Salic. Foram realizadas diversas reuniões técnicas com a
equipe da SEFIC, desde a equipe responsável pela admissibilidade até a equipe
responsábel pela avaliação de resultados. Os objetivos dessas reuniões foram:
(a) compreender o processo (fases, etapas) da Lei Federal de Incentivo à Cultura, (b) identificar
os principais envolvidos/stakeholders em cada etapa, (c) levantar os principais
pontos de melhoria. A partir desses levantamentos, vamos na próxima etapa,
propor melhorias, ou por meio do assistente virtual (chatbot) ou por meio de
algoritmos de aprendizagem de máquinas ou mesmo por meio de novos requisitos para o Salic.

Referente à última meta "Realizar estudos sobre funcionalidades de catálogo de
software", foi feito um levantamento, juntamente com a CGTEC, da necessidade de se desenvolver um catálogo de software
como previsto no plano de trabalho. Foram levantados como alguns governos lidam com o portifólio de projetos software livre, tais como as iniciativas do governo inglês de trabalhar majoritamente com software livre
[https://governmenttechnology.blog.gov.uk/2016/12/15/next-steps-for-open-source-in-government/](https://governmenttechnology.blog.gov.uk/2016/12/15/next-steps-for-open-source-in-government/), e manter seu catálogo de software na própria organização github [http://gds-operations.github.io/](http://gds-operations.github.io/). Observamos também uma tendência mundial do uso de software livre no governo (egovernment - [http://www.egov4dev.org/success/definitions.shtml](http://www.egov4dev.org/success/definitions.shtml)), com uma quantidade crescente de adesão [https://government.github.com/community/](https://government.github.com/community/), [https://github.com/g0v](https://github.com/g0v). Observamos que o próprio repositório, organização, e wiki do repositório são utilizados para compor o catálogo de software. Como o principal objetivo dessa etapa é executar um ciclo completo de projeto, de comum acordo com a CGTEC, decidimos não desenvolver o catálogo de software, como previsto no calendário. Para atender o objetivo principal da etapa, o ciclo completo de projeto será realizado no pacote de trabalho "Aprendizado de Máquina Lei Rouanet". A equipe devops manteve na frente catálogo, e os demais integrantes da frente foram realocados para o pacote de trabalho "Aprendizado de Máquina Lei Rouanet". Essa última mudança foi motivada pela prioridade e importância dadas tanto pela CGTEC quanto SEFIC em relação ao chatbot e à frente aprendizagem de máquina. Isso fez com que o cronograma de entregas fossem encurtados, justificando o aumento das equipes para garantir tais entregas. Porém, não houveram alterações no processo administrativo dos membros das equipes, e como visto na análise financeira, parte da equipe manteve alocada no pacote de trabalho "Catálogo de Softwares Culturais".


<!-- }}} -->

### Práticas de gestão colaborativa <!-- {{{ -->

Nessa etapa será realizada uma pesquisa exploratória tendo como objeto de
estudo os movimentos, organizações, desenvolvedores e demais stakeholders que
atuam na gestão colaborativa de software livre. O principal objetivo do
trabalho de gestão colaborativa dessas comunidades de software livre é manter
um conjunto de ações de governança digital e comunicação que aproveite ao
máximo esse potencial em favor das necessidades do órgão e das metas comuns às
organizações parte das comunidades. Esse esforço envolve um trabalho de
mapeamento de atores de cada comunidade (atuais e potenciais futuros),
assessoria para planejamento conjunto, facilitação de fluxos de comunicação e
mobilização, realização de atividades conjuntas para integração, identificação
de oportunidades externas, assessoria para comunicação e divulgação ao público
externo à comunidade e apoio para solução de conflitos.

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudos sobre processo de planejamento conjunto;
- [x] Identificar grupos de opinião.

Todas as atividades relacionadas as ações listadas acima foram 100% finalizada.
Nessa etapa, foi focado na estratégia de colaboração entre os laboratórios de
pesquisa que contribuem para os repositórios MinC:

1. Frente de metodologias ágeis e DevOps: Por ser uma prática comum ao Lappis,
   oriunda da própria história do laboratório e reforçada pelas disciplinas
   práticas da FGA/UnB, é um ativo que pode ser compartilhado na comunidade de
   laboratórios;
    - Oficinas para intercâmbio de método de trabalho (funcionamento das
      sprints, wikis, decisão sobre pull requests etc) - Maio ou junho/2018;
    - Evento prático de DevOps para apresentar o resultado da pesquisa e fazer
      intercâmbio prático;
1. Frente de tecnologias livres para chatbots: Pela carência de tecnologias
   livres desse tipo e as inúmeras aplicações na qualificação dos serviços
   públicos essa pode ser uma oportunidade para os outros laboratórios. O Lappis
   pode auxiliar a incorporação dessa tecnologia nos serviços digitais em
   desenvolvimento pelos outros laboratórios, assim como já está fazendo com o
   Salic e pode fazer com o Mapas Culturais;
    - Lançamento da tecnologia no MinC e Workshop técnico na semana seguinte
      para os interessados em conhecer/colaborar na tecnologia;
    - Incorporação de metas estratégicas conjuntas para DevOps e chatbots em
      outros serviços digitais do MinC;
    - Implementação de boas práticas para governança da comunidade em torno
      desse ativo tecnológico (chatbots) visando aumento da contribuição de
      desenvolvedores externos ao Lappis, com foco nos times dos laboratórios
      parceiros;
1. Frente de Governança de Comunidades: Essa frente envolve pesquisa e
   realização de eventos conjuntos com temas estratégicos para a colaboração
   aberta nas tecnologias desenvolvidas e mantidas pelo Estado.

Intercâmbio de pesquisa através do compartilhamento de referências e produção
conjunta de artigos - Seminário Interno com UFG - Jul/2018 à Out/2018.

Realização de eventos conjuntos sobre o tema da Governança de Comunidades Open
Source com adesão do Estado e Contratação Pública de TICs - Maio ou junho/2018.

<!-- }}} -->

### Aprendizado de Máquina Lei Rouanet <!-- {{{ -->

O principal objetivo é o estudo de técnicas de Aprendizado de Máquina que
possam apoiar o sistema de recomendação e fiscalização da Lei Federal de Incentivo à Cultura (Lei Rouanet). Nessa
etapa será realizada uma pesquisa exploratória em técnicas de aprendizado de
máquina e processamento de linguagem natural. Tais técnicas e algoritmos serão
aplicados para melhorar a experiência de usuário (UX) por meio da proposta de
chatbots como interface entre os proponentes na Lei Rouanet e o Ministério da
Cultura.

Além disso, técnicas de aprendizado de máquinas serão estudadas para
automatizar processos nas trilhas de auditorias, tanto na etapa de habilitação
e aprovação, quanto na etapa de prestação de contas. O objetivo é auxiliar
auditores a encontrar erros, inconsistências e detectar anomalias nas
submissões.

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudo Lei Rouanet/SALIC;
- [x] Realizar Estudo de aprendizado de máquina;
- [x] Realizar Estudo processamento linguagem natural;
- [x] Realizar Estudos de chatbots.

Todas as atividades relacionadas as ações listadas acima foram 100%
finalizadas. Segue resumo da execução das atividades:

Foi desenvolvido uma versão inicial do bot -- versão 0.1 (beta) -- com o
framework Hubot Natural[^hubot], o desenvolvimento aconteceu após estudos sobre
ferramentas para criação de chatbots. Decidiu-se utilizar o Rocket.Chat como
interface para o chatbot, compondo a solução em conjunto com o Hubot Natural.

[^hubot]: Hubot Natural é um chatbot de Processamento de Linguagem Natural para o Rocket.Chat. [https://github.com/RocketChat/hubot-natural](https://github.com/RocketChat/hubot-natural)

Realizou-se evolução do projeto Hubot Natural, com contribuições da equipe ao
repositório oficial do projeto. Além de colaboração com os desenvolvedores core
do projeto Rocket.Chat para avaliação do melhor caminho para futuras evoluções.

Esta primeira versão foi treinada com uma base de conhecimento criada a partir
de documentos disponibilizados pela ouvidoria da SEFIC, importante destacar que
neste primeiro treinamento foi incluido especialmente conhecimentos avançados
sobre a lei de incentivo, deixando de fora da base conhecimento básicos
necessários para responder adequadamente questões mais básicas.

Levantou-se um ambiente de homologação em [https://rouana.lappis.rocks](https://rouana.lappis.rocks), incluindo uma landing page da Rouana
com instruções de como validar e homologar o assistente virtual, onde através
da base de conhecimento criada a partir dos documentos disponibilizados pela
ouvidoria da SEFIC, avaliou-se a eficácia do chatbot através de testes de
usuários incluindo servidores do MinC, pesquisadores e alunos do Lappis.

Os testes realizados com chatbot versão 0.1 (beta) em ambiente de homologação
revelaram que o assistente virtual com as tecnologias selecionadas atende
perfeitamente as necessidades do projeto, indicando que o caminho trilhado até
o momento está em sintonia com a missão final de proporcionar um novo canal
aos cidadãos para compreender e tirar dúvidas sobre a lei Rouanet.

Os dados coletados e feedback dos usuários durante a fase de homologação serão
utilizados para direcionar a evolução e melhorias, identificou-se inicialmente
que a base de conhecimento necessita de evolução, especialmente com questões
mais simples.

Contribuimos com a documentação do repositório do Hubot Natural, incluindo
documentar o processo de configuração do LiveTransfer, tradução da documentação
do Hubot Natural para o inglês e adoção de solução de documentação para o
Hubot Natural.
Foi feito também levantamento de práticas e ferramentas para instrumentalização
com ferramentas para análise estática como Coffeelint e
Codeclimate, além de integração contínua ao projeto.

Realizou-se também pesquisa e implementação de melhores práticas de UX para
interfaces conversacionais, necessária para melhoria na experiência do usuário
ao utilizar o assistente virtual da lei Rouanet.

Em paralelo a todo este trabalho, estudou-se tecnologias para criação de uma
nova versão do bot, incluindo frameworks para criação de chatbots mais
inteligentes, exemplos: Rasa, AIVA, Botpress, IBM blue mix, Seq2seq,
Hubot-playbook e Neo4j.  Estes frameworks foram avaliados na prática e algumas
tecnologias foram analisadas em detalhes, como: Rasa-NLU + BotPress +
RocketChat e Rasa-core + Rasa-nlu.

A implementação da nova versão do bot foi iniciada em paralelo ao
desenvolvimento da versão 0.1 (beta) citada anteriormente, já utilizando uma
abordagem mais poderosa de desenvolvimento de bots; escolha de mudança de
arquitetura e tecnologias a serem usadas para a próxima versão do chat.

Em complemento ao desenvolvimento do chatbot realizamos estudos para
compreensão do processo de projetos incentivados via Lei Rouanet, incluindo
estudo de tecnologias de aprendizado de máquina a fim de auxiliar o processo de
admissão e prestação de contas do Salic.

Neste sentido, iniciou-se estudos e testes de algoritmos para detecção de
anomalias em itens das planilhas orçamentárias de projetos submetidos ao Salic,
utilizando técnicas de aprendizado de máquina, tanto na extração de
características relevantes para o problema (_Exploratory Data Analysis_ e _Data
Wrangling_), quanto na classificação de novos dados (usando modelos básicos de
regressão do módulo _Scikit-learn_).

São dois os objetivos dessa frente de trabalho:

1. Auxiliar o processo de admissão e prestação de contas do Salic: automatizar
   tarefas simples e repetitivas de tais processos para otimizar da criação à
   conclusão de projetos culturais;
2. Fornecer insumos para um sistema de transparência do Salic: fornecer
   métricas utilizadas para mapear as categorias e regiões de maior incentivo e
   para incentivar novos produtores culturais.

A frente está trabalhando na criação de uma API que deve se comunicar, a
princípio, com o Salic. Contudo, futuramente novos sistemas também podem
realizar requisições à API para extrair métricas sobre projetos culturais.

O desenvolvimento desta frente está sendo feito com o levantamento de hipóteses
e evolução da API. A metodologia utilizada é a _Hypothesis-Driven Development_,
focada em criação e validação contínua de hipóteses de aprendizado de máquina,
seguida de implementação na API das hipóteses confirmadas na etapa de
validação.

A API está em desenvolvimento em Python, utilizando-se o framework Django. Três
hipóteses já foram levantadas e estão sendo validadas:

1. Relação entre o tempo e a mudança dos preços de itens da planilha
   orçamentária de um projeto;
2. Identificação de itens superfaturados a partir do histórico de projetos
   aprovados e recusados e;
3. Categorização e identificação de similaridade de um projeto a partir de sua
   planilha orçamentária vigente.

Caso as hipóteses se confirmem, serão implementadas e será possível verificar,
para cada projeto, se sua planilha orçamentária contém itens possivelmente
superfaturados e quais os projetos mais similares com o projeto em questão.

<!-- }}} -->

### Aferição e aceitação de produtos de software <!-- {{{ -->

O objetivo geral desta frente de pesquisa é auxiliar os times de
desenvolvimento e gestores de TI do MinC a aprimorarem sua capacidade em tomar
decisões acerca da qualidade das versões dos produtos de software entregues por
seus fornecedores.

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Revisão da área;
- [x] Diagnóstico sobre as práticas atualmente adotadas pelo MinC de garantia da qualidade de produto;
- [ ] Elaborar Plano de Pesquisa-Ação.

Nessa etapa foram aplicadas surveys com os gestores do MinC e desenvolvedores
seniores do Lappis e MinC. O objetivo do survey foi fazer uma análise
qualitativa sobre o projeto e sobre práticas devops e práticas de comunidades
de software livre.

Nesse período também foi realizado a análise do survey aplicado aos alunos. O
resultado é apresentado em anexo.

<!-- }}} -->

# Acompanhamento Financeiro


O valor do repasse referente à Etapa III foi de R$202.600,00. Todo esse repasse
foi na rubrica 30.90.20, referente à auxílio Financeiro a Pesquisa (Bolsas).
Desse repasse, um total de R$190.635,90 foi executado na Etapa II, representando
na prática que o orçamento foi consumido apenas na categoria mão-de-obra. Todo
esse valor foi executado no pagamento das bolsas do time, e o valor gasto por
frente do projeto pode ser visto na Figura 2 abaixo.

![Neste gráfico é possível observar a representação do percentual do custo da mão-de-obra incidido em cada equipe do projeto. A maior alocação de recursos encontram-se nas equipes do Catálogo de Softwares Culturais(representado pela cor azul), uma vez que grande parte das  funcionalidades desenvolvidas são providas através desta frente, e a equipe do Aprendizado de máquina(representado pela cor verde), que desenvolveu o chatbot.](figs/bolsas_E2.png){width=400px}

# Assinatura

Responsável pela Execução:
---
Nome:  Carla Silva Rocha Aguiar
             (Coordenadora do Projeto)

Assinatura:
![assinatura](figs/assinatura.png)

Data: 06/04/2018



