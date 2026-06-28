import torch
import torch.nn as nn
import torch.optim as optim
from dataset import create_dataset
from model import RecommendationModel
from recommend import recommend
from data import users


dataset = create_dataset()
model = RecommendationModel()
loss_fn = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(500):

    total_loss = 0
    
    for inputs, label in dataset:

        inputs = torch.tensor(inputs, dtype=torch.float32)
        label = torch.tensor([[label]], dtype=torch.float32)

        prediction = model(inputs)
        loss = loss_fn(prediction, label)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    if epoch % 50 == 0:
        print(f"Epoch {epoch} | Loss = {total_loss:.4f}")
print()
print("-" * 5 + "Anticipating user needs" + "-" * 5)
print()

recommendations = recommend(users[0], model)

for video, score in recommendations:

    print(f"Video (id: {video["id"]}) - Topic: {video["topic"]} - Views: {video["views"]} - Likes: {video["likes"]} - Shares: {video["shares"]}.\nScore: {score}" )
    print()
