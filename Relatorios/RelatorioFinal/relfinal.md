---
title: RELATÓRIO FINAL - Ecossistemas de Software Livre - Setembro 2019
author: Carla Silva Rocha Aguiar (Coordenadora do Projeto)
date: 15 de Setembro de 2019
geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
colorlinks: true
---

# Objetivo Geral


# Objetivos Específicos

No plano de trabalho foram levantados alguns objetivos específicos referentes à parceria. Ao longo do relatório de entrega final serão detalhadas como esses objetivos foram alcaçandos. Abaixo elencamos esses objetivos e resumimos como eles foram realizados, e por qual pacote de trabalho:

-  __Realizar estudos de algoritmos de aprendizado de máquina para analisar dados da execução da Lei Rouanet__:O projeto "Salic-ML" realizou esse objetivo. Além de inúmeras reuniões com a equipe da Sefic, para entender o processo da Lei de Incentivo a Cultura e o SALIC, foram levantados os principais gargalos do processo. O gargalo mais crítico foi a prestação de contas, no qual o Ministério tem um passivo de cerca de 17 mil projetos a serem análisado o objeto e a prestação de contas. O time então priorizou em desenvolver algoritmos de ciência de dados para gerar métricas/indicadores que explicitem a **complexidade** de um projeto cultural, no que tange a análise financeira. O objetivo é direcionar o trabalho dos técnicos da sefic no trabalho técnico, e aos gestores a priorizar e delegar as análises de forma eficiente e orientadas a dados. Esse trabalho foi finalizado e entregue como um microsserviço a ser integrado no SALIC.

- _
-  __Realizar estudos de métodos/práticas ágeis e de desenvolvimento lean de software, além das práticas de engenharia de software e de governança utilizadas nas comunidades de software livre, de forma a prover uma infraestrutura computacional para desenvolvimento e experimentação contínua de software__: Esse objetivo foi alcaçado com as reuniões estratégias trimestrais com os principais stakeholders do ministério, além de mantermos as boas prática de comunidades de software livre nos projetos desenvolvidos ao longo da cooperação. Um grande trabalho de governança foi feito com a chatbot "Tais", engajando outros ministérios a adotarem a solução técnica da Tais, aumentando assim a comunidade.


-  __Fornecer suporte tecnológico para apropriação das informações por parte da sociedade civil de
maneira a contribuir para transparência pública e participação social__ Todos os estudos, código, apresentações, material de treinamento foram disponibilizados com licenças livres, de modo que a sociedade civil possa acessar, dar feedback, contribuir, etc.

-  __Fornecer suporte tecnológico para estimular a participação da sociedade civil na governança
digital em torno das tecnologias livres do portfólio do ministério__: esse objetivo foi alcançado ao seguir as boas práticas e documentações adotadas pela comunidade de software livre. Dessa maneira, diminui a barreira de contribuição para os interessados em contribuir com os projetos desenvolvidos ao longo da parceria.

-  __Mineração em repositórios de software para extração e análise de dados__: esse objetivo foi alncançado nos notebooks de análise de dados. Isso foi feito tanto no contexto da Lei de Incentivo Cultural, por meio da mineração do banco de dados do Salic, quanto da análise dos próprios repositórios e métricas dos projetos desenvolvidos ao longo do parceria.

- __Processamento de linguagem natural dos dados extraídos dos diferentes sistemas de software
culturais__: esse objetivo foi alcaçando por meio da assistente virtual TAIS. Nela, aplicamos algoritmos de __Natural Language Understanding (NLU)__ para a classificação da intenção dos usuários que interagem com a chatbot por meio de linguagem natural.

- __Transferência de conhecimento da academia para o Estado__: além dos diversos workshops realizados ao longo do projeto com a equipe de TI do Ministério da Cidadania, foram realizados pela frente de governanças do projeto, diversas interaçoes com comunidades de software livre e outros ministérios.

- __Formação de alunos de graduação em pós-graduação em projetos com problemas reais do
contexto cultural__: esse objetivo foi alcançado com grande parte da equipe do projetos sendo alunos de graduação de Engenharia de Software, design e letras. Ao total, X alunos de alunos de graduação foram bolsistas do projeto.

