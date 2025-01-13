from flask import Flask, request, jsonify, render_template
import json

import scrape_data
import analyze

app = Flask(__name__)

def load_saved_comments():
    try:
        with open("saved_comments.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
saved_comments = load_saved_comments()

def save_comments(comments, username):
    with open("saved_comments.json", "w") as file:
        saved_comments[username] = comments
        json.dump(saved_comments, file, indent=4)

def get_page_data(comments):
    return {
        "comments": comments,
        "subreddits": set([comment["subreddit"] for comment in comments]),
        "post_per_subreddit": analyze.get_post_per_subreddit(comments),
        "post_per_day": analyze.get_post_per_day(comments)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_user_comments', methods=['POST'])
def get_comments():
    username = request.form['username']

    if username in saved_comments:
        comments = saved_comments[username]
    else:
        comments = scrape_data.get_user_comments(username)
        save_comments(comments, username)

    return render_template('comments_analysis.html', data=get_page_data(comments))

