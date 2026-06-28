import torch
from data import videos
from encoder import one_hot
from normalize import (
    normalize_views,
    normalize_likes,
    normalize_shares
)

def recommend(user, model):

    user_vector = torch.tensor(one_hot(user["favorite_topic"]), dtype=torch.float32)
    recommendations = []

    for video in videos:

        video_vector = torch.tensor( one_hot(video["topic"]), dtype=torch.float32 )

        stats_vector = torch.tensor([ 0.6 * normalize_views(video["views"]),  0.3 * normalize_likes(video["likes"]),  0.1 * normalize_shares(video["shares"])], dtype=torch.float32)

        inputs = torch.cat([ 1.0 * user_vector, stats_vector, 1.0 * video_vector ], dim=0)

        with torch.no_grad():
            score = model(inputs).item()
    
        recommendations.append((video, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations
