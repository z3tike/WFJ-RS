import torch
from data import users, videos
from encoder import topic_to_id
from normalize import (
    normalize_views,
    normalize_likes,
    normalize_shares
)

def create_dataset():

    dataset = []

    for user in users:

        for video in videos:

            topic_match = int(user["favorite_topic"] == video["topic"])

            engagement = (
                0.4 * normalize_likes(video["likes"]) +
                0.4 * normalize_views(video["views"]) +
                0.2 * normalize_shares(video["shares"])
            )

            label = (
                0.7 * topic_match +
                0.3 * engagement
            )

            user_topic = topic_to_id(user["favorite_topic"])

            video_topic = topic_to_id(video["topic"])

            stats = torch.tensor([
                normalize_views(video["views"]),
                normalize_likes(video["likes"]),
                normalize_shares(video["shares"])
            ], dtype=torch.float32)

            dataset.append(
                (
                    torch.tensor(user_topic),
                    stats,
                    torch.tensor(video_topic),
                    torch.tensor([label], dtype=torch.float32)
                )
            )

    return dataset