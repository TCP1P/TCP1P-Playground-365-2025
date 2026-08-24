FROM php:8.3-fpm-alpine3.20

RUN apk add --no-cache curl gcc musl-dev nginx \
    && mkdir -p /run/nginx /var/www/html/public
COPY public/ /var/www/html/public/
COPY nginx.conf /etc/nginx/http.d/default.conf
COPY readflag.c /tmp/readflag.c
RUN gcc -O2 -o /readflag /tmp/readflag.c \
    && rm /tmp/readflag.c \
    && chown root:root /readflag \
    && chmod 4755 /readflag
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
