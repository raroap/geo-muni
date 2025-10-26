# Comandos útiles
.PHONY: setup test format run-demo

setup:
	python -m pip install -e .[dev]

test:
	pytest -q

run-demo:
	geo-muni assign --points data/raw/puntos_sample.csv --municipios data/raw/municipios_sample.geojson --out data/processed/puntos_con_municipio.csv --lon lon --lat lat --muni-col name
