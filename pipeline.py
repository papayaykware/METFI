# pipeline.py

from ingest import DataIngestor
from spectral_analysis import SpectralAnalyzer
from event_detection import EventDetector
from coherence import CoherenceEstimator

def run_pipeline():
    # Ingesta
    ingestor = DataIngestor(source="synthetic")
    t, signal = ingestor.load()

    # Análisis espectral
    analyzer = SpectralAnalyzer(sampling_rate=100)
    freqs, spectrum = analyzer.compute_fft(signal)

    # Detección de eventos
    detector = EventDetector()
    anomalies = detector.detect_anomalies(signal)
    transitions = detector.detect_transitions(signal)

    # Coherencia
    coherence = CoherenceEstimator().compute_coherence(signal)

    return {
        "time": t,
        "signal": signal,
        "spectrum": (freqs, spectrum),
        "anomalies": anomalies,
        "transitions": transitions,
        "coherence": coherence
    }
