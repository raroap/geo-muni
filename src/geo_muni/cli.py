from __future__ import annotations
import typer
from rich import print
import pandas as pd
from .assign import load_municipios, assign

app = typer.Typer(help="Asignación de Municipios por Georreferencia (RD)")

@app.command()
def assign_cmd(
    points: str = typer.Option(..., help="CSV con columnas de coordenadas"),
    municipios: str = typer.Option(..., help="Shapefile o GeoJSON de municipios"),
    out: str = typer.Option(..., help="Ruta de salida CSV"),
    lon: str = typer.Option("lon", help="Nombre de la columna de longitud"),
    lat: str = typer.Option("lat", help="Nombre de la columna de latitud"),
    muni_col: str = typer.Option("name", help="Columna en el GeoDataFrame que contiene el nombre del municipio"),
):
    """Convierte un CSV de puntos (lon/lat) a CSV con columna `municipio` asignada."""
    df = pd.read_csv(points)
    muni_gdf = load_municipios(municipios, muni_col=muni_col)
    # Renombrar si las columnas no son lon/lat
    if lon != "lon":
        df = df.rename(columns={lon: "lon"})
    if lat != "lat":
        df = df.rename(columns={lat: "lat"})
    out_df = assign(df, muni_gdf, muni_col=muni_col)
    out_df.to_csv(out, index=False)
    print(f"[bold green]✔ Guardado:[/bold green] {out}")

if __name__ == '__main__':
    app()
