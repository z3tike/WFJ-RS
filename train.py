import torch
import torch.nn as nn
import torch.optim as optim
from dataset import create_dataset
from model import RecommendationModel
from recommend import recommend
from data import users

dataset = create_dataset()

model = RecommendationModel()

loss_fn = nn.MSELoss()

optimizer = optim.Adam( model.parameters(), lr=0.001 )

for epoch in range(500):

    total_loss = 0

    for user_topic, stats, video_topic, label in dataset:

        prediction = model(
            user_topic,
            stats,
            video_topic
        )

        loss = loss_fn(prediction, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    if epoch % 50 == 0:
        print(f"Epoch {epoch:3} | Loss = {total_loss:.4f}")

print("\n===== AJÁNLÁS =====\n")

recommendations = recommend(users[0], model)

for video, score in recommendations:

    print(
        f"Video {video['id']}\n"
        f"Topic : {video['topic']}\n"
        f"Views : {video['views']}\n"
        f"Likes : {video['likes']}\n"
        f"Shares: {video['shares']}\n"
        f"Score : {score}\n"
    )