#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST 5432; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata users.json genders.json player_types.json
python manage.py collectstatic --no-input --clear

exec "$@"
