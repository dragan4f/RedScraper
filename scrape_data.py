import nodriver as uc
from bs4 import BeautifulSoup

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

    await scroll_to_bottom(page)

    html_content = await page.get_content()
    await page.close()

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

        processed_comments.append({
            "subreddit": subreddit,
            "full_link": full_link,
            "timestamp": datetime,
            "content": content
        })

    return processed_comments