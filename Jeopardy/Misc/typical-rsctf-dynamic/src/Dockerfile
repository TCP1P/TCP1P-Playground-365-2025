# check=skip=JSONArgsRecommended
FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install socat python3 --fix-missing && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/chall

COPY typical.py typical.py

CMD test -n "$RSCTF_FLAG" && printf '%s\n' "$RSCTF_FLAG" > /flag-$(head -c8 /dev/urandom | md5sum | cut -c1-16) && unset RSCTF_FLAG && exec socat -dd TCP-LISTEN:5000,fork,reuseaddr EXEC:"python3 -u ./typical.py",su=nobody
