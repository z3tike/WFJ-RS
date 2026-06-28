import math

MAX_VIEWS = 150000
MAX_LIKES = 40000
MAX_SHARES = 2000

def normalize_views(x):
    return math.log1p(x) / math.log1p(MAX_VIEWS)

def normalize_likes(x):
    return math.log1p(x) / math.log1p(MAX_LIKES)

def normalize_shares(x):
    return math.log1p(x) / math.log1p(MAX_SHARES)