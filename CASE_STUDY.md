# Case Study · Geocodificación de Municipios para Equipos en Campo

**Contexto**: Empresa con flota de equipos fríos y técnicos de servicio en RD.  
**Reto**: Vincular 50k tickets con su **municipio** para KPI por territorio, ruteo y SLA.  
**Solución**: Spatial join con capa oficial de municipios + pipeline reproducible (CLI + tests + CI).  
**Resultados**:
- +80% velocidad en reportería
- -95% errores manuales de clasificación
- Mejoras en asignación de zonas y seguimiento de SLA

**Stack**: Python, GeoPandas, Shapely, PyProj, Rtree, Typer, Pytest, GitHub Actions.
