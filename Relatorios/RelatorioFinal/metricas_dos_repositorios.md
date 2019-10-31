### Análise das métricas dos repositórios

Com o intuito de compreender a dinâmica de desenvolvimento e a qualidade de cada uma das soluções de software desenvolvidas durante o período do projeto, foi realizada uma análise das métricas dos repositórios onde estão hospedados os códigos fonte e as respectivas documentações.

É importante ressaltar o fato de todos os softwares terem sido desenvolvidos como softwares livres sob a licença recíproca total *GNU General Public License* versão *3*, o que permite acesso público à todo o código bem como todos os direitos intrínsicos ao software livre.

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
Iniciamos a análise dos repositórios apontando três métricas gerais, sendo elas:

* **Número de linhas de código (LOC):** quantidade total de linhas de código  do projeto indicando, em parte, sua complexidade.
* **Número de contribuidores:** quantidade de pessoas que contribuiram diretamente com o código do projeto.
* **Esforço em meses:** quantidade de tempo pela qual a equipe trabalhou no projeto.

A tabela abaixo apresenta estas métricas juntamente com as linguagens de programação predominantes utilizadas em cada uma das soluções para ajudar a contextualizar as tecnologias de cada projeto.

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

Neste caso, destacam-se os projetos *Promova Cultura*, *Salic-ML*, *Sailc ML FrontEnd* e *Tais* como os de maior complexidade, o que é apontado pelo número de linhas de código e, consequentemente, os que tiveram maior tempo de dedicação da equipe. Considerando que todos as soluções são aplicações para serem executadas em servidor *web* com acesso via browser ou via API,  observa ainda o caráter inovador dos projeto que adotam de menira predominante as linguagens de progeamação que estão hoje (Ano base 2019) com o maior crescimento de adoção no mercado (https://www.sciencealert.com/master-website-programming-with-these-ten-amazing-deals, https://www.geeksforgeeks.org/top-10-programming-languages-of-the-world-2019-to-begin-with/).

#### Métricas de volume de trabalho

Em seguida, consideramos outras 4 métricas que apontam o volume de trabalho e fornecem uma noção da complexidade do projeto:

* **Número de Commits:** indicam o número de grupos de alterações no código fonte, sendo um indicador do volume de atividades realizadas ao longo do projeto.
* **Número de Arquivos:** quantidade total de arquivos do projeto indicando, em parte, sua complexidade.
* **Número de linhas adicionadas / removidas:** quantidade de linhas de código adicionadas e removidas durante o período do projeto, indicando a quantidade de trabalho realizada incluindo melhorias à partir de refatoração do código.
* **Média de Linhas modificadas por commit:** esta métrica indica a quantidade média de modificações realizadas à cada nova versão do sistema. Este é um importante indicador de boas práticas de desenvolvimeto, uma vez que novas submissões devem passar por revisão e, se forem muito extensas, dificultam sua avaliação e extendem o tempo necessários para as mesmas serem integradas à base de código e estarem disponíveis para os demais desenvolvedores. 

Neste caso, se observa na tabela à seguir o grande volume de *commits* e alterações de código realizadas ao longo do desenvolvimetno de cada um dos projetos.

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

Considerando que a *Média de Linhas modificadas por commit* ainda representa um valor considerado alto de modificações cuja qualidade possa ser mais facilmente analisada e rastreada, levantou-se um histograma, mostrando, de maneira mais granular, a frequência de commits com a respectiva quantidade de modificações conforme pode ser observado na figura abaixo.

![Histograma de commits](figs/histograma_commits.pdf)

Neste caso, é possível observar que 40% dos commits não passa de 50 linhas modificadas. Na prática 63% dos commits altera até 150 linhas. Se observa ainda que em torno de 20% dos commits realizam alterações acima de 500 linhas por commit e, em análise pontual, foi possível observar que em sua maioria representam inclusões de bibliotecas externas ou mesmo arquivos de dados para treinamento de modelos de Machine Learning que podem chegar a até 20 mil linhas, cada um. Conclui-se então que, em sua maioria, os commits realizados estão seguindo as boas práticas de fazerem alterações pequenas de mais fácil compreensão e rastreamento.

#### Métricas de boas práticas de Eng. de Software

Para avaliar boas práticas no desenvolvimento das soluções de software, são consideradas 3 métricas gerais conforme à seguir:

* **Quantidade de *Pull Requests*:** indicam a quantidade de submissões de alterações no código fonte. Associada ao número de commits, esta métrica demonstra o volume de atividades realizadas e também indica a boa prática de revisão de códigos submetidos antes das modificações serem aceitas.
* **Quantidade de issues abertas/fechadas:** a *issues* de um repositório documentam tanto os requisitos do projeto em sua fase de desenvolvimento quanto necesisdades de evolução e necessidades de correções (*bugs*) observados em seu funcionamento. Seu propósito é socializar estas tarefas a serem realizadas, designar responsáveis, bem como deixar transparendo o que está sendo desenvolvido através da documentação do processo de construção do software.
* **Pipeline de CI/CD:** configuração das técnicas de integração contínua (CI) e deploy contúnuo (CD) mostrando a maturidade do processo de desenvolvimento e manutenção da solução de software.

  
Neste caso, a tabela à seguir aponta estas métricas em cada um dos repositórios onde é possível observar que praticamente todos eles adotaram as boas práticas de documentar *issues* nos repositórios e distribuí-las entre os membros da equipe, socializando o conhecimento e documentando a evolução do software. Os dois repositórios que não contém *issues* cadastradas (*BotFlowAPI* e *Sailc ML FrontEnd*) tiveram suas *issues* gerenciadas em nos repositórios equivalentes em suas frentes de trabalho. Uma outra boa prática observada é o uso do mecanismo de *Pull Request* onde as submissões de alterações no código são feitas para o repositório e tem que ser aprovadas por outros membros do projeto, incentivando a revisão do código, bem como ampliando o conhecimento de toda a equipe sobre a base se código que está sendo desenvolvida. Por fim, a configuração do pipeline de CI/CD em praticament todos os repositórios demonstra a maturidade da solução de software com testes automatizados e métricas de análise estática de código. Este pipeline aumenta a confiança da equipe em realiar modificações em uma grande base de código uma vez que os testes podem apontar falhas antes que submissões novas possam ser aceitas.

Repositório	|	Quantidade de Pull Requests (Abertos/Fechados)	|	Número de Issues (Abertas / Fechadas)	|	Pipeline CI/CD
-	|	:-:	|	:-:	|	:-:
**Tais**	|	0 / 158	|	39 / 387	|	GitlabCI / CD
**Rasa-ptbr-Boilerplate**	|	1 / 55	|	15 / 44	|	GitlabCI 
**BotFlow**	|	1 / 54	|	34 / 50	|	TravisCI
**BotFlow API**	|	0 / 24	|	0 / 0	|	-
**Promova Cultura**	|	1 / 78	|	19 / 157	|	-
**Salic-ML**	|	0 / 89	|	38 / 292	|	GitlabCI
**Sailc ML FrontEnd**	|	1 / 17	|	0 / 0	|	GitlabCI / TravisCI
**Salic API**	|	2/31	|	17/53	|	GitlabCI

#### Métricas de adoção pela comunidade

Duas métricas importantes para avaliar a adoção do software livre pela comunidade são o número de *Estrelas* e o número de *Forks* nos reposirótios conforme explicados à seguir:

* **Estrelas:** O número de estrelas em um repositório demonstra como a comunidade classifica cada um dos projetos. Quanto maior é o número, mais visível é o projeto da comunidade. (Ref. https://medium.appbase.io/analyzing-20k-github-repositories-af76de21c3fc)
* **Forks:** Os *Forks* representam as cópias do repositório feita por membros da comunidade. Um *fork* pode ser feito por membros da comunidade tanto para que contribuam para o projeto original (atrávés de *Pull Requests* / *Merge Requests*) quanto para a realização de derivações do projeto original em outras soluções. (Ref. https://medium.appbase.io/analyzing-20k-github-repositories-af76de21c3fc)

A tabela à seguir apresenta estas duas métricas para cada um dos repositórios juntamente com a data de criação de cada um dos projetos. Pela tabela, é possível observar que projetos com caráter mais interno como os do Salic tem menos adoção da comunidade, enquanto projetos cuja base de código pode ser aproveitada por outros órgãos como a *Tais* e o *Rasa-ptbr-Boilerplate* apresentam um índice de adoção da comunidade bem mais alto. O destaque aqui fica com o projeto *Rasa-ptbr-Boilerplate* que foi baseado na experiência da *Tais* e, mesmo tendo sido desenvolvido só em 2019, já possui 65 *Forks* mostrando uma ótima adoção da comunidade. Além disso, pode ser observado que os projetos do *BotFlow* / *BotFlowAPI* que foram iniciados em meados de 2019 e só tiveram sua primeira versão estável em set/2019 também já contam com *Forks* da comunidade.

Repositório	|	Forks	|	Número de Estrelas	|	Data de Criação
-	|	:-:	|	:-:	|	:-:
**Tais**	|	26	|	28	|	21/03/2018
**Rasa-ptbr-Boilerplate**	|	65	|	42	|	21/01/2019
**BotFlow**	|	2	|	9	|	03/06/2019
**BotFlow API**	|	1	|	3	|	21/05/2019
**Promova Cultura**	|	0	|	5	|	21/03/2018
**Salic-ML**	|	0	|	4	|	21/03/2018
**Sailc ML FrontEnd**	|	0	|	0	|	27/08/2018
**Salic API**	|	4	|	2	|	10/01/2018

#### Documentação dos repositórios

Por fim, foi realizada uma análise da documentação dos projetos nos respectivos repositórios. Foi identificado que todos adotam a boa prática de ter a documentação resumida no arquivo *Readme.md* na raiz de cada repositório. Neste arquivo, em todos os repositórios estão contidas as descrições gerais da solução e instruções de como executar o software. Além disso, a maioria dos projetos também descreve a arquitetura e tecnologias envolvidas já no arquivo *Readme.md*. 

Documentações mais detalhadas de cada uma das soluções estão disponíveis na *Wiki* de cada repositório. Damos destaque aqui aos projetos que extrapolam a documentação formal de arquitetura e descrição geral da solução e incluem a documentação de tutoriais e de todo o processo de aprendizagem durante o desenvolvimento do produto de software:

* *Tais* (https://lappis-unb.github.io/tais
* *Rasa-ptbr-Boilerplate* (https://docs.rasaboilerplate.lappis.rocks)
* *Promova Cultura* (https://lappis-unb.github.io/PromovaCultura/)
* *Salic-ML* (https://lappis-unb.github.io/salic-ml-frontend/)
* *Salic-API* (https://salic-api.readthedocs.io/pt/latest/)