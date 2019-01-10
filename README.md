# EGE - Build



## Objetivo

O EGE é um Ecossistema de Gestão Educacional feito em Django usando vários microserviços, portanto, para facilitar o desenvolvimento criamos este 
project com o propósito de ajuda no processo de desenvolvimento e implantação.


## Iniciando o projeto
```bash
git clone https://github.com/CoticEaDIFRN/ege_build.git
git submodule update --init
./_deploy
./db_up

# em outra janela, o acesso é obrigatório
./acesso_up

# em mais uma janela, o perfil é desejável
./perfil_up

# em mais uma janela, caso queira desenvolver o processo_seletivo
./seletivo_up

# recomendamos que o proxy_up só seja executado depois que as outras aplicações terminarem o UP
./proxy_up
``` 


### Caso queiras usar LDAP

```bash

cp conf/examples/acesso_ldap.env conf/.acesso_ldap.env

```

Recomendamos que, antes de alterar um código coloque em uma branch, no caso, se quiseres usar a branch master use o script abaixo.
```bash
# estando em bin
./_to_branch master

```

## Testar

Acesse http://localhost/  e, quando solicitado, informe o usuário e senha do superusário que você criou, caso tenha deixado o deploy criar o usuário será ```admin``` e a senha será ```admin```.

## Observação

Antes de fazer qualquer alteração em um dos APPS, é necessário certificar-se de que está trabalhando na branch adequada.
