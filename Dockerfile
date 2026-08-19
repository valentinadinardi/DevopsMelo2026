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
    && rm -rf /var/lib/apt/lists/* \
    # Crear un usuario para ejecutar el runner
    && useradd -ms /bin/bash router && adduser router sudo

RUN pip install routeros_api 

USER router
WORKDIR /home/router

# Descargar el repositorio de la aplicación
RUN git clone
RUN git clone https://github.com/valentinadinardi/DevopsMelo2026.git