FROM mcr.microsoft.com/playwright:v1.45.3-jammy

ENV NODE_ENV=production
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends nginx \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /run/nginx /app/bot
WORKDIR /app/bot
COPY bot/package.json ./
RUN npm install --omit=dev --no-audit --no-fund
COPY bot/ ./
COPY app.js /app/site/app.js
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