- __Contribuir para o fomento da cultura de software livre na Administração Pública Federal__: esse objetivo foi alcançado;

- __Contribuir para o desenvolvimento da cultura de tomada de decisões orientadas a dados e
evidência__: esse objetivo foi alncançado com o projeto Salic-ML no qual  estimamos métricas e indicadores de complexidade de projetos de projetos culturais. Na TAIS, criamos um dashboard de BI que fornece, em tempo real, o comportamento dos usuários que interagem com a TAIS. Esse dashboard disponibiliza dados preciosos para compreender o perfil do usuário que acessa a o portal da Lei de Incentivo, e o comportamento desse usuário;

- __Contribuir para o estabelecimento da cultura de desenvolvimento e experimentação contínua__: alcançamos esse objetivo pela forma como escolhemos as ferramentas, técnicas, e escopos a serem desenvolvidos, sempre realizados após um período de experimentação. Esses aprendizado e amadurecimento de experimentação contínua foi registrado nas wikis e notebooks disponibilizados em licenças livre nos repositórios dos projetos, no qual estudos comparativos precedem escolhas técnicas.


# Metodologia, metas e etapas do projeto

O planejamento de execução das metas foi inicialmente dividido em 5 etapas e 5 pacotes de trabalho. Descrevemos os avanços a seguir e ressaltamos alguns itens que foram executados de forma diferente do cronograma. Vale ressaltar que todas execução diferente ao planejado foi previamente acordada com o Ministério, e registrado nos relatórios de acompanhamento entregues trimestralmente.

## Inovação tecnológica em Software

Os pacotes de trabalho da presente parceria acarretou em X projetos, distribuidos em X repositórios. Ao todo, foram X arquivos distintos, X commits com contribuições de X desenvolvedores distintos, X deles vinculados como bolsistas do projeto, correspondendo a X% dos commits realizados no projeto. Além disto, o projeto ainda contempla estudos acadêmicos,  estudos de identidade visual, dinâmicas de capacitação e outros insumos fora do produto de software propriamente dito. 

Obviamente é impraticável anexar toda esta produção à este documento, portanto este documento apresenta um resumo com estatísticas e os resultados mais importantes obtidos e direções sobre como obter o código para fazer uma análise detalhada. Todo software desenvolvido no projeto está disponível publicamente sob licenças livres na plataforma Github (principal plataforma de disponibilização de código no mundo). Os repositórios e seus respectivos endereços estão listados abaixo e podem ser acessados publicamente por qualquer pessoa:

