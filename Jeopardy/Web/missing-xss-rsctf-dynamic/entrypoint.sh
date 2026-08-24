#!/bin/bash
set -euo pipefail
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
export APPFLAG="$RSCTF_FLAG" APPNAME=Admin APPURL=http://127.0.0.1:8080/ APPURLREGEX='^http(|s)://.*$'
export APPLIMIT=2 APPLIMITTIME=60 USE_PROXY=1 BROWSER=firefox
unset RSCTF_FLAG

pids=()
cleanup() { trap - EXIT INT TERM; if ((${#pids[@]})); then kill "${pids[@]}" 2>/dev/null || true; fi; wait 2>/dev/null || true; }
trap cleanup EXIT INT TERM
node /app/site/app.js & pids+=("$!")
(cd /app/bot && exec node index.js) & pids+=("$!")
nginx -g 'daemon off;' & pids+=("$!")
wait -n "${pids[@]}"
