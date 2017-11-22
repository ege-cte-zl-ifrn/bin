#!/bin/bash
#
# Test the PTD applications.

source env.sh

function docker-compose-test()
{
  docker-compose -f docker-compose.yml -f docker-compose.test.yml $@
}

if [[ $# -ne 0 ]]; then
  SERVICES=($1)
fi

docker-compose-test down

sudo mkdir -p $POSTGRESQL_TESTING_VOLUME

sudo mount -t tmpfs -o size=1G tmpfs $POSTGRESQL_TESTING_VOLUME

docker-compose-test up -d db

until docker-compose-test run db psql -h db -U postgres -c '\l' >/dev/null 2>&1; do
  echo_warning "Postgres is unavailable - sleeping"; sleep 1
done

for i in "${SERVICES[@]}"; do
  echo_info "Testing $i..."

  if [[ -f "../apps/$i/.env" ]]; then
    mv ../apps/$i/.env ../apps/$i/.env.original
  fi
  cp ../apps/$i/env.testing ../apps/$i/.env

  docker-compose-test run $i php artisan migrate --seed
  docker-compose-test run $i ./vendor/bin/phpunit --coverage-text
  docker-compose-test run $i php artisan migrate:reset

  if [[ -f "../apps/$i/.env.original" ]]; then
    mv ../apps/$i/.env.original ../apps/$i/.env
  fi
done

docker-compose-test down

sudo umount $POSTGRESQL_TESTING_VOLUME

sudo rm -rf $POSTGRESQL_TESTING_VOLUME

