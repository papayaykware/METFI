import numpy as np

class ToroidalField:
    def __init__(self, size=100):
        self.size = size
        self.field = np.zeros(size)

    def step(self, forcing, dt=0.1):
        """
        Dinámica no lineal simplificada tipo oscilador acoplado
        """
        noise = np.random.normal(0, 0.01, self.size)

        self.field += dt * (
            -0.1 * self.field
            + np.sin(self.field)
            + forcing
            + noise
        )

        return self.field
