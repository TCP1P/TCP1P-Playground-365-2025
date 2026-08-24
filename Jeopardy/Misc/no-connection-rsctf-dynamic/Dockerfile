FROM ubuntu:22.04 AS curl-builder

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential ca-certificates libssl-dev pkg-config wget \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /tmp
RUN wget -q https://curl.se/download/curl-8.1.2.tar.gz \
    && echo '2e5a9b8fcdc095bdd2f079561f369de71c5eb3b80f00a702fbe9a8b8d9897891  curl-8.1.2.tar.gz' | sha256sum -c - \
    && tar xzf curl-8.1.2.tar.gz
WORKDIR /tmp/curl-8.1.2
RUN ./configure --prefix=/build --disable-shared --enable-static --with-openssl \
        --disable-dict --disable-file --disable-ftps --disable-gopher \
        --disable-imap --disable-imaps --disable-ldap --disable-ldaps \
        --disable-pop3 --disable-pop3s --disable-rtmp --disable-rtsp \
        --disable-scp --disable-sftp --disable-smb --disable-smbs \
        --disable-smtp --disable-smtps --disable-telnet --disable-tftp \
    && make -j2 \
    && make install

FROM mongo:7.0.14-jammy

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends figlet socat \
    && rm -rf /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash ctf
COPY --from=curl-builder /build/bin/curl /usr/local/bin/curl
COPY --chmod=0555 app.sh /app/app.sh
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint

EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
