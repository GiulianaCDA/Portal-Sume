# Portal Sumé

Esse repositório consiste na implementação do backlog proposto no curso de formação de desenvolvedores full stack do lccv. O Portal Sumé permite realizar o cadastro de bens e a visualizar bens já cadastrados. Foi possível utilizar Bootstrap e Angular no front-end. No que tange ao Bootstrap, foram feitas algumas customizações no css padrão a fim de tornar o Portal Sumé uma plataforma mais visualmente agradável aos usuários. Docker e Django foram usados no back-end.

## Tarefas realizadas

1. Integração do front-end com o back-end: as ações de cadastro e remoção de bens realizadas na interface do projeto são aplicadas também no banco de dados.
3. Cadastrar um bem: todo bem cadastrado é armazenado no banco de dados e, após a atualização da página, é listado na aba Bens. 
4. Deletar bem: o ícone de lixeira permite deletar um bem após a confirmação dessa ação.

## Tarefas não realizadas

## Dificuldades 

## Requisitos necessários
1. Angular CLI versão 9.1.13
2. Docker

## Como executar

3. Após obter o repositório e instalar as dependências necessárias, é necessário entrar na pasta front_end e executar o seguinte comando em distribuições Linux:

```
ng serve
```
2. Em seguida, deve-ser entrar na pasta back_end e executar a seguinte instrução para executar docker-compose:

```
docker-compose up
```


