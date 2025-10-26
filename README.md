# geo-muni · Asignación de Municipios por Georreferencia (Rep. Dominicana)

> Portafolio de **Ciencia de Datos / GIS** por *Raquel Roa*. Este proyecto asigna el **municipio** a registros con **latitud/longitud** usando `GeoPandas` y *spatial join* sobre capas oficiales de municipios (sustituibles por las de tu país/área).

[![CI](https://img.shields.io/github/actions/workflow/status/raroap/geo-muni/ci.yml?label=CI&logo=github)](https://github.com/raroap/geo-muni/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Made with GeoPandas](https://img.shields.io/badge/made%20with-GeoPandas-blue)](#)
[![Python 3.11](https://img.shields.io/badge/python-3.11+-informational)](#)

## 🎯 Problema
Las empresas de Distribución recopilan grandes volúmenes de datos con coordenadas GPS (ventas, servicios, clientes). sin una asignación territorial automática, resulta difícil analizar indicadores por municipio o región. 

Este proyecto ofrece una solución práctica de geocodificación inteligente, permitiendo vincular cada punto georreferenciado con su municipio correspondiente. De esta forma, las empresas pueden integrar fácilmente la información en dashboards de Business Intelligence, optimizar rutas, evaluar cobertura y mejorar la toma de decisiones basadas en datos.




## 💡 Solución
`geo-muni` convierte tus **puntos** (`lon`, `lat`) en **municipios** con una sola instrucción:
```bash
geo-muni assign \
  --points data/raw/puntos_sample.csv \
  --municipios data/raw/municipios_sample.geojson \
  --out data/processed/puntos_con_municipio.csv \
  --lon lon --lat lat --muni-col name
```

## ✨ Highlights
- Spatial join robusto (`within`) con manejo de **CRS**.
- **CLI** amigable (`typer`) y **tests** (`pytest`).
- **Notebook demo** para mostrar el flujo end-to-end.
- Preparado para **CI/CD** con GitHub Actions.
- Estructura profesional de repo (issues, PR template, changelog, licencia).

## 📦 Instalación
Con **conda** (recomendado):
```bash
conda env create -f environment.yml
conda activate geo-muni
pip install -e .
```

## 🧪 Pruebas
```bash
pytest -q
```

## 🗺️ Datos
- `data/raw/municipios_sample.geojson`: polígonos **sintéticos** de ejemplo.
- `data/raw/puntos_sample.csv`: 4 puntos de prueba.
> Sustituye por tu **capa oficial** de municipios (ONE/OGTIC) y tu dataset anonimizado.

## 📓 Demo
Abre `notebooks/01_demo.ipynb`. Añade un mapa rápido:
```python
import geopandas as gpd
ax = muni_gdf.boundary.plot(figsize=(5,5))
out_gdf = gpd.GeoDataFrame(out, geometry=gpd.points_from_xy(out.lon, out.lat), crs=muni_gdf.crs)
out_gdf.plot(ax=ax, markersize=12)
```

## 🧱 Arquitectura
```
src/geo_muni/
 ├─ assign.py       # lógica de sjoin (puntos → municipio)
 ├─ cli.py          # interfaz de línea de comandos
 └─ __init__.py
```

## 🚀 Roadmap
- [ ] Modo `nearest` para puntos fuera de polígonos.
- [ ] Validación de calidad (porcentaje sin match, distancia al polígono más cercano).
- [ ] Benchmarks con 1M de puntos (rtree).
- [ ] Soporte multi-país (columna `iso_subdivision`).

## 🧭 Caso de uso (Ejemplo)
- Entrada: 50k tickets de servicio con `lat/lon`.
- Salida: CSV con **municipio** + KPIs por territorio para ruteo y performance.
- Impacto: +80% velocidad en reportería; -95% errores manuales; habilita **bonos por zona**, SLA por municipio, etc.

## 🧑‍💻 Autor
**Raquel Roa** · Ciencia de Datos / BI · RD  
LinkedIn: https://www.linkedin.com/in/RaquelRoaP · Email: raquelroa33@gmail.com

## 🔖 Licencia
MIT © 2025 Raquel Roa
