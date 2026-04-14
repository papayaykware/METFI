from metfi.toroidal_field import ToroidalField
from metfi.coupling import eeg_to_forcing
from metfi.observables import compute_coherence

import numpy as np
import logging

def compute_phi_eeg(features):
    corr = np.corrcoef(features)
    return np.mean(np.abs(corr))


def run_cpea_metfi(features):
    logging.info("===== CPEA-METFI LOOP =====")

    # 1. Coherencia EEG
    phi_eeg = compute_phi_eeg(features)
    logging.info(f"Phi EEG: {phi_eeg:.4f}")

    # 2. Inicializar campo
    field = ToroidalField(size=100)

    phi_geo_series = []

    # 3. Simulación dinámica
    for t in range(50):
        forcing = eeg_to_forcing(phi_eeg, field.size)
        state = field.step(forcing)

        phi_geo = compute_coherence(state)
        phi_geo_series.append(phi_geo)

    phi_geo_mean = np.mean(phi_geo_series)

    logging.info(f"Phi GEO: {phi_geo_mean:.4f}")

    # 4. Error de coherencia
    error = abs(phi_eeg - phi_geo_mean)

    logging.info(f"Error coherencia: {error:.4f}")

    return {
        "phi_eeg": phi_eeg,
        "phi_geo": phi_geo_mean,
        "error": error
    }
