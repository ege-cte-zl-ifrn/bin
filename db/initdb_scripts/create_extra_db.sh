#!/usr/bin/env sh
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_acesso
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_baggins
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_perfil
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_seletivo
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_selecao
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_integrador_ms
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_integrador_ui
createdb -e -U $POSTGRES_USER -O $POSTGRES_USER sead_dashboard
