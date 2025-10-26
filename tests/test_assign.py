import pandas as pd
from geo_muni.assign import load_municipios, assign

def test_assign_basic(tmp_path):
    municipios_path = "data/raw/municipios_sample.geojson"
    muni_gdf = load_municipios(municipios_path, muni_col="name")
    df = pd.read_csv("data/raw/puntos_sample.csv")
    out = assign(df, muni_gdf, muni_col="name")
    assert "municipio" in out.columns
    # Los dos primeros están dentro de algún municipio
    assert out.loc[out['id'] == 1, 'municipio'].iloc[0] == "Santo Domingo"
    assert out.loc[out['id'] == 2, 'municipio'].iloc[0] == "Santiago"
