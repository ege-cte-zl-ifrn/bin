#!/bin/bash
#
# Stop the PTD services.

source env.sh

SUFFIX=""
if [[ $1 == "--homologacao" ]]; then
  SUFFIX="-homologacao"
fi

for i in "${DOCKERS[@]}"; do
  sudo systemctl stop "$i$SUFFIX"
done

