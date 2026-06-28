import torch

from data import videos
from encoder import topic_to_id
from normalize import (
    normalize_views,
    normalize_likes,
    normalize_shares
)

def recommend(user, model):

    recommendations = []

    user_topic = torch.tensor(
        topic_to_id(user["favorite_topic"]),
        dtype=torch.long
    )

    for video in videos:

        video_topic = torch.tensor(
            topic_to_id(video["topic"]),
            dtype=torch.long
        )

        stats = torch.tensor([
            normalize_views(video["views"]),
            normalize_likes(video["likes"]),
            normalize_shares(video["shares"])
        ], dtype=torch.float32)

        with torch.no_grad():
            score = model(
                user_topic,
                stats,
                video_topic
            ).item()

        recommendations.append((video, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations