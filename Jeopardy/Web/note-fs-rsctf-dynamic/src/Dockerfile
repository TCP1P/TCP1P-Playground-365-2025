# Use the official Bun image as a base
FROM oven/bun:1.1.43

# Create and set the working directory
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json bun.lockb /app/
RUN bun install

COPY ./flag.txt /flag.flag

# Copy the rest of the application files
COPY . /app

# Expose the port the app runs on
EXPOSE 3000

# Command to run the application
CMD ["bun", "start"]

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /flag.flag /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_84c0ebfe9910f56300a611774dedc5744d599de5c5060d -e RSCTF_DYNAMIC_FLAG_393c291816dfb6c896d87510bdc05f48e66cdb0 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
