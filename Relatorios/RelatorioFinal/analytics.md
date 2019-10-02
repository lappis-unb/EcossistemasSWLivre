**Concluído**

Através de uma demanda combinada com o antigo Ministério da Cultura, atual Secretaria Especial da Cultura do Ministério da Cidadania, foi criada uma equipe para atuar no campo de pesquisa e desenvolvimento na área de *business intelligence* (BI). Frente de trabalho responsável por elaborar visualizações dos dados provenientes da interação dos usuários com a Tais.

Com muita empolgação e dedicação, por ser uma nova área de atuação dentro do LAPPIS, a equipe começou pesquisando sobre quais métricas são relevantes coletar a partir da interação do *usuário vs Tais*, fornecendo dados tanto para equipe de desenvolvimento do *chatbot*, facilitando na manutenção e evolução da Tais, e gerando dados para a equipe de negócios, comprovando os objetivos da implementação do projeto.

Após a pesquisa sobre as métricas, um estudo teve que ser realizado sobre quais tecnologias seriam utilizadas para armazenar e elaborar as visualizações propostas, seguindo a cultura do laboratório de utilização de *software*. Foi então selecionado o *ElasticSearch*, como sendo a ferramenta de armazenamento de dados, que também trabalha com buscas em tempo real e faz o armazenamento em cache das pesquisas já realizadas. Para consumir os dados armazenados no Elastic e tratá-los para disponbilizar em formato de visualizações, foi utilizado o *Kibana*, um dos componentes da *ElasticStack*. Essa ferramenta fornece recursos para elaboração de dashboards e visualizações.

Subsequente à escolha das tecnologias, a equipe atuou na implementação de todas as visualizações propostas. Foram dividas em dois grupos, métricas de desenvolvimento e de negócio, sendo disponibilizadas respectivamente em dois *dashboards* distintos, *Paloma's* e *Perfil de Usuário*.

Com a finalização da etapa de implementação, foi automatizado o processo de importação dos *dashboards* contendo as visualizações a partir de um único comando, evitando um retrabalho e garantindo uma entrega de excelência.

**Conclusão**

- [Estudo sobre métricas](https://github.com/lappis-unb/tais/wiki/Estudo-sobre-metricas-para-bots)

- [Automação do processo de importação](https://github.com/lappis-unb/rasa-ptbr-boilerplate/blob/master/analytics/import_dashboards.py)

- [Stack do Elastic/Kibana](https://github.com/lappis-unb/tais/blob/master/README.md)
