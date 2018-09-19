#!/usr/bin/env bash
cd /apps/suapsso
pip install -e /apps/ege_django_theme
python3 manage.py runserver 0.0.0.0:8000

