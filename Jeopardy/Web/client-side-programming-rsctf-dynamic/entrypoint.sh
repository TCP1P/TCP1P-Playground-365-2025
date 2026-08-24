#!/bin/bash
set -euo pipefail
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"

export APPFLAG="$RSCTF_FLAG"
export APPNAME=Admin
export APPURL=https://127.0.0.1:8080/
export APPURLREGEX='^https://.*$'
export APPLIMIT=2
export APPLIMITTIME=60
export USE_PROXY=1
unset RSCTF_FLAG

pids=()
cleanup() {
  trap - EXIT INT TERM
  if ((${#pids[@]})); then kill "${pids[@]}" 2>/dev/null || true; fi
  wait 2>/dev/null || true
}
trap cleanup EXIT INT TERM

(cd /app/data && exec /app/imagefmt) & pids+=("$!")
(cd /app/ui && exec npm run start -- --hostname 127.0.0.1 --port 3000) & pids+=("$!")
(cd /app/bot && exec node index.js) & pids+=("$!")
nginx -g 'daemon off;' & pids+=("$!")

wait -n "${pids[@]}"
