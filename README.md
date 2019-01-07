# EGE - Build



## Objetivo

O EGE é um Ecossistema de Gestão Educacional feito em Django usando vários microserviços, portanto, para facilitar o desenvolvimento criamos este 
project com o propósito de ajuda no processo de desenvolvimento e implantação.


## Iniciando o projeto
```
git clone https://github.com/CoticEaDIFRN/ege_build.git
cd ege_build
git submodule update --init
cd bin
cp example.env .env
cp acesso_example.env .acesso.env
./_deploy
./db_up
./proxy_up

# em outra janela
./acesso_up

# em mais uma janela
./perfil_up
``` 

## Testar

Acesse http://localhost/  e, quando solicitado, informe o usuário e senha do superusário que você criou, caso tenha deixado o deploy criar o usuário será ```admin``` e a senha será ```admin```.
