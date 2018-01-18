# Checklist

## Básico
- Projeto: VerSalic
- Repositório: https://github.com/mateuswetah/Projeto-Salic
- Linguagem principal:  TypeScript
- Plataforma (web, mobile, desktop, etc): Web

- [x] Possui licença? GPLv3
  - [x] É open source?

- [ ] Possui arquivo CONTRIBUTING (Guidelines para a contribuição no projeto)?
- [ ] Possui CODE_OF_CONDUCT (Como se comportar no projeto)?
- [x] O nome do projeto é claro e consegue mostrar o que ele faz?


## Readme
- [x] Possui readme?
  - Formato do readme (md, txt, rst, etc): md
- [ ] Badges presentes no readme?
- A descrição do projeto responde as seguintes perguntas? :
  - [x] O que é esse repositório/projeto?
  - [ ] Como o projeto funciona? Não, mas menciona a API usada.
  - [ ] Quem usa/usará esse repositório?
  - [x] Qual o objetivo do projeto?
- [ ] Existe informação sobre como contatar o time de desenvolvimento?



## Integração contínua
- [ ] Possui integração contínua?
    - Servidor de integração contínua (travis, circleci, etc):
- [ ] Possui testes?
- [ ] Cobertura de testes:
- [ ] Métricas de código (ex: codeclimate):

## Empacotamento
- [ ] É empacotado?
  - Sistema(s) de empacotamento (deb, npm, pip, etc):

## Documentação
- [ ] Possui documentação de usuário?
- [ ] Possui documentação de código?
- Formato da documentação (wiki, markdown, rest, doxygen, etc): md
- [ ] Possui documentação na internet?

## Comunidade
- [x] Possui issues abertas no github?
- [x] Possui issues fechadas?
- [x] Já aceitou algum pull request?
  - Número de estrelas: 3
  - Número de forks: 4
  - Utiliza a wiki?: Sim
- [x] A "fila" de issues está atualizada ?
  - [ ] Existem labels nas issues ?

## Docker
- [x] Possui Dockerfile?
- [ ] Possui Docker compose?
- [ ] Presente no Docker hub?
- [x] Dockerfile presente no repositório?
- [ ] Dockerfile em repositório separado?

## Automação
- Gerenciador de tarefas (make, rake, inv, gulp, etc):
- Comando de instalação/dependências?

    Caso se utilize o Docker, criar/executar a imagem do projeto instalará todas as dependências. Caso contrário, o comando abaixo instalará os modulos necessários de acordo com o arquivo de configuracao `packages.json`, desde que se esteja na pasta do projeto.
    ```
    $ npm install
    ```

    Mais detalhes: https://github.com/mateuswetah/Projeto-Salic/blob/master/README.md

- Comando:
  - Comando para inicializar serviço/aplicativo?

    O comando abaixo executa a aplicação num servidor local.
    ```
    $ ng serve --host 0.0.0.0
    ``` 

  - Comando para executar testes?
  - Comando para construir a documentação?
  - Comando para empacotar?
