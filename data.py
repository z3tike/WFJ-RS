from generate_data import generate_videos, generate_interactions

users = [
    {
        "id": 1,
        "favorite_cluster": "gaming"
    },
    {
        "id": 2,
        "favorite_cluster": "sports"
    },
    {
        "id": 3,
        "favorite_cluster": "tech"
    }
]

generated_videos = generate_videos()
generated_interactions = generate_interactions(users, generated_videos)

videos = generated_videos
interactions = generated_interactions



generated_interactions = generate_interactions(users, generated_videos)

interactions = [

    {"user_id": 1, "video_id": 1,  "watch_time": 150},  
    {"user_id": 1, "video_id": 4,  "watch_time": 120}, 
    {"user_id": 1, "video_id": 2,  "watch_time": 10},   
    {"user_id": 1, "video_id": 5,  "watch_time": 8},    
    {"user_id": 1, "video_id": 3,  "watch_time": 5},   
    {"user_id": 1, "video_id": 6,  "watch_time": 4},   

    {"user_id": 2, "video_id": 2,  "watch_time": 90},  
    {"user_id": 2, "video_id": 5,  "watch_time": 100},
    {"user_id": 2, "video_id": 4,  "watch_time": 12},   
    {"user_id": 2, "video_id": 6,  "watch_time": 6},   
    {"user_id": 2, "video_id": 3,  "watch_time": 7},    

    {"user_id": 3, "video_id": 3,  "watch_time": 200},
    {"user_id": 3, "video_id": 6,  "watch_time": 180},  
    {"user_id": 3, "video_id": 2,  "watch_time": 10},   
    {"user_id": 3, "video_id": 1,  "watch_time": 5}, 
]