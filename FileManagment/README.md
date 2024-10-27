# File Management Automation with Python and Watchdog

Este proyecto es una herramienta de automatización que organiza archivos en una carpeta específica. Utiliza la librería `watchdog` para monitorear cambios en la carpeta de origen y, cuando detecta nuevos archivos, los mueve automáticamente a subcarpetas según su tipo (imágenes, videos o archivos).

## Funcionalidad
- Monitorea la carpeta especificada (`Downloads`) en busca de archivos nuevos o modificados.
- Clasifica los archivos por tipo:
  - **Imágenes** (.png, .jpeg, .jpg) se mueven a `Downloaded_Images`.
  - **Videos** (.mp4, .mov) se mueven a `Downloaded_Videos`.
  - Otros archivos se mueven a `Downloaded_Files`.
- Si un archivo con el mismo nombre ya existe en la carpeta de destino, se añade un número al final del nombre para evitar conflictos.

## Requisitos
- Python 3.x
- Librería `watchdog`

## Instalación
1. Clona este repositorio.
2. Instala los requisitos usando `pip`:
   ```bash
   py -m pip install watchdog
