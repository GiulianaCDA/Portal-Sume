
# Portal Sumé
O Portal Sumé permite realizar o cadastro de bens e a visualizar bens já cadastrados. Foi possível utilizar Bootstrap e Angular no front-end. No que tange ao Bootstrap, foram feitas algumas customizações no css padrão a fim de tornar o Portal Sumé uma plataforma mais visualmente agradável aos usuários. Docker e Django foram usados no back-end.

## Tarefas realizadas

1. Integração do front-end com o back-end: as ações de cadastro e remoção de bens realizadas na interface do projeto são aplicadas também no banco de dados.
3. Cadastrar um bem: todo bem cadastrado é armazenado no banco de dados e, após a atualização da página, é listado na aba Bens. 
4. Deletar bem: o ícone de lixeira permite deletar um bem após a confirmação dessa ação.
2. Criação dos componentes no Angular
3. Configuração do FormGroup
4. Cadastrar um bem: O bem é cadastrado no arquivo json
5. Deletar bem: o ícone de lixeira permite deletar um item do banco de dados.
6. Criação e configuração do PostgreSQL
7. Campos de 'Fornecedor' e 'Notas Fiscais' na aba Geral são capazes de listar os dados contidos no banco. 
8. Criação da API

## Tarefas não realizadas
1. Aplicação das regras de negócio
2. Cadastro de bens no banco de dados
3. Listar valores dos campos 'Nota fiscal' de acordo com o Fornecedor escolhido

## Dificuldades 

1. Compreender itens contidos no Backlog, como composição do 'Tombamento' e algumas regras de negócio
2. Integrar o back-end com o front-end, foi necessária a utilização do Django Cors
3. Relacionar inputs 'Fornecedor', 'Nota Fiscal' e 'Item da Nota Fiscal' no formulário
4. Criar novos elementos em tabelas com muitas chaves estrangeiras

## Requisitos necessários
1. Angular CLI versão 9.1.13
2. Docker

## Como executar
1. Após obter o repositório, é necessário entrar na pasta front_end e executar a seguinte instrução em distribuições Linux:

```
ng serve
```
2. Em seguida, deve-se entrar na pasta back_end e executar o comando:
```
docker-compose up
```

Após isso, o Portal Sumé pode ser acessado no endereço http://localhost:4200/
