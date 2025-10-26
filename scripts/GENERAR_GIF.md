# Cómo generar un GIF corto del uso de la CLI

## Opción 1: Asciinema + agg
asciinema rec demo.cast
# ejecuta el comando CLI
geo-muni assign --points data/raw/puntos_sample.csv --municipios data/raw/municipios_sample.geojson --out data/processed/puntos_con_municipio.csv
# Ctrl+D para terminar
pip install agg
agg demo.cast demo.gif --font-size 16 --theme dracula

## Opción 2: Peek/OBS (GUI)
Graba la terminal 6–8s ejecutando el comando y guardando el CSV.
