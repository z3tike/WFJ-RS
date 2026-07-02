import torch
import torch.nn as nn

class WatchTimeModel(nn.Module):

    def __init__(self, num_users, num_videos, num_topics, embedding_dim=16):
        super().__init__()

        self.user_embedding  = nn.Embedding(num_users, embedding_dim)
        self.video_embedding = nn.Embedding(num_videos, embedding_dim)
        self.topic_embedding = nn.Embedding(num_topics, embedding_dim)

        self.network = nn.Sequential(
            nn.Linear(embedding_dim * 3, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 1)
        )

    def forward(self, user_id, video_id, topic_id):
        u = self.user_embedding(user_id)
        v = self.video_embedding(video_id)
        t = self.topic_embedding(topic_id)

        x = torch.cat([u, v, t], dim=-1)
        return self.network(x).squeeze()