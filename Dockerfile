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

# Instalar dependencia Python
RUN pip3 install --break-system-packages routeros_api

USER router
WORKDIR /home/router

# Descargar repositorio
RUN git clone https://github.com/valentinadinardi/DevopsMelo2026.git

WORKDIR /home/router/DevopsMelo2026
