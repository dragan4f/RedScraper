def filter_by_keyword(comments, keyword):
    filtered_comments = []

    for comment in comments:
        if keyword.lower() in comment['content'].lower():
            filtered_comments.append(comment)

    return filtered_comments

def filter_by_subreddits(comments, subreddits):
    filtered_comments = []

    for comment in comments:
        if comment['subreddit'] in subreddits:
            filtered_comments.append(comment)

    return filtered_comments

def filter_by_date_range(comments, start_date, end_date):
    filtered_comments = []

    for comment in comments:
        date = comment['timestamp'].split("T")[0]
        if start_date <= date <= end_date:
            filtered_comments.append(comment)

    return filtered_comments