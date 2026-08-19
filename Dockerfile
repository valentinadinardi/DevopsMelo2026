FROM ubuntu:26.04
LABEL org.opencontainers.image.source="https://github.com/valentinadinardi/DevopsMelo2026.git"
LABEL org.opencontainers.image.description="Tarea Presencial 19 de Agosto"

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    gnupg \
    unzip \
    dirmngr \
    jq \
    git \
    curl \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/* \
    # Crear un usuario para ejecutar el runner
    && useradd -ms /bin/bash router && adduser router sudo

USER router
WORKDIR /home/router

RUN python3 -m venv /home/router/venv \
    && /home/router/venv/bin/pip install routeros_api

ENV PATH="/home/router/venv/bin:$PATH"

WORKDIR /home/router

RUN git clone https://github.com/valentinadinardi/DevopsMelo2026.git

CMD ["python3", "/home/router/DevopsMelo2026/main.py"]