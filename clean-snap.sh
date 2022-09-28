#!/bin/bash
#https://randomblog.hu/how-to-free-up-disk-space-on-ubuntu-when-your-root-partition-is-almost-full/

set -eu
 LANG=en_US.UTF-8 snap list --all | awk '/disabled/{print $1, $3}' |
     while read snapname revision; do
         sudo snap remove "$snapname" --revision="$revision"
     done
