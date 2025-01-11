class Comment:
    def __init__(self, subreddit, link, timestamp, content):
        self.subreddit = subreddit
        self.link = link
        self.timestamp = timestamp
        self.content = content

    def to_dict(self):
        return {
            "subreddit": self.subreddit,
            "link": self.link,
            "timestamp": self.timestamp,
            "content": self.content
        }

    def __repr__(self):
        return f"Subreddit: {self.subreddit}\nLink: {self.link}\nTimestamp: {self.timestamp}\nContent: {self.content}\n"