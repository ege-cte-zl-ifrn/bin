#!/bin/bash
#
# Start the PTD services.

source env.sh

SUFFIX=""
if [[ $1 == "--homologacao" ]]; then
  SUFFIX="-homologacao"
fi

for i in "${DOCKERS[@]}"; do
  sudo systemctl start "$i$SUFFIX"
done

