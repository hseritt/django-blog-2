#!/usr/bin/env bash

OPTS=$1

echo "Running Django development server ..."
PYTHON=$(which python)
echo "Using Python: ${PYTHON}"
echo "Python version: $($PYTHON -VV)"

echo "Using opts: ${OPTS}"
$PYTHON manage.py runserver $OPTS
