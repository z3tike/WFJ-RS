from data import users, videos
from encoder import one_hot
from normalize import ( normalize_views, normalize_likes, normalize_shares )

def create_dataset():
    dataset = []
    for user in users:
        for video in videos:
            user_vector = one_hot(user["favorite_topic"])
            video_vector = one_hot(video["topic"])

            inputs = [
                user_vector + [ normalize_views(video["views"]), normalize_likes(video["likes"]), normalize_shares(video["shares"]) ] + video_vector
            ]
            if user["favorite_topic"] == video["topic"]:
                label = 1
            else:
                label = 0

            dataset.append([inputs, label])
    return dataset