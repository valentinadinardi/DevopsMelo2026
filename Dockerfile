FROM ubuntu:26.04

LABEL org.opencontainers.image.source="https://github.com/valentinadinardi/DevopsMelo2026.git"
LABEL org.opencontainers.image.description="Tarea Presencial 19 de Agosto"

RUN apt-get update && apt-get install -y \
    gnupg \
    unzip \
    dirmngr \
    jq \
    git \
    curl \
    python3 \
    python3-pip \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Crear usuario
RUN useradd -ms /bin/bash router \
    && adduser router sudo

# Instalar dependencias Python
RUN pip3 install --break-system-packages routeros_api flask

USER router
WORKDIR /home/router

# Clonar directamente la rama grupo4
RUN git clone -b grupo4 --single-branch \
    https://github.com/valentinadinardi/DevopsMelo2026.git

WORKDIR /home/router/DevopsMelo2026

# Verificar rama y archivos durante el build
RUN echo "=== RAMA ACTUAL ===" \
    && git branch --show-current \
    && echo "=== ARCHIVOS ===" \
    && find . -maxdepth 2 -type f

EXPOSE 5000

CMD ["python3", "app.py"]