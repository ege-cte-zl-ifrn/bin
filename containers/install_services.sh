#!/bin/bash
#
# Install the PTD services.

source env.sh

for i in "${DOCKERS[@]}"; do
  cd "$pwd/$i"
  ./install-service.sh $@
done
