import torch
import torch.nn as nn

class METFIGraphEmbedding(nn.Module):
    def __init__(self, num_nodes, emb_dim):
        super().__init__()
        self.embedding = nn.Embedding(num_nodes, emb_dim)

    def forward(self, node_ids):
        return self.embedding(node_ids)
