# Django migrations

## Generate and apply migrations

  ```bash
  ./scripts/migrate.sh
  ```

## Roll back migrations to a version

This will undo all migrations after core 0012

  ```bash
  docker-compose exec web python manage.py migrate core 0012
  ```

## Roll back several migrations to regenerate a combined migration file

This will combine the old migration files into a new core 0009.

  ```bash
  docker-compose exec web python manage.py migrate core 0008
  rm app/core/migrations/{0009*,0010*,0011*,0012*,0013*}
  ./scripts/migrate.sh
  ```
