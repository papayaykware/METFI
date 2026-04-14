import numpy as np

def compute_coherence(field):
    """
    Coherencia interna del campo
    """
    corr = np.corrcoef(field)
    return np.mean(np.abs(corr))
