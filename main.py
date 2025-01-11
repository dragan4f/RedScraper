import nodriver as uc
from pprint import pprint
import json


async def get_comment_data(comment):
    comment_link = "https://reddit.com" + comment.attrs['href']
    # example link: /r/unitedkingdom/comments/1hy5p0o/comment/m6eqdvn/
    comment_subreddit = comment.attrs['href'].split("/comments/")[0]

    content_el = await comment.query_selector(".md")
    content = content_el.text

    datetime_el = await comment.query_selector("time")
    datetime = datetime_el.attributes[1]

    return {
        "link": comment_link,
        "subreddit": comment_subreddit,
        "timestamp": datetime,
        "content": content
    }

async def main():
    username = "Venoosian"
    url = "https://www.reddit.com/user/" + username

    processed_comments = []

    browser = await uc.start()
    page = await browser.get(url)

    await page.wait_for("shreddit-profile-comment")
    await page.wait(0.1)

    # scroll until the bottom of the page
    cur_height = await page.evaluate("document.body.scrollHeight")
    while True:
        await page.scroll_down(900)
        new_height = await page.evaluate("document.body.scrollHeight")

        if new_height == cur_height:
            break

        cur_height = new_height

    comments = await page.select_all("shreddit-profile-comment")
    print(len(comments))
    
    for comment in comments:
        data = await get_comment_data(comment)
        processed_comments.append(data)
        # save data to json file
        with open("comments.json", "w") as f:
            json.dump(processed_comments, f, indent=4)


if __name__ == "__main__":
    uc.loop().run_until_complete(main())
