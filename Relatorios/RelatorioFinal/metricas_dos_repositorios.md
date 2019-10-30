### Análise das métricas dos repositórios

Com o intuito de compreender a dinâmica de desenvolvimento e a qualidade de cada uma das soluções de software desenvolvidas durante o período do projeto, foi realizada uma análise das métricas dos repositórios onde estão hospedados os códigos fonte e a respectiva documentação.

É importante ressaltar o fato de todos os softwares terem sido desenvolvidos como softwares livres sob a licença recíproca total *GNU General Public License* versão *3*, o que permite acesso público à todo o código.

Estão contemplados nesta análise 8 repositórios, sendo eles:

1. **Tais:** A Tais (Tecnologia de Aprendizado Interativo do Salic) é um chatbot desenvolvido para o projeto da Lei Rouanet com o objetivo de ajudar os proponentes nos momentos de dúvida. A Tais é baseada no framework Rasa. Disponível em: https://github.com/lappis-unb/tais. 
2. **Rasa-ptbr-Boilerplate:**  Projeto feito com a tecnologia  Rasa incluindo as configurações iniciais necessárias para a construção de um projeto chatbot. Disponível em: https://github.com/lappis-unb/rasa-ptbr-boilerplate.
3. **BotFlow:** O BotFlow é uma plataforma criada para facilitar a criação e edição de conteúdos para o desenvolvimento de ChatBots que utilizam o framework Rasa. Neste repositório estão os códigos referentes à camada de visualização (*Front-end*). Disponível em: https://github.com/lappis-unb/BotFlow.
4. **BotFlowAPI:** O BotFlowAPI é a API baseada no protocolo REST para permitir o funcionamento do BotFlow. Disponível em: https://github.com/lappis-unb/BotFlowAPI.
5. **Promova Cultura:** O PromovaCultura tem como objetivo principal desenvolver visualizações de dados sobre a Lei Federal de Incentivo à Cultura. Disponível em: https://github.com/lappis-unb/PromovaCultura.
6. **SalicML:** Módulo para análise dos dados do Salic por meio de algoritmos de aprendizagem de máquina . Disponível em: https://github.com/lappis-unb/salic-ml.
7. **SalicAPI:** API aberta para o sistema SALIC. Tem por objetivo expor os dados de projetos da lei Rouanet. Disponível em: https://github.com/lappis-unb/salic-api.
8. **SailcMLFrontEnd:** Protótipo de front-end para o módulo SalicML. Disponível em: https://github.com/lappis-unb/salic-ml-frontend.

#### Métricas Gerais 
Iniciamos a análise dos repositórios apontando três métricas gerais, juntamente com as linguagens predominantes utilizadas na solução:

* **Número de linhas de código (LOC):** quantidade total de linhas de código  do projeto indicando, em parte, sua complexidade.
* **Número de contribuidores:** quantidade de pessoas que contribuiram diretamente com o código do projeto.
* **Esforço em meses:** quantidade de tempo pela qual a equipe trabalhou no projeto.

Repositório	|	Linhas de Código	|	Número de Contribuidores	|	Esforço em Meses	|	Linguagem predomintante
-	|	:-:	|	:-:	|	:-:	|	:-:
**Tais**	|	15085	|	34	|	19	|	Python/Markdown/Jupyter Notebook
**Rasa-ptbr-Boilerplate**	|	5397	|	17	|	8	|	Markdown
**BotFlow**	|	4117	|	10	|	3	|	JavaScript
**BotFlow API**	|	2062	|	11	|	4	|	Python
**Promova Cultura**	|	103368	|	11	|	18	|	JavaScript
**Salic-ML**	|	80268	|	14	|	18	|	Python/Jupyter Notebook / Markdown
**Sailc ML FrontEnd**	|	20675	|	6	|	13	|	Vue / JavaScript
**Salic API**	|	9786	|	15	|	-	|	Python

Neste caso, se destacam os projetos Promova Cultura, Salic-ML, Sailc ML FrontEnd e Tais como os de maior complexidade, o que é apontado pelo número de linhas de código e consequentemente os que tiveram maior tempo de esforço da equipe. 