- Ecossitemas ([https://github.com/lappis-unb/EcossistemasSWLivre](https://github.com/lappis-unb/EcossistemasSWLivre)): todos os documentos administrativos do projeto estão disponibilizados nesse repositório. Registro de reuniões, decisões, relatórios de acompanhamento, plano de trabalho.

- TAIS ([https://github.com/lappis-unb/tais](https://github.com/lappis-unb/tais)): aplicação principal da TAIS, com o bot, interface web, dashboard de BI. 


- Salic-ML ([https://github.com/lappis-unb/salic-ml](https://github.com/lappis-unb/salic-ml)): aplicação principal do microsserviço SALIC-ML. Nesse se encontra tanto a API do microsserviço, quanto toda a documentação técnica na Wiki, e estudos realizados nos notebooks.

- Promova Cultura ([https://github.com/lappis-unb/PromovaCultura](https://github.com/lappis-unb/PromovaCultura)): estudo de visualização de dados dos dados do banco de dados do Salic. Contém toda a documentação técnica, resultados da design sprint realizadas para definição do escopo e as visualizações implementadas.

- Botflow ([https://github.com/lappis-unb/BotFlow](https://github.com/lappis-unb/BotFlow) e [https://github.com/lappis-unb/BotFlowAPI](https://github.com/lappis-unb/BotFlowAPI)): não previsto no plano de trabalho, mas foi julgado pelo time necessário para facilitar a manutenção e evolução da base de conhecimento da Tais.

- Salic-API ([https://github.com/lappis-unb/salic-api](https://github.com/lappis-unb/salic-api)): refatoramos, criamos testes unitários, pipelinde de integração contínua, documentação técnica. Ou seja, adequamos a API do Salic, que é o projeto do ministério de maior interesse externo, para os padrões, boas práticas e documentação de comunidades de software livre.

Existem metodologias na área de Engenharia de Software para estimar o esforço de desenvolvimento de um produto. É importante notar que estes modelos são apenas aproximados, mas ajudam a estabelecer uma ordem de grandeza do esforço de desenvolvimento de um software em comparação com projetos semelhantes encontrados na indústria. 

 Analisamos o projeto da ótica do modelo COCOMO (Constructive Cost Model) desenvolvido por Berry W. Boehm a partir da análise empírica da produtividade de equipes de desenvolvimento em vários projetos de software reais. Os dados foram extraídos utilizando as ferramenta sloccount (para código Python) e cloc (para as linguagens. A tabela abaixo resume os principais resultados:


XX

 Podemos estimar o custo de desenvolvimento a partir do número de horas necessários para desenvolver o projeto, o custo médio da hora trabalhada de cada desenvolvedor e o parâmetro de sobrecarga (do inglês overhead), que estima o esforço adicional devido à reescrita de código e realização de outras atividades como reuniões, planejamento, documentação, estudo, etc que não estão diretamente relacionadas à produção de código. 
A ferramenta sloccount considera como valores padrão um parâmetro de overhead de 2,4 e um salário anualizado de U$56.286,00. Utilizando-se estes valores, obtemos uma estimativa de U$X ou cerca de X milhões de reais. Obviamente a realidade brasileira é diferente. Se tomarmos o salário médio de um desenvolvedor como sendo R$6.400,00, este custo cairia para R$X (sem custos trabalhistas), o que ainda assim demonstra uma grande eficiência econômica na execução do projeto.

Nota-se ainda que o projeto abrange atividades de pesquisa, formação de alunos treinamento e desenvolvimento de identidade visual que estão fora do escopo da programação que em um acordo comercial aumentariam ainda mais o custo do projeto. 

Finalmente, além do desenvolvimento de uma solução para o Ministério da Cidadania, o projeto parte de uma lógica de parceria com a universidade e pressupõe a criação de insumos de pesquisa e produção acadêmica. A maior parte dos membros da equipe é formada por alunos do curso de Engenharia de Software, sendo que a participação no projeto contribuiu diretamente para a formação dos mesmos. Alguns destes alunos adotaram o temas relacionados ao projeto como tema em trabalhos de conclusão de curso ainda em andamento. Foram publicados dois artigos científicos. Um deles, com o título "X" que contem a experienca no desenvolvimento da Tais foi apresentado no OpenSym, uma dos maiores simposios de pesquisa acadêmica em software livre. O segundo, com o título "X" foi aceito  na revista X, de alto impacto acadêmico (A1 no critério de Qualis da Capes) e mostra o resultado acadêmico dos estudos em devops. Foi publicado também um capítulo do livro "X", no qual discutimos os modelos de contratação nas equipes de TI do governo federal.



## Pacote de Trabalho: Estratégia/modelo de transformação de softwares legados em comunidades de software aberto


Evoluir e manter um software legado é uma experiência desgastante para 
desenvolvedores e desestimulantes no contexto de fomento a comunidades. Por outro lado, 
a reescrita desses softwares é impraticável e, em se tratando de software implantado,
a necessidade de adicionar novas funcionalidades e dar manutenção persiste. 

Os objetivos gerais desse pacote de trabalho, e o alcance desses objetivos foram:

- [x] Pesquisa em metodologias de refatoração de sistemas legados - 100% alcançado;
- [x] Utilizar como estudo de casos alguns sistemas legados do Ministério da Cultura, tais como o
projeto SIMEC (Sistema Integrado de Monitoramento Execução e Controle) e o projeto Salic (Sistema de Apoio às Leis de Incentivo à Cultura), Sistel - 100% alcançado.

### Metas Específicas

Quanto as metas específicas dessa frente de trabalho definidas plano de trabalho são:

1. __Estudos e documentação do processo de conteinerização, testes automatizados, refatoração de sistemas legados em uma estrutura de DevOps para viabilizar trabalhos futuros__

**Concluído**


**Documentação comprobatória**


2.  __Pesquisa em metodologias de refatoração de sistemas legados__

**Concluído**


**Documentação comprobatória**

3.  __Utilizar como estudo de casos alguns sistemas legados do Ministério da Cultura, tais como o projeto SIMEC (Sistema Integrado de Monitoramento Execução e Controle) e o projeto Salic (Sistema de Apoio às Leis de Incentivo à Cultura), Sistel__ 

**Concluído**


**Documentação comprobatória**

## Pacote de Trabalho: Estudo sobre catálogos de Software Culturais

De acordo com o plano de trabalho, "O foco dessa etapa é executar o ciclo de projeto de software completo, desde a iniciação.Assim, o projeto já será iniciado como software livre e com as práticas de devops,  ferramentas e tecnologias modernas. Será focado o levantamento das tecnologias e  ferramentas usadas pela comunidade de software livre para automatizar o processo de  desenvolvimento e implantação do software, pois há pouca pesquisa focada nesse tema. O principal objetivo nessa etapa é exercitar em todo ciclo de projeto a experimentação e inovação contínua, de forma a subsidiar a pesquisa realizada na Etapa 5. 



### Metas Específicas

1. __Aplicação de práticas de experimentação e inovação contínua no desenvolvimento do projeto de Catálogo de Software Culturais__

**Cancelado** - Durante a execução do projeto, percebemos que os objetivos desse pacote de trabalho estavam sendo realizados no desenvolvimento da TAIS e do SalicML. Adicionalmente, catálogo de softwares são apresentados atualmente como gitpages dentro das próprias organizações, otimizando a manutenção e evolução. Dessa forma, em conjunto acordo com o Ministério, essa frente foi extinta. Tal decisão foi documentada no relatório de entrega 2 (2 de maio de 2018), página 04, que foi devidamente aprovada pela equipe da gestão do projeto tanto na Unb quanto no Ministério.

2. __Realizar estudos e documentação do processo de desenvolvimento e das boas práticas e automações realizadas__

**Concluído**


**Documentação comprobatória**


3. __Relatório com os  modelos de desenvolvimento e comunidade para serem aplicados aos projetos de software do Minc__
  
**Concluído**


**Documentação comprobatória**


4. __Transferência de conhecimento e capacitar a equipe de servidores e técnicos do MinC em práticas de gestão e desenvolvimento de software aberto, colaborativo e contínuo__

**Concluído**


**Documentação comprobatória**

## Pacote de Trabalho: Estudos sobre práticas de gestão colaborativa em comunidades de software aberto

De acordo com o plano de trabalho, "O principal resultado dessa pesquisa será sistematizar e produzir conhecimento sobre as práticas das comunidades de software livre que o Estado participa por adesão e, a partir dos aprendizados com seus arranjos, orientar e capacitar os servidores e técnicos do MinC nas práticas de 
planejamento, gestão de softwares abertos, aprimorando os mecanismos de governança digital dos softwares presentes no portifólio do MinC".

### Metas Específicas

1. __Estudos de caso sobre comunidades de software livre onde o Estado participa por adesão, com prioridade para os softwares utilizados para a gestão cultural__

**Concluído**


**Documentação comprobatória**

2. __Estudos sobre boas práticas para planejamento conjunto de milestones e releases entre as organizações que fazem parte das comunidades__
**Concluído**


**Documentação comprobatória**

  
3. __Estudos sobre boas práticas de comunicação e mobilização no contexto das comunidades onde o Estado participa__
  
  **Concluído**


**Documentação comprobatória**

4. __Participação em eventos e encontros das comunidades de software livre que contribuem para o portifólio mantido pelo MinC__

**Concluído**


**Documentação comprobatória**
  
5. __Estudos sobre arranjos econômicos utilizados pelas comunidades com fins de sustentabilidade de seus comuns de software__

**Concluído**


**Documentação comprobatória**

6. __Estudos sobre metodologias e suportes tecnológicos para a gestão colaborativa em comunidades de software livre nas quais o Estado participa por adesão__

**Concluído**


**Documentação comprobatória**


## Pacote de Trabalho: Estudo de técnicas de Aprendizado de Máquina para apoiar a fiscalização da Lei Rouanet

De acordo com o plano de trabalho, "O principal objetivo é o estudo de técnicas de Aprendizado de Máquina que possam apoiar o sistema de recomendação e fiscalização da lei Rouanet. Nessa etapa será realizada  uma pesquisa exploratória em técnicas de aprendizado de máquina e processamento de linguagem natural. Tais técnicas e algoritmos serão aplicados para melhorar a experiência de usuário (UX) por meio da proposta de chatbots como interface entre os proponentes na lei Rouanet e o Ministério da Cultura". 

###  Metas específicas

1. __Realizar estudos e propor técnicas de processamento de linguagem natural, aprendizado supervisionado e o desenvolvimento de chatbots para interagir com proponentes da Lei Rouanet__

**Concluído**


**Documentação comprobatória**


2. __Realizar estudos e propor técnicas de aprendizado supervisionado e detecção de anomalias para automatizar as trilhas de auditoria na fase de aprovação e prestação de contas__

**Concluído**


**Documentação comprobatória**

3. __Realizar estudos e propor técnicas de reconhecimento de padrão e Inteligência de Negócio para análise dos projetos submetidos via Lei Rouanet__


**Concluído**


**Documentação comprobatória**

## Pacote de Trabalho: Visualização de dados e criação de Dashboards

De acordo com o plano de trabalho, "O tema deste estudo é buscar formas visuais de apresentar os dados obtidos e 
processados nas etapas anteriores. Os gráficos produzidos servem de embasamentotanto para análise por parte da equipe do projeto quanto pelos gestores do próprio ministério.""

### Metas específicas

1. __Painéis com estatísticas sobre projetos cadastrados no Salic__

**Concluído**


**Documentação comprobatória**

 2. __Estudos sobre a apresentação visual de resultados de algoritmos de aprendizado de máquina e análises estatísticas__ 

 **Concluído**


**Documentação comprobatória**

 
 3. __Dashboard  para a visualização e análise das relações entre proponentes e financiadores por meio de grafos__

 **Concluído**


**Documentação comprobatória**


## Pacote de Trabalho: Estudos dos processos técnicos e gerenciais MinC para aferição e aceitação de produtos de software

De acordo com o plano de trabalho, "O objetivo geral desta frente de pesquisa é auxiliar os times de desenvolvimento e gestores de TI do MinC a aprimorarem sua capacidade em tomar decisões acerca  da qualidade das versões dos produtos de software entregues por seus fornecedores.

Esse pacote de trabalho teve seu cronograma alterado e escopo limitado. Tais mudanças foram registradas no relatório X de acompanhamento, e devidamente aprovados pelo ministério e universidade.



### Metas específicas

1. __Experimentação contínua aplicada à engenharia de produto de software__

 **Concluído**


**Documentação comprobatória**

 
2. __a mineração em repositórios de software e a análise científica de dados do software__

 **Concluído**


**Documentação comprobatória**


 3. __prospectar uma sistemática, baseada em evidência científica, que auxilie  a homologação de produtos de software, em obediência ao normativo estabelecido__

  **Concluído**


**Documentação comprobatória**


# Acompanhamento Financeiro

Tivemos completa transparência quanto ao acompanhamento financeiro do projeto. A prestação de contas foi feita a cada relatório de acompanhamento, no qual apresentamos não só o montante gasto, quanto também o valor gasto por pacote de trabalho. O tamanho do time por frente de trabalho foi definido de acordo com as prioridades estabelecidas pelo ministério, nas reuniões estratégicas. Porém, vale ressaltar, que por se tratar de times multidisciplinares, membros poderiam ser alocados em diferentes frentes por diversas __sprints__ de acordo com necessidade de projeto e deadlines de entrega. 

O financeiro completo do projeto pode ser visto na figura abaixo.


# Assinatura

Responsável pela Execução:
---
Nome:  Carla Silva Rocha Aguiar
             (Coordenadora do Projeto)

Assinatura:

Data:/2019

# Anexos

# Artigos

# 



