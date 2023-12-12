#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
set -x

export DEBUG=2
export SECRET_KEY=foo
export DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1 [::1]"
export DJANGO_SUPERUSER_USERNAME=admin
export DJANGO_SUPERUSER_EMAIL=admin@admin.com
export DJANGO_SUPERUSER_PASSWORD=admin
# SQL_ENGINE=django.db.backends.postgresql
# SQL_DATABASE=people_depot_dev
# SQL_USER=people_depot2
# SQL_PASSWORD=people_depot
# SQL_HOST=db
# SQL_PORT=5432
export DATABASE=postgres

export COGNITO_AWS_REGION=us-west-2
export COGNITO_USER_POOL=us-west-2_Fn4rkZpuB
