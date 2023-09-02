#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
set -x

# create and run any migrations
APP_PATH=/home/fang/src/peopledepot/app docker-compose exec -T web python manage.py makemigrations
APP_PATH=/home/fang/src/peopledepot/app docker-compose exec -T web python manage.py migrate "$@"
