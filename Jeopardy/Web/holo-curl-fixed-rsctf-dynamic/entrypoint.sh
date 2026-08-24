#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
umask 077
printf '%s\n' "$RSCTF_FLAG" > /root/flag.txt
unset RSCTF_FLAG
php-fpm -D
exec nginx -g 'daemon off;'
