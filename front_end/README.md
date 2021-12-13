# CRM Portal Sumé

Adaptação do Portal Sumé para Angular para a atividade proposta. 

Este projeto foi gerado com [Angular CLI](https://github.com/angular/angular-cli) versão 9.1.13.


## Como executar

1. É necessário executar o seguinte comando em distribuições Linux:

```
ng serve
```
2. Em seguida, deve-se abrir outra aba no terminal e executar o json server, a partir da instrução:

```
json-server --watch db.json
```

Após o Portal Sumé ser carregado, é possível clicar em "Cadastrar Bem", onde será visto o componente principal da página. Na aba Bens, há uma tabela que permite a visualização do Tombamento (gerado a partir do ano de término + 123456), Data de cadastro, registrada no momento em que o bem foi adicionado, e o valor de cada um dos bens. É possível cadastrar um novo bem clicando no ícone '+'. Além disso, também há uma opção para deletar bens.
