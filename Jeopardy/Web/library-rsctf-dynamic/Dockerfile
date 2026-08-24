FROM mcr.microsoft.com/dotnet/aspnet:7.0

ENV ASPNETCORE_URLS=http://0.0.0.0:8181 \
    COMPlus_EnableDiagnostics=0 \
    DOTNET_EnableDiagnostics=0

RUN useradd --create-home --shell /usr/sbin/nologin ctf \
    && command -v setpriv \
    && rm -f /usr/share/dotnet/shared/Microsoft.NETCore.App/7.0.*/System.Diagnostics.Process.dll \
    && mkdir -p /app
WORKDIR /app
COPY app/ ./
COPY CRUD.runtimeconfig.json ./CRUD.runtimeconfig.json
COPY --chmod=0555 entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN chown -R root:root /app \
    && chmod -R a-w /app \
    && chmod 0700 /tmp

EXPOSE 8181
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
