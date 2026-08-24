#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
printf '%s\n' "$RSCTF_FLAG" > /flag.txt
chown root:root /flag.txt
chmod 0444 /flag.txt
unset RSCTF_FLAG
exec "$@"
