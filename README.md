# Monitoreo de Router MikroTik

Aplicación web diseñada para monitorear los recursos de un router MikroTik a través de una interfaz visual sencilla e intuitiva.

## Prerrequisitos

* Tener **Docker** instalado y configurado en el sistema.

## Instalación y Ejecución

**1. Clonar el repositorio**
```bash
git clone https://github.com/valentinadinardi/DevopsMelo2026.git

**2. Construir la imagen de Docker**
docker build -t nombre_imagen .

**3. Levantar el contenedor**
docker run --rm -it --name monitoreo-contenedor -p 8080:8080 monitoreo bash