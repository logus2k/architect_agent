# Multi-stage: build the Java tool, ship a slim runtime with JRE + Python.
FROM eclipse-temurin:21-jdk AS javabuild
WORKDIR /build
COPY java/ArchitectTool.java .
# The kernel jar is mounted at runtime, not baked in (~127 MB); compilation needs
# it on the classpath, so it is passed through as a build context volume.
COPY data/sysml-toolchain/jupyter-sysml-kernel-0.60.1-all.jar ./kernel.jar
RUN mkdir -p classes && javac -cp kernel.jar -d classes ArchitectTool.java

FROM eclipse-temurin:21-jre
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir --break-system-packages -r requirements.txt
COPY src/ ./src/
COPY --from=javabuild /build/classes /app/tool-classes
ENV PYTHONPATH=/app/src ARCHITECT_DATA_DIR=/app/data \
    ARCHITECT_TOOL_CLASSES=/app/tool-classes
# Run as a non-root user whose UID matches the host owner of data/, so generated
# artifacts on the bind mount are not root-owned. Override at build time:
#   docker compose build --build-arg APP_UID=$(id -u) --build-arg APP_GID=$(id -g)
ARG APP_UID=1000
ARG APP_GID=1000
RUN groupadd -g "$APP_GID" app 2>/dev/null || true \
 && useradd -u "$APP_UID" -g "$APP_GID" -m -s /usr/sbin/nologin app 2>/dev/null || true \
 && mkdir -p /app/data && chown -R "$APP_UID:$APP_GID" /app
USER $APP_UID:$APP_GID
# data/ is bind-mounted: the kernel jar and SysML standard library are large and
# environment-specific, so they are provisioned rather than baked into the image.
VOLUME ["/app/data"]
CMD ["python3", "-c", "from architect_agent import sysml; print('toolchain available:', sysml.is_available())"]
