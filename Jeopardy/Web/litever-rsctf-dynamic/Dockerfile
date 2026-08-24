FROM python:3.11-slim-buster

WORKDIR /app

RUN pip3 install flask

COPY src/ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
COPY rsctf-prepare-flag.sh /usr/local/bin/rsctf-prepare-flag
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_4701cd4e1a898 -e RSCTF_DYNAMIC_FLAG_7f5414 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets; \
    chmod 0555 /usr/local/bin/rsctf-prepare-flag; \
    chmod a+w /app/tcp1p.sqlite
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
