#!/usr/bin/env bash

echo "Resetting database ..."

MYSQL="mysql -u admin -padmin"

# rm -rf db.sqlite3
$MYSQL -e "drop database djangoblog"
$MYSQL -e "create database djangoblog"

rm -rf blog/migrations

./manage.py makemigrations
./manage.py makemigrations blog
./manage.py migrate

./manage.py createsuperuser --username admin --email admin@localhost --noinput
scripts/chadminpw.py
