#!/bin/bash
#
# Install the PTD services.

source env.sh

./stop_services.sh $@

SUFFIX=""
if [[ $1 == "--homologacao" ]]; then
  SUFFIX="-homologacao"
fi

for i in "${DOCKERS[@]}"; do
  sudo systemctl disable /etc/systemd/system/$i$SUFFIX.service && \
    sudo rm /etc/systemd/system/$i$SUFFIX.service
done
