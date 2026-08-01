# Slim Python runtime. SysML v2 and the 127MB kernel jar were dropped (contract 2.0):
# the Architect designs per-aspect and emits Mermaid diagram source rendered client-side,
# so there is no JVM, no jar, and no SysML standard library to provision.
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY src/ ./src/
ENV PYTHONPATH=/app/src ARCHITECT_DATA_DIR=/app/data
# Run as a non-root user whose UID matches the host owner of data/, so generated
# artifacts on the bind mount are not root-owned. Override at build time:
#   docker compose build --build-arg APP_UID=$(id -u) --build-arg APP_GID=$(id -g)
ARG APP_UID=1000
ARG APP_GID=1000
RUN groupadd -g "$APP_GID" app 2>/dev/null || true \
 && useradd -u "$APP_UID" -g "$APP_GID" -m -s /usr/sbin/nologin app 2>/dev/null || true \
 && mkdir -p /app/data && chown -R "$APP_UID:$APP_GID" /app
USER $APP_UID:$APP_GID
# data/ is bind-mounted: generated architecture packages persist on the host.
VOLUME ["/app/data"]
# Batch job, not a server. Override the arg with a project id or package.json path:
#   docker compose run --rm architect-agent python3 -m architect_agent.aspect_pipeline <PID>
CMD ["python3", "-m", "architect_agent.aspect_pipeline", "--help"]
