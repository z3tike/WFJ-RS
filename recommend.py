import torch
from data import videos, watch_interactions
from encoder import topic_to_id
from normalize import normalize_views, normalize_likes, normalize_shares

def content_score(video):
    return (
        0.4 * normalize_views(video["views"]) +
        0.4 * normalize_likes(video["likes"]) +
        0.2 * normalize_shares(video["shares"])
    )

def cf_recommend(user, model, cf_weight=0.7, content_weight=0.3):

    already_watched = {
        i["video_id"]
        for i in watch_interactions
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