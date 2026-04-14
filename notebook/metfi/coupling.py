import numpy as np

def eeg_to_forcing(phi_eeg, size):
    """
    Traduce coherencia EEG a forzamiento del campo
    """
    base = np.ones(size) * phi_eeg

    # perturbación estructurada
    spatial_pattern = np.sin(np.linspace(0, 2*np.pi, size))

    return base * spatial_pattern
