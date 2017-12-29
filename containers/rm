#!/bin/bash
#
# Remove the PTD containers.

source env.sh

rm() {
  (docker kill $1 || true) && docker rm $1
}

SUFFIX=""
if [[ $1 == "--homologacao" ]]; then
  SUFFIX="-homologacao"
fi

for i in "${DOCKERS[@]}"; do
  rm "$i$SUFFIX"
done
