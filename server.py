from flask import Flask, request, jsonify, render_template
import json

import scrape
import analyse
import filters

app = Flask(__name__)

def get_comments_from_file():
    with open("saved_comments.json", "r") as file:
        return json.load(file)

def save_comments_to_file(comments, username):
    saved_comments = get_comments_from_file()

    with open("saved_comments.json", "w") as file:
        saved_comments[username] = comments
        json.dump(saved_comments, file, indent=4)

def get_page_data(comments, username):
    return {
        "comments": comments,
        "subreddits": set([comment["subreddit"] for comment in comments]),
        "post_per_subreddit": analyse.get_post_per_subreddit(comments),
        "post_per_day": analyse.get_post_per_day(comments),
        "username": username
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_user_comments', methods=['POST'])
def get_comments():
    username = request.form['username']

    saved_comments = get_comments_from_file()

    if username in saved_comments:
        comments = saved_comments[username]
    else:
        comments = scrape.get_user_comments(username)
        save_comments_to_file(comments, username)

    return render_template('analysis.html', data=get_page_data(comments, username))

@app.route('/filter_comments', methods=['POST'])
def filter_comments():
    subreddit = request.form['subreddit']
    from_date = request.form['date-start']
    end_date = request.form['date-end']
    search_term = request.form['search-term']
    username = request.form['username']

    comments = get_comments_from_file()[username]

    if subreddit != "all":
        comments = filters.filter_by_subreddits(comments, [subreddit])

    if from_date and end_date:
        comments = filters.filter_by_date_range(comments, from_date, end_date)

    if search_term:
        comments = filters.filter_by_keyword(comments, search_term)

    return render_template('analysis.html', data=get_page_data(comments, username))

if __name__ == '__main__':
    app.run()