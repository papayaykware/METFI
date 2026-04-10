def exception_detection(predicted, observed, threshold=0.8):
    similarity = coherence_metric(predicted, observed)
    return similarity < threshold
