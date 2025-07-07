#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: ./ping_check.sh <host1> <host2> ..."
  exit 1
fi

for host in "$@"
do
  echo "------------------------------"
  echo "Pinging $host..."
  ping -n 3 $host
  echo ""
done
