import numpy as np

class Kuramoto:
    def __init__(self, N=50, K=1.0):
        self.N = N
        self.K = K
        self.theta = np.random.rand(N) * 2*np.pi
        self.omega = np.random.normal(1.0, 0.1, N)

    def step(self, forcing=0, dt=0.05):
        coupling = np.sum(np.sin(self.theta[:, None] - self.theta), axis=1)

        self.theta += dt * (
            self.omega +
            (self.K / self.N) * coupling +
            forcing
        )

        return self.theta
