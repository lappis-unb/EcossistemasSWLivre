# RELATÓRIO DE CUMPRIMENTO DO OBJETO ETAPA II - Ecossistemas de Software Livre - Abril 2018


# Introdução
 O presente relatório apresenta o acompanhamento do trabalho realizado no projeto "Ecossistemas de Software Livre", Termo de Cooperação para Descentralização de Crédito, Processo Ofício No 0646/2017/FUB-UnB, Vigência Outubro 2017 à Outubro 2019. O relatório apresentado é referente aos avanços realizados na Etapa II (Janeiro 2018 à Março 2018), de acordo com o cronograma do Plano de Trabalho.

## FASE DE PLANEJAMENTO/EXECUÇÃO

### Legado em Software Livre

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudos de conteinerização
- [x] Realizar Estudo de refatoração em software legado
- [x] Realizar Estudos sobre práticas de DevOps aplicada a software legado

dockerização da API -
Legado API - Salic
transformou o software l

mostra as métricas, checklist antes/depois

- Adicionada instalação automazada do ambiente de desenvolvimento através do Virtualenv e do Docker, a documentação está no README.
- A qualidade do código foi melhorada através das seguintes atividades:
  - Os SQL's em forma de textos foram refatorados, e agora é utilizado o SQLAlchemy. Essa refatoração melhora a manutenibilidade do código e também permite que o salic-api funcione com qualquer banco de dados que o SQLAlchemy oferece suporte.
  - O Python utilizado no projeto foi atualizado para a versão 3.
  - Utilização do Flake8 para melhorar a estrutura do código.
  - Adicionado banco de dados local para o ambiente de desenvolvimento.
  - Classificação no Code Climate foi de "F" para "A", resultado da redução do débito técnico.
  - Criados testes para os endpoints da api, onde é testado se os dados das requisições são recebidos corretamente.
  - Adicionada integração, build e deploy contínuo.
  - Documentação do projeto atualizada.

API até homologação
Commits pro minc PR (300 commits)



### Catálogo de Softwares Culturais

Ações programadas para esta etapa de acordo com o plano de trabalho:

- [x] Realizar Estudos de tecnologias e práticas devops
- [x] Realizar Estudos repositórios MINC
- [x] Elaborar Relatório de Resultado dos Estudos

Todas as atividades relacionadas as ações listadas acima foram 100% finalizadas.

A ação abaixo foi programada para esta etapa, mas foi realocada para em decisão conjunta com o gestor do MinC para a Etapa 3.

- [ ] Realizar estudos sobre funcionalidades de catálogo de software


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

Ações programadas para esta etapa:

- [x] Realizar Estudo de aprendizado de máquina
- [x] Realizar Estudo processamento linguagem natural
- [x] Realizar Estudos de chatbots
- [x] Realizar Estudo Lei Rouanet/SALIC

Todas as atividades relacionadas as ações listadas acima foram 100%
finalizadas. Segue resumo da execução das atividades:

Foi desenvolvido uma versão inicial do bot -- versão 0.1 (beta) -- com o
framework Hubot Natural, o desenvolvimento aconteceu após estudos sobre
ferramentas para criação de chatbots. Decidiu-se utilizar o Rocket.Chat como
interface para o chatbot, compondo a solução em conjunto com o Hubot Natural.

Realizou-se evolução do projeto Hubot Natural, com contribuições da equipe ao
repositório oficial do projeto. Além de colaboração com os desenvolvedores core
do projeto Rocket.Chat para avaliação do melhor caminho para futuras evoluções.

Esta primeira versão foi treinada com uma base de conhecimento criada a partir
de documentos disponibilizados pela ouvidoria da SEFIC, importante destacar que
neste primeiro treinamento foi incluido especialmente conhecimentos avançados
sobre a lei de incentivo, deixando de fora da base conhecimento básicos
necessários para responder adequadamente questões mais básicas.

Levantou-se um ambiente de homologação, incluindo uma landing page da Rouana
com instruções de como validar e homologar o assistente virtual, onde através
da base de conhecimento criada a partir dos documentos disponibilizados pela
ouvidoria da SEFIC, avaliou-se a eficácia do chatbot através de testes de
usuários incluindo servidores do MinC e pesquisadores e alunos do Lappis.

Os testes realizados com chatbot versão 0.1 (beta) em ambiente de homologação
revelou que o assistente virtual com as tecnologias selecionadas atende
perfeitamente as necessidades do projeto, indicando que o caminho trilhado até
o momento estão em sintonia com a missão final de proporcionar um novo canal
aos cidadãos para compreender e tirar dúvidas sobre a lei Rouanet.

Os dados coletados e feedback dos usuários durante a fase de homologação serão
utilizados para direcionar a evolução e melhorias, identificou-se inicialmente
que a base de conhecimento necessita de evolução, especialmente com questões
mais simples.

Contribuimos com a documentação do repositório do Hubot Natural, incluindo
documentar o processo de configuração do LiveTransfer, tradução da documentação
do Hubot Natural para o inglês e adoção de solução de documentação para o
hubot-natural.

Foi feito levantamento de práticas e ferramentas para instrumentalização do
Hubot Natural com ferramentas para análise estática como Coffeelint e
Codeclimate, além de integração contínua ao Hubot Natural.

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
arquitetura tecnologias a serem usadas para a próxima versão do chat.

Em complemento ao desenvolvimento do chatbot realizamos estudos para
compreensão do processo de projetos incentivados via Lei Rouanet, incluindo
estudo de tecnologias para aprendizado de máquina a fim de auxiliar
na evolução do assistente virtual.

Neste sentido iniciou-se estudos e testes de algoritmos para detecção de
anomalias das planilhas orçamentárias dos projetos submetidos utilizando
tecnologias autônomas de aprendizado de máquina ...

(continuar aqui descrevendo detalhes sobre a frente ML)

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
