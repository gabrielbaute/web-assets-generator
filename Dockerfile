# Build stage
FROM python:3.13-slim-bookworm as builder

WORKDIR /app
COPY requirements.txt .

# Instala dependencias de compilación solo si son necesarias (para psycopg2, Pillow, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libjpeg-dev \
    zlib1g-dev && \
    pip install --user -r requirements.txt && \
    apt-get remove -y gcc python3-dev libjpeg-dev zlib1g-dev && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Runtime stage
FROM python:3.13-slim-bookworm

WORKDIR /app

# Copia desde el builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Configuración de entorno
ENV PATH=/root/.local/bin:$PATH \
    PYTHONPATH=/app

# Puerto expuesto (documentativo, no configura el servicio)
EXPOSE ${PORT:-8000}  

CMD ["sh", "-c", "waitress-serve --port=${PORT:-8000} --call server:create_app"]