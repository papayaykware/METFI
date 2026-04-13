# spectral_analysis.py

import numpy as np

class SpectralAnalyzer:
    def __init__(self, sampling_rate):
        self.fs = sampling_rate

    def compute_fft(self, signal):
        fft_vals = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(signal), 1/self.fs)
        return freqs, np.abs(fft_vals)

    def dominant_frequencies(self, signal, top_n=3):
        freqs, spectrum = self.compute_fft(signal)
        idx = np.argsort(spectrum)[-top_n:]
        return freqs[idx], spectrum[idx]
