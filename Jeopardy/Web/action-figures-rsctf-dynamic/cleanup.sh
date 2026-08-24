#!/bin/sh
set -eu
find /chall -mindepth 1 -maxdepth 1 -exec rm -rf -- {} +
cp -R /root/dist_cleanup/. /chall/
chmod -R 0777 /chall
