import torch
import torch.nn as nn
import torch.optim as optim
from data import videos, interactions
from model import WatchTimeModel
from encoder import topic_to_id, topic_count

MAX_WATCH_TIME = 200

video_topic_map = {v["id"]: v["topic"] for v in videos}

model = WatchTimeModel(
    num_users=3,
    num_videos=10,
    num_topics=topic_count(),
    embedding_dim=8
)

loss_fn  = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

for epoch in range(1000):
    total_loss = 0

    for interaction in interactions:
        user_id  = torch.tensor(interaction["user_id"] - 1)
        video_id = torch.tensor(interaction["video_id"] - 1)

        topic    = video_topic_map[interaction["video_id"]]
        topic_id = torch.tensor(topic_to_id(topic))

        label = torch.tensor(
            interaction["watch_time"] / MAX_WATCH_TIME,
            dtype=torch.float32
        )

        prediction = model(user_id, video_id, topic_id)
        loss = loss_fn(prediction, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    if epoch % 100 == 0:
        print(f"Epoch {epoch:4} | Loss = {total_loss:.4f}")