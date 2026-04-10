def coherence_metric(x, y):
    return torch.cosine_similarity(x, y, dim=-1)
