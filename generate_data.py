import random

topics = {
    "sports": ["football", "soccer", "basketball", "tennis"],
    "gaming": ["gaming", "esports", "minecraft", "fps", "rpg"],
    "tech": ["ai", "machine_learning", "programming", "tech", "data_science"]
}

all_topics = sum(topics.values(), [])


def generate_videos(n=10):
    videos = []

    for i in range(1, n+1):

        cluster = random.choice(list(topics.keys()))
        topic = random.choice(topics[cluster])

        base_views = random.randint(5000, 120000)

        videos.append({
            "id": i,
            "views": base_views,
            "likes": int(base_views * random.uniform(0.01, 0.2)),
            "shares": int(base_views * random.uniform(0.001, 0.03)),
            "topic": topic,
            "cluster": cluster
        })

    return videos

def generate_interactions(users, videos):
    interactions = []

    for user in users:
        for video in videos:

            base = random.randint(2, 15)

            if user["favorite_cluster"] == video["cluster"]:
                watch_time = random.randint(80, 200)

            elif abs(list(topics.keys()).index(user["favorite_cluster"]) -
                     list(topics.keys()).index(video["cluster"])) == 1:
                watch_time = random.randint(20, 60)

            else:
                watch_time = base

            interactions.append({
                "user_id": user["id"],
                "video_id": video["id"],
                "watch_time": watch_time
            })

    return interactions