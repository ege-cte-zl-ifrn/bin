pip install -r requirements-app.txt 

if [ "True" = "$DJANGO_DEBUG" ]; then
    python3 manage.py runserver 0.0.0.0:8000
else
    gunicorn \
        wsgi:application \
        --bind 0.0.0.0:8000 \
        --name app \
        --user app \
        --group app \
        --timeout $GUNICORN_TIMEOUT \
        --workers $GUNICORN_NUM_WORKERS \
        --log-level $GUNICORN_LOG_LEVEL \
        --log-file=-
fi
