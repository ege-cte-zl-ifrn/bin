#!/bin/bash
#
# Update all PTD applications to same branch (per default to master branch).

source env.sh

if [[ $# -eq 0 ]]; then
  branch='master'
else
  branch=$1
fi

for f in ../apps/*; do
  if [[ ! -d "$pwd/$f" ]] || [[ -z $(ls "$pwd/$f") ]]; then
    echo_info "Initing submodules..."
    git submodule update --init
  fi

  echo_info "Updating $f..."
  cd "$pwd/$f" && \
    git checkout $branch && \
    git pull origin $branch
  echo
done
