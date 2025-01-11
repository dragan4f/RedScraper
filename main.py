import nodriver as uc
from pprint import pprint
import json
from bs4 import BeautifulSoup

class Comment:
    def __init__(self, subreddit, link, timestamp, content):
        self.subreddit = subreddit
        self.link = link
        self.timestamp = timestamp
        self.content = content

    def __repr__(self):
        return f"Subreddit: {self.subreddit}\nLink: {self.link}\nTimestamp: {self.timestamp}\nContent: {self.content}\n"

async def scroll_to_bottom(page):
    cur_height = await page.evaluate("document.body.scrollHeight")
    new_height = 0

    while new_height != cur_height:
        cur_height = new_height

        await page.scroll_down(900)
        new_height = await page.evaluate("document.body.scrollHeight")

async def get_html_content(username):
    url = "https://www.reddit.com/user/" + username

    browser = await uc.start()
    page = await browser.get(url)

    await page.wait_for("shreddit-profile-comment")
    await page.wait(0.1)

    # await scroll_to_bottom(page)

    html_content = await page.get_content()

    return html_content

def get_user_comments(username):
    html_content = uc.loop().run_until_complete(
        get_html_content(username)
    )

    soup = BeautifulSoup(html_content, 'html.parser')

    comments = soup.find_all("shreddit-profile-comment")
    processed_comments = []

    for comment in comments:
        # example link: /r/unitedkingdom/comments/1hy5p0o/comment/m6eqdvn/
        subreddit = comment.attrs['href'].split("/comments/")[0]
        full_link = "https://reddit.com" + comment.attrs['href']
        content = comment.find("div", class_="md").text.strip()
        datetime = comment.find("time").attrs['datetime']

        processed_comments.append(
            Comment(subreddit, full_link, datetime, content)
        )

    return processed_comments

def filter_comments(comments, keyword):
    filtered_comments = []

    for comment in comments:
        if keyword.lower() in comment.content.lower():
            filtered_comments.append(comment)

    return filtered_comments

def filter_subreddits(comments, subreddits):
    filtered_comments = []

    for comment in comments:
        if comment.subreddit in subreddits:
            filtered_comments.append(comment)

    return filtered_comments

def filter_date_range(comments, start_date, end_date):
    filtered_comments = []

    for comment in comments:
        date = comment.timestamp.split("T")[0]
        if start_date <= date <= end_date:
            print(date, "match")
            filtered_comments.append(comment)

    return filtered_comments

def cli():
    help_message = """
    Enter 'exit' to exit the program.
    Enter 'help' to view this menu.
    Enter 'get {username}' to get comments of a user.
    Enter 'show' to display all comments.
    Enter 'save' to save comments to a file.
    Enter 'filter key {keyword}' to filter comments by keyword.
    Enter 'filter sub {subreddit}' to filter comments by subreddit.
    Enter 'filter date {start_date} {end_date}' to filter comments by date range.
    """
    
    print("Welcome to Reddit Comment Scraper!")
    print(help_message)

    user_comments = []

    while True:
        command = input("Enter command: ")

        if command == "exit":
            exit()

        elif command == "help":
            print(help_message)

        elif command.startswith("get"):
            username = command.split(" ")[1]
            user_comments = get_user_comments(username)

        elif command == "show":
            pprint(user_comments)

        elif command == "save":
            with open("comments.json", "w") as f:
                json.dump(user_comments, f, indent=4)
            print("Comments saved to comments.json.")

        elif command.startswith("filter"):
            if len(user_comments) == 0:
                print("No comments to filter. Enter 'get {username}' to get comments of a user.")
                continue

            filter_type = command.split(" ")[1]

            if filter_type == "key":
                keyword = command.split(" ")[2]
                print(keyword)
                pprint(
                    filter_comments(user_comments, keyword)
                )

            elif filter_type == "sub":
                subreddit = command.split(" ")[2]
                pprint(
                    filter_subreddits(user_comments, subreddit)
                )

            elif filter_type == "date":
                start_date = command.split(" ")[2]
                end_date = command.split(" ")[3]
                pprint(
                    filter_date_range(user_comments, start_date, end_date)
                )

            else:
                print("Invalid filter type. Enter 'help' to view the menu.")

        else:
            print("Invalid command. Enter 'help' to view the menu.")

cli()