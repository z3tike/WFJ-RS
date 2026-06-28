import torch
import torch.nn as nn
from encoder import topic_count
class RecommendationModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.topic_embedding = nn.Embedding(
            num_embeddings=topic_count(),
            embedding_dim=8    
        )

        self.network = nn.Sequential(
            nn.Linear(19, 32),
            nn.ReLU(),

            nn.Linear(32, 16),
            nn.ReLU(),

            nn.Linear(16, 1),
        )

    def forward(self, user_topic, stats, video_topic):

        user_embedding = self.topic_embedding(user_topic)

        video_embedding = self.topic_embedding(video_topic)

        x = torch.cat([
            user_embedding,
            stats,
            video_embedding
        ])

        return self.network(x)