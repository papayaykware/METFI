# climate_data.py

import numpy as np
import pandas as pd

def generate_synthetic_climate(n=1000):
    t = np.arange(n)

    # temperatura base (estacionalidad)
    temp = 15 + 10 * np.sin(2 * np.pi * t / 365)

    # perturbaciones tipo evento extremo
    anomalies = np.zeros(n)
    anomalies[500:520] += 5

    noise = np.random.randn(n)

    temperature = temp + anomalies + noise

    df = pd.DataFrame({
        "time": t,
        "temperature": temperature
    })

    return df


def load_climate_from_csv(path="data/climate.csv"):
    return pd.read_csv(path)


if __name__ == "__main__":
    df = generate_synthetic_climate()
    df.to_csv("data/climate.csv", index=False)
    print("Climate data generated.")
