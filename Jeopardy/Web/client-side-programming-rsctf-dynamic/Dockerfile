FROM golang:1.22.6-bookworm AS backend-builder
WORKDIR /src
COPY imagefmt/go.mod imagefmt/go.sum ./
RUN go mod download
COPY imagefmt/ ./
RUN CGO_ENABLED=1 go build -trimpath -ldflags='-s -w' -o /out/imagefmt .

FROM node:20.17.0-bookworm-slim AS ui-builder
WORKDIR /app
COPY ui/package.json ui/package-lock.json ./
RUN npm ci
COPY ui/ ./
RUN npm run build

FROM node:20.17.0-bookworm-slim AS bot-builder
WORKDIR /app
COPY bot/package.json ./
ENV PUPPETEER_SKIP_DOWNLOAD=true
RUN npm install --omit=dev --no-audit --no-fund

FROM node:20.17.0-bookworm-slim
ENV NODE_ENV=production PUPPETEER_SKIP_DOWNLOAD=true NEXT_TELEMETRY_DISABLED=1
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        ca-certificates chromium nginx openssl \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /app/data/uploads /run/nginx
COPY --from=backend-builder /out/imagefmt /app/imagefmt
COPY --from=ui-builder /app /app/ui
COPY --from=bot-builder /app/node_modules /app/bot/node_modules
COPY bot/ /app/bot/
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ext.conf /tmp/ext.conf
RUN openssl req -x509 -newkey rsa:2048 -keyout /tmp/privkey.pem -out /tmp/fullchain.pem \
        -days 3650 -nodes -config /tmp/ext.conf \
    && chmod 0600 /tmp/privkey.pem
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
