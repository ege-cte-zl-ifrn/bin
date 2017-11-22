#!/bin/bash
#
# Reload the PTD services.

./stop_services.sh $@
./run.sh $@
./start_services.sh $@

