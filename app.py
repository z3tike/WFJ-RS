from train import model
from recommend import cf_recommend
from data import users

for user in users:
    print(f"\n=== User {user['id']} ({user['favorite_topic']}) ajánlásai ===")
    recs = cf_recommend(user, model)
    for video, score, cf, content in recs:
        print(
            f"  Video {video['id']:2} ({video['topic']:8}) | "
            f"final: {score:.3f} | "
            f"cf: {cf:.3f} | "
            f"content: {content:.3f}"
        )