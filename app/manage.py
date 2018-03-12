#!/usr/bin/env python
import os
import sys


def wait_db():
    import psycopg2
    import time
    print('Findind DB...')
    hostname = os.environ.get('POSTGRES_HOST', 'db')
    dbname = os.environ.get('POSTGRES_DB', 'suapsso_db')
    username = os.environ.get('POSTGRES_USER', 'suapsso_user')
    password = os.environ.get('POSTGRES_PASS', 'suapsso_pass')
    while True:
        try:
            conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (hostname, dbname, username, password,))
            print('DB found')
            return
        except Exception as e:
            print('Waiting DB for 1 second...')
            time.sleep(1)
            continue



if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line

    wait_db()

    execute_from_command_line(sys.argv)