Em seguida, consideramos outras 5 métricas que apontam o volume de trabalho e fornecem uma noção da complexidade do projeto:

* **Número de Commits:** indicam o número de grupos de alterações no código fonte, sendo um indicador do volume de atividades realizadas ao longo do projeto.
* **Número de Arquivos:** quantidade total de arquivos do projeto indicando, em parte, sua complexidade.
* **Número de linhas adicionadas / removidas:** quantidade de linhas de código adicionadas e removidas durante o período do projeto, indicando a quantidade de trabalho realizada incluindo melhorias à partir de refatoração do código.
* **Média de Linhas modificadas por commit:** esta métrica indica a quantidade média de modificações realizadas à cada nova versão do sistema. Este é um importante indicador de boas práticas de desenvolvimeto, uma vez que novas submissões devem passar por revisão e, se forem muito extensas, dificultam sua avaliação e extendem o tempo necessários para as mesmas serem integradas à base de código e estarem disponíveis para os demais desenvolvedores. 


Repositório	|	Número de Arquivos	|	Número de Commits	|	Número de Linhas Adicionadas / Linhas Removidas	|	Média de Linhas modificadas por commit
-	|	:-:	|	:-:	|	:-:	|	:-:
**Tais**	|	224	|	1441	|	167750 / 166147	|	232
**Rasa-ptbr-Boilerplate**	|	62	|	297	|	30689 / 23840	|	184
**BotFlow**	|	82	|	291	|	41078 / 35942	|	265
**BotFlow API**	|	50	|	152	|	5947 / 3414	|	62
**Promova Cultura**	|	133	|	229	|	800202 / 669861	|	6419
**Salic-ML**	|	203	|	638	|	3150841 / 3076296	|	9760
**Sailc ML FrontEnd**	|	38	|	113	|	43966 / 23038	|	593
**Salic API**	|	156	|	399	|	69973 / 57328	|	319






* **Quantidade de *Pull Requests*:** indicam a quantidade de submissões de alterações no código fonte. Associada ao número de commits, esta métrica demonstra o volume de atividades realizadas e também indica a boa prática de revisão de códigos submetidos antes das modificações serem aceitas.
* **Quantidade de issues abertas/fechadas:** 


Repositório	|	Quantidade de Pull Requests (Abertos/Fechados)	|	Número de Issues (Abertas / Fechadas)
-	|	:-:	|	:-:
**Tais**	|	0 / 158	|	39 / 387
**Rasa-ptbr-Boilerplate**	|	1 / 55	|	15 / 44
**BotFlow**	|	1 / 54	|	34 / 50
**BotFlow API**	|	0 / 24	|	0 / 0
**Promova Cultura**	|	1 / 78	|	19 / 157
**Salic-ML**	|	0 / 89	|	38 / 292
**Sailc ML FrontEnd**	|	1 / 17	|	0 / 0
**Salic API**	|	2/31	|	17/53



* **Forks:** A repositories stars might not always represent an intrinsic value. Forks on the other hand show how many community members also keep a personal copy of the repository, oftentimes this is to add their own derivative customizations and sometimes this is to contribute back to the original repository. (Ref. https://medium.appbase.io/analyzing-20k-github-repositories-af76de21c3fc)
* **Estrelas:** Github stars are similar to Facebook likes, they tell us how the community rates the code that is hosted on Github. Our first chart is a distribution of the 🔝 20k repositories based on their stars. (Ref. https://medium.appbase.io/analyzing-20k-github-repositories-af76de21c3fc)


Repositório	|	Forks	|	Número de Estrelas
-	|	:-:	|	:-:
**Tais**	|	26	|	28
**Rasa-ptbr-Boilerplate**	|	65	|	42
**BotFlow**	|	2	|	9
**BotFlow API**	|	1	|	3
**Promova Cultura**	|	0	|	5
**Salic-ML**	|	0	|	4
**Sailc ML FrontEnd**	|	0	|	0
**Salic API**	|	4	|	2