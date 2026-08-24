#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"

flag_path="/flag_$(cat /proc/sys/kernel/random/uuid).txt"
umask 022
printf '%s\n' "$RSCTF_FLAG" > "$flag_path"
chown root:root "$flag_path"
chmod 0444 "$flag_path"
unset RSCTF_FLAG flag_path

exec setpriv --reuid=ctf --regid=ctf --init-groups \
  dotnet /app/CRUD.dll --urls http://0.0.0.0:8181
