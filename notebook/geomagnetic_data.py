
---

## 1. `geomagnetic_data.py`

Descarga y simulación de datos geomagnéticos (ej. índice Kp simplificado).

```python
# geomagnetic_data.py

import numpy as np
import pandas as pd

def generate_synthetic_geomagnetic(n=1000):
    t = np.arange(n)
    
    # señal base (variación suave)
    signal = np.sin(2 * np.pi * t / 200)
    
    # perturbaciones geomagnéticas
    disturbances = np.zeros(n)
    disturbances[300:320] += 2
    disturbances[700:710] -= 1.5

    noise = 0.2 * np.random.randn(n)

    data = signal + disturbances + noise

    df = pd.DataFrame({
        "time": t,
        "geomagnetic_index": data
    })

    return df


def load_geomagnetic_from_csv(path="data/geomagnetic.csv"):
    return pd.read_csv(path)


if __name__ == "__main__":
    df = generate_synthetic_geomagnetic()
    df.to_csv("data/geomagnetic.csv", index=False)
    print("Geomagnetic data generated.")
