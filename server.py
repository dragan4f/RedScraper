from flask import Flask, request, jsonify, render_template
import json

from get_data import get_user_comments
from analyze import get_post_per_subreddit, get_post_per_day

saved_comments = json.load(open("comments.json"))

unique_subreddits = set([comment['subreddit'] for comment in saved_comments])

page_data = {
    "comments": saved_comments,
    "subreddits": unique_subreddits,
    "post_per_subreddit": get_post_per_subreddit(saved_comments),
    "post_per_day": get_post_per_day(saved_comments)
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=page_data)

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    print(username)
    comments = get_user_comments(username)

    return jsonify([comment.to_dict() for comment in comments])

