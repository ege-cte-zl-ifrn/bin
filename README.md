# EGE - Build



## Objetivo

O EGE é um Ecossistema de Gestão Educacional feito em Django usando vários microserviços, portanto, para facilitar o desenvolvimento criamos este 
project com o propósito de ajuda no processo de desenvolvimento e implantação.


## Iniciando o projeto
```bash
git clone https://github.com/CoticEaDIFRN/ege_build.git

cd ege_build/conf
cp example.env .env
cp example_acesso.env .acesso.env
cp example_perfil.env .perfil.env
cp example_processo_seletivo.env .processo_seletivo.env
cp example_selecao.env .selecao.env
cp example_integrador_ms.env .integrador_ms.env
cp example_integrador_ui.env .integrador_ui.env
# caso queira usar LDAP
# cp example_acesso_ldap.env .acesso_ldap.env
# caso NÃO queira usar LDAP
# echo "" > .acesso_ldap.env

git submodule update --init
cd ege_build/bin
./_deploy
./db_up

# em outra janela, o acesso é obrigatório
./acesso_up

# em mais uma janela, o perfil é desejável
./perfil_up

# em mais uma janela, caso queira desenvolver o processo_seletivo
./seletivo_up

./proxy_up
``` 

## Testar

Acesse http://localhost/  e, quando solicitado, informe o usuário e senha do superusário que você criou, caso tenha deixado o deploy criar o usuário será ```admin``` e a senha será ```admin```.

## Observação

Antes de fazer qualquer alteração em um dos APPS, é necessário certificar-se de que está trabalhando na branch adequada.
