topics = [
    'football',
    'gaming',
    'ai'
]

def one_hot(topic):
    vector = []
    for t in topics:
        if t == topic:
            vector.append(1)
        else:
            vector.append(0)
    return vector