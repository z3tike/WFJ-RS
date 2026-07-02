from train import model
from recommend import cf_recommend
from data import users
from data import videos, interactions


for i in videos:
    print(f"\nVideo id: {i["id"]} - Topic: {i["topic"]}, Views: {i["views"]}, Likes: {i["likes"]}, Shares: {i["shares"]}, topic: {i["topic"]}, cluster: {i["cluster"]}\n")

"""
for i in interactions:
    print(f"User ID: {i["user_id"]} - Video ID: {i["video_id"]} - Time: {i["watch_time"]}") 
"""

for user in users:
    print(f"\n=== User {user['id']} ajánlásai ===")
    recs = cf_recommend(user, model)
    for video, score, cf, content in recs:
        print(
            f"  Video {video['id']:2} ({video['topic']:8}) | "
            f"final: {score:.3f} | "
            f"cf: {cf:.3f} | "
            f"content: {content:.3f}"
        )