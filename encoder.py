TOPICS = {
    "football": 0,
    "gaming": 1,
    "ai": 2
}

def topic_to_id(topic):
    return TOPICS[topic]

def topic_count():
    return len(TOPICS)
