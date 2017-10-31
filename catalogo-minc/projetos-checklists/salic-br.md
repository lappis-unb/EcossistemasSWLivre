# Checklist

## Básico
- Projeto: **Salic**
- Repositório: https://github.com/culturagovbr/salic-br
- Linguagem principal: **PHP**
- Plataforma (web, mobile, desktop, etc): **Web**

- [x] Possui arquivo de licença ?
  - [x] É open source ?

- [x] Possui arquivo CONTRIBUTING (Guidelines para a contribuição no projeto) ?
- [ ] Possui CODE_OF_CONDUCT (Como se comportar no projeto) ?
- [ ] O nome do projeto é claro e consegue mostrar o que ele faz ?

## Readme
- [x] Possui readme?
  - Formato do readme (md, txt, rst, etc): **Md.**
- [ ] Badges presentes no readme?
- A descrição do projeto responde as seguintes perguntas? :
  - [ ] O que é esse repositório/projeto ?
  - [x] Como o projeto funciona ?
  - [ ] Quem usa/usará esse repositório?
  - [ ] Qual o objetivo do projeto ?
- [x] Existe informação sobre como contatar o time de desnvolvimento ?

## Integração contínua
- [ ] Possui integração contínua?
    - Servidor de integração contínua (travis, circleci, etc):
- [x] Possui testes?
- [ ] Cobertura de testes:
- [ ] Métricas de código (ex: codeclimate):

## Empacotamento
- [ ] É empacotado?
  - Sistema(s) de empacotamento (deb, npm, pip, etc):

## Documentação
- [x] Possui documentação de usuário?
- [x] Possui documentação de código?
  - Formato da documentação (wiki, markdown, rest, doxygen, etc): **Md.**
- [ ] Possui documentação na internet?
  - Endereço:

## Comunidade
- [x] Possui issues abertas no github?
- [x] Possui issues fechadas?
- [x] Já aceitou algum pull request?
  - Número de estrelas: **4**
  - Número de forks: **0**
  - Utiliza a wiki? **Não.**
- [x] A "fila" de issues está atualizada ?
- [ ] Existem labels nas issues ?

## Docker
- [x] Possui Dockerfile?
- [x] Possui Docker compose?
- [x] Presente no Docker hub?
  - Endereço: https://hub.docker.com/r/culturagovbr/salic-br
- [ ] Dockerfile presente no repositório?
- [x] Dockerfile em repositório separado?
  - Endereço: https://github.com/culturagovbr/docker-salic

## Automação
- Gerenciador de tarefas (make, rake, inv, gulp, etc):
- Comando de instalação/dependências?
- Comando:
  - Comando para inicializar serviço/aplicativo?

    Clone o repositório, renomeie "docker-compose.yml_sample" para "docker-compose.yml". Configure os volumes de acordo com sua preferência e rode "docker compose up -d".
  - Comando para executar testes?

    Execute o script `test.sh`, localizado dentro do diretorio tests/bin.
  - Comando para construir a documentação?
  - Comando para empacotar?

## Melhorias
  - Separar solução docker em dois contextos, uma abordagem para desenvolvimento e outra para contexto de produção. Para solução de produção é necessário modularizar os containers: O banco de dados está sendo instalado dentro do mesmo container da aplicação;
  - Melhorar docker-compose.yml: Remover linhas não utilizadas e remover redundancias das linhas build e image;
  - Melhorar script de execução dos testes;
  - É necessaŕio atualizar o docker para utilizar uma versão mais atualizada do PHP e do PHPUnit;
  - Há um comando $PWD no docker-composer que não é reconhecido e por isso não roda o composer. Isso depende da versão do docker-composer. Para consertar, trocar $PWD por '.' no docker-composer.yml.
  - Os testes estão falhando, pois há declarações duplicadas de classes de testes. Mesmo sem a duplicação, há diversos erros e falhas. Acredita-se que seja pela ausência de um banco de teste.
  - Utilizar ferramenta para analizar cobertura de testes do Salic;
  - Docker utiliza imagem do Salic Minc, e deve utiliar uma imagem criada a partir do Salic Br;
