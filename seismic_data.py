# seismic_data.py

import numpy as np
import pandas as pd

def generate_synthetic_seismic(n=1000):
    t = np.arange(n)
    
    # actividad base baja
    activity = np.random.poisson(lam=0.1, size=n)

    # eventos sísmicos artificiales
    events = np.zeros(n)
    events[400] = 5
    events[800] = 6

    magnitude = activity + events

    df = pd.DataFrame({
        "time": t,
        "magnitude": magnitude
    })

    return df


def load_seismic_from_csv(path="data/seismic.csv"):
    return pd.read_csv(path)


if __name__ == "__main__":
    df = generate_synthetic_seismic()
    df.to_csv("data/seismic.csv", index=False)
    print("Seismic data generated.")
