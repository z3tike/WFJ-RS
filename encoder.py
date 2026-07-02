from data import generated_videos

TOPICS = {
    topic: idx
    for idx, topic in enumerate(sorted({video["topic"] for video in generated_videos}))
}

def topic_to_id(topic):
    return TOPICS[topic]

def topic_count():
    return len(TOPICS)