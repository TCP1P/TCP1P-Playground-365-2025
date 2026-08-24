FROM composer:2.7 AS dependencies
WORKDIR /app
COPY composer.json composer.lock ./
RUN composer install --no-dev --no-interaction --no-progress --prefer-dist --classmap-authoritative

FROM php:7.4.33-bullseye
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends cron supervisor \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --system ctf \
    && useradd --system --gid ctf --home /nonexistent ctf \
    && mkdir -p /chall /root/dist_cleanup
COPY index.php order.php composer.json composer.lock /chall/
COPY --from=dependencies /app/vendor /chall/vendor
COPY supervisord.conf /etc/supervisor/conf.d/rsctf.conf
COPY cleanup.sh /root/cleanup.sh
COPY cleanup-cron /etc/cron.d/rsctf-cleanup
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN chmod 0644 /etc/cron.d/rsctf-cleanup /etc/supervisor/conf.d/rsctf.conf \
    && chmod 0555 /root/cleanup.sh \
    && cp -R /chall/. /root/dist_cleanup/ \
    && chmod -R 0777 /chall \
    && crontab /etc/cron.d/rsctf-cleanup

EXPOSE 30032
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/rsctf.conf"]
