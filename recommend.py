import torch
from data import videos
from encoder import one_hot
from normalize import (
    normalize_views,
    normalize_likes,
    normalize_shares
)

def recommend(user, model):

    user_vector = one_hot(user["favorite_topic"])
    recommendations = []

    for video in videos:
        video_vector = one_hot(video["topic"])

        inputs = (
            user_vector
            + [
                normalize_views(video["views"]),
                normalize_likes(video["likes"]),
                normalize_shares(video["shares"])
            ]
            + video_vector
        )
        inputs = torch.tensor(inputs, dtype=torch.float32)
        with torch.no_grad():
            score = model(inputs).item()

        recommendations.append((video, score))

        recommendations.sort(key=lambda x: x[1], reverse=True)

        return recommendations
