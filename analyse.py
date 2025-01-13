def get_post_per_subreddit(comments):
    post_per_subreddit = {}

    for comment in comments:
        subreddit = comment['subreddit']

        if subreddit not in post_per_subreddit:
            post_per_subreddit[subreddit] = 1
        else:
            post_per_subreddit[subreddit] += 1

    return post_per_subreddit

def get_post_per_day(comments):
    post_per_day = {}

    for comment in comments:
        # timestamp example: 2025-01-11T16:47:18.922Z
        date = comment['timestamp'].split("T")[0]

        if date not in post_per_day:
            post_per_day[date] = 1
        else:
            post_per_day[date] += 1

    return post_per_day

