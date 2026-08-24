#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"

grep -qE '(^|[[:space:]])db([[:space:]]|$)' /etc/hosts || printf '127.0.0.1 db\n' >> /etc/hosts
mkdir -p /data/db
mongod --bind_ip 127.0.0.1 --dbpath /data/db --fork --logpath /tmp/mongod.log
RSCTF_FLAG="$RSCTF_FLAG" mongosh --quiet --host 127.0.0.1 --eval '
  const target = db.getSiblingDB("flagdb");
  target.flag.drop();
  target.flag.insertMany([
    {flag: "fake flag 1"},
    {flag: "fake flag 2"},
    {flag: process.env.RSCTF_FLAG},
    {flag: "fake flag 3"}
  ]);
' >/dev/null
unset RSCTF_FLAG
cd /app
exec socat TCP-LISTEN:8080,reuseaddr,fork EXEC:/app/app.sh,pty,stderr,su=ctf
