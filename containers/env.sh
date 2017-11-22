#!/bin/bash
#
# Load .env file.

GREEN_COLOR='\033[1;32m'
ORANGE_COLOR='\033[0;33m'
RED_COLOR='\033[0;31m'
BLUE_COLOR='\033[1;34m'
NO_COLOR='\033[0m'

pwd=$(pwd -P)

if [[ ! -f "$pwd/.env" ]]; then
  cp $pwd/env.example $pwd/.env
fi

source "$pwd/.env"

echo_warning() {
  echo ${@:3} -e "$ORANGE_COLOR$1$NO_COLOR"
}

echo_danger() {
  echo ${@:3} -e "$RED_COLOR$1$NO_COLOR"
}

echo_info() {
  echo ${@:3} -e "$BLUE_COLOR$1$NO_COLOR"
}

echo_success() {
  echo ${@:3} -e "$GREEN_COLOR$1$NO_COLOR"
}
