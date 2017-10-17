# Checklist

## Básico
- Projeto: Mapas Culturais
- Repositório: https://github.com/culturagovbr/mapasculturais
- Linguagem principal:  PHP
- Plataforma (web, mobile, desktop, etc): Web

## Readme
- [x] Possui readme?
  - Formato do readme (md, txt, rst, etc): md
- [x] Badges presentes no readme?

## Integração contínua
- [x] Possui integração contínua?
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
   - https://github.com/culturagovbr/mapasculturais/blob/master/documentation/docs/mc_developer_guide.md
- Formato da documentação (wiki, markdown, rest, doxygen, etc): md
- [x] Possui documentação na internet?
  - Endereço: https://pt.wikiversity.org/wiki/Mapas_Culturais_-_software_livre_e_colabora%C3%A7%C3%A3o
    * https://institutotim.org.br/project/mapas-culturais/

## Comunidade
- [x] Possui issues abertas no github?
- [x] Possui issues fechadas?
- [x] Já aceitou algum pull request?
  - Número de estrelas: 5
  - Número de forks: 76
  - Utiliza a wiki?: Não

## Docker
- [x] Possui Dockerfile?
- [x] Possui Docker compose?
- [x] Presente no Docker hub?
  * https://hub.docker.com/r/culturagovbr/mapasculturais/
- [x] Dockerfile presente no repositório?
- [ ] Dockerfile em repositório separado?
  - Endereço:

OBS: Falta referencia a documentação do docker no doc de deploy e/ou no readme

## Automação
- Gerenciador de tarefas (make, rake, inv, gulp, etc):
- Comando de instalação/dependências?
      * https://github.com/culturagovbr/mapasculturais/blob/master/documentation/docs/mc_deploy.md#1-softwares-requeridos

- Comando:
  - Comando para inicializar serviço/aplicativo?
  - Comando para executar testes?
  - Comando para construir a documentação?
    *   https://github.com/culturagovbr/mapasculturais/blob/master/documentation/readme.md#how-to-get-this-documentation

            mkdocs serve
            mkdocs build
  - Comando para empacotar?
