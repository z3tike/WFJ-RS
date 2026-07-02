import torch
from data import videos, interactions
from encoder import topic_to_id
from normalize import normalize_views, normalize_likes, normalize_shares


def content_score(video):
    score = (
        0.2 * normalize_views(video["views"]) +
        0.3 * normalize_likes(video["likes"]) +
        0.1 * normalize_shares(video["shares"])
    )
    return score * 0.3


def cf_recommend(user, model, cf_weight=0.9, content_weight=0.1):

    already_watched = {
        i["video_id"]
        for i in interactions
        if i["user_id"] == user["id"]
    }

    user_id = torch.tensor(user["id"] - 1)
    recommendations = []

    for video in videos:
        if video["id"] in already_watched:
            continue

        video_id = torch.tensor(video["id"] - 1)
        topic_id = torch.tensor(topic_to_id(video["topic"]))

        with torch.no_grad():
            cf_score = model(user_id, video_id, topic_id).item()

        score = (
            cf_weight * cf_score +
            content_weight * content_score(video)
        )

        recommendations.append((video, score, cf_score, content_score(video)))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations