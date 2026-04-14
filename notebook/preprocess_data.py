# preprocess_data.py

import pandas as pd

def normalize(df, column):
    mean = df[column].mean()
    std = df[column].std()
    df[column] = (df[column] - mean) / (std + 1e-6)
    return df


def align_time_series(dfs, on="time"):
    merged = dfs[0]
    for df in dfs[1:]:
        merged = pd.merge(merged, df, on=on, how="inner")
    return merged


def preprocess_all():
    geomag = pd.read_csv("data/geomagnetic.csv")
    seismic = pd.read_csv("data/seismic.csv")
    climate = pd.read_csv("data/climate.csv")

    geomag = normalize(geomag, "geomagnetic_index")
    seismic = normalize(seismic, "magnitude")
    climate = normalize(climate, "temperature")

    merged = align_time_series([geomag, seismic, climate])

    merged.to_csv("data/merged.csv", index=False)
    print("Preprocessing complete. File saved as data/merged.csv")


if __name__ == "__main__":
    preprocess_all()
