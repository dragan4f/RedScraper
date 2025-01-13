from pprint import pprint

import filters
import scrape

help_message = """
    Enter 'exit' to exit the program.
    Enter 'help' to view this menu.
    Enter 'get {username}' to get comments of a user.
    Enter 'show' to display all comments.
    Enter 'filter key {keyword}' to filter comments by keyword.
    Enter 'filter sub {subreddit}' to filter comments by subreddit.
    Enter 'filter date {start_date} {end_date}' to filter comments by date range.
    """

def run_cli():
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
            user_comments = scrape.get_user_comments(username)

        elif command == "show":
            pprint(user_comments)

        elif command.startswith("filter"):
            if len(user_comments) == 0:
                print("No comments to filter. Enter 'get {username}' to get comments of a user.")
                continue

            filter_type = command.split(" ")[1]

            if filter_type == "key":
                keyword = command.split(" ")[2]

                pprint(
                    filters.filter_by_keyword(user_comments, keyword)
                )

            elif filter_type == "sub":
                subreddit = command.split(" ")[2]

                pprint(
                    filters.filter_by_subreddits(user_comments, subreddit)
                )

            elif filter_type == "date":
                start_date = command.split(" ")[2]
                end_date = command.split(" ")[3]

                pprint(
                    filters.filter_by_date_range(user_comments, start_date, end_date)
                )

            else:
                print("Invalid filter type. Enter 'help' to view the menu.")

        else:
            print("Invalid command. Enter 'help' to view the menu.")

if __name__ == "__main__":
    run_cli()