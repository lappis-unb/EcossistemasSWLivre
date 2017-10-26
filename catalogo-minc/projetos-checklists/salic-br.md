# Checklist

## Básico
- Projeto: **Salic**
- Repositório: https://github.com/culturagovbr/salic-br
- Linguagem principal: **PHP**
- Plataforma (web, mobile, desktop, etc): **Web**

## Readme
- [x] Possui readme?
  - Formato do readme (md, txt, rst, etc): **Md.**
- [ ] Badges presentes no readme?

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
  - Docker-compose não está rodando o service 'composer'(Gerenciador de pacotes PHP), e não instala as dependências do compose.json no container da aplicação;
  - Utilizar ferramenta para analizar cobertura de testes do Salic;
  - Docker utiliza imagem do Salic Minc, e deve utiliar uma imagem criada a partir do Salic Br;
