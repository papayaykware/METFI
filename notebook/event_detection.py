# event_detection.py

import numpy as np

class EventDetector:
    def __init__(self, threshold=2.0):
        self.threshold = threshold

    def detect_anomalies(self, signal):
        mean = np.mean(signal)
        std = np.std(signal)
        
        anomalies = np.where(np.abs(signal - mean) > self.threshold * std)[0]
        return anomalies

    def detect_transitions(self, signal):
        derivative = np.diff(signal)
        transitions = np.where(np.abs(derivative) > np.std(derivative) * 3)[0]
        return transitions
