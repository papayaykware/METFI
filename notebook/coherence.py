# coherence.py

import numpy as np

class CoherenceEstimator:
    def compute_coherence(self, signal):
        # Simplificación: coherencia como inverso de varianza local
        window = 100
        coherence = []

        for i in range(len(signal) - window):
            segment = signal[i:i+window]
            coherence.append(1 / (np.var(segment) + 1e-6))

        return np.array(coherence)
