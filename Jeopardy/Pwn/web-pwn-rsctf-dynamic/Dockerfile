FROM ubuntu@sha256:2260313b31c8c011cd2eebe728008efac1b3982be73eb71348ea2648d2c0e09b AS app

RUN apt-get update && apt-get install -y gcc make

WORKDIR /app

COPY ./http.c ./http.h ./main.c ./Makefile ./
COPY ./public/ ./public/

RUN make

RUN rm *.o *.c *.h Makefile

COPY ./flag.txt .
RUN mv ./flag.txt /$(cat /proc/sys/kernel/random/uuid).txt

RUN useradd -m app
USER app

CMD ["./neko", "80"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app/public /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_e74052fbaed77ef9806bd042f3af7eb00f06f56ec8c4b -e RSCTF_DYNAMIC_FLAG_832b0855ff8ec9e5e52b6dd9a87b6895c {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
USER app
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
