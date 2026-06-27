MAX_VIEWS = 100000
MAX_LIKES = 40000
MAX_SHARES = 2500

def normalize_views(views):
    return views / MAX_VIEWS

def normalize_likes(likes):
    return likes / MAX_LIKES

def normalize_shares(shares):
    return shares / MAX_SHARES