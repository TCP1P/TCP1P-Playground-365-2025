FROM node:20.17.0-bookworm-slim AS bot-builder
WORKDIR /app
COPY bot/package.json ./
ENV PUPPETEER_SKIP_DOWNLOAD=true
RUN npm install --omit=dev --no-audit --no-fund

FROM node:20.17.0-bookworm-slim
ENV NODE_ENV=production PUPPETEER_SKIP_DOWNLOAD=true
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends ca-certificates chromium nginx \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/nginx
COPY site/ /var/www/html/
COPY --from=bot-builder /app/node_modules /app/bot/node_modules
COPY bot/ /app/bot/
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
