from __future__ import annotations
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def load_municipios(path: str, to_epsg: int = 4326, muni_col: str = "name") -> gpd.GeoDataFrame:
    gdf = gpd.read_file(path)
    if gdf.crs is None:
        # Suponemos WGS84 si no hay CRS
        gdf.set_crs(epsg=4326, inplace=True)
    if to_epsg and (gdf.crs.to_epsg() != to_epsg):
        gdf = gdf.to_crs(epsg=to_epsg)
    if muni_col not in gdf.columns:
        raise ValueError(f"Columna de municipio '{muni_col}' no existe en {path}. Columnas: {list(gdf.columns)}")
    return gdf

def df_points_to_gdf(points_df: pd.DataFrame, lon_col: str = "lon", lat_col: str = "lat", epsg: int = 4326) -> gpd.GeoDataFrame:
    if lon_col not in points_df.columns or lat_col not in points_df.columns:
        raise ValueError(f"Columnas de coordenadas '{lon_col}', '{lat_col}' no están presentes en el DataFrame.")
    geometry = [Point(xy) for xy in zip(points_df[lon_col], points_df[lat_col])]
    gdf = gpd.GeoDataFrame(points_df.copy(), geometry=geometry, crs=f"EPSG:{epsg}")
    return gdf

def assign(points_df: pd.DataFrame, municipios_gdf: gpd.GeoDataFrame, muni_col: str = "name", how: str = "left") -> pd.DataFrame:
    """Hace un sjoin entre puntos y polígonos de municipios, devolviendo el nombre del municipio en una columna `municipio`.

    - `how`: estrategia de join para puntos sin match (por defecto 'left' conserva todos los puntos)

    """
    points_gdf = df_points_to_gdf(points_df)
    # Asegurar CRS compatibles
    if points_gdf.crs != municipios_gdf.crs:
        municipios_gdf = municipios_gdf.to_crs(points_gdf.crs)
    joined = gpd.sjoin(points_gdf, municipios_gdf[[muni_col, 'geometry']], how=how, predicate='within')
    out = joined.drop(columns=[c for c in joined.columns if c.startswith('index_')], errors='ignore')
    out = out.rename(columns={muni_col: 'municipio'})
    # Volver a DataFrame plano
    out = pd.DataFrame(out.drop(columns=['geometry']))
    return out
