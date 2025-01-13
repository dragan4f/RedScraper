# Reddit Comment Scraper

THis projec scrapes comments from a Reddit user's profile using [nodriver](https://github.com/ultrafunkamsterdam/nodriver), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [Flask](https://flask.palletsprojects.com/en/stable/).

## Prerequisites
- Python 3.13.1
- Google Chrome browser

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/redScraper.git
    cd redScraper
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

- For the command line interface:
    ```sh
    python cli.py
    ```

- For the web interface:
    ```sh
    python server.py
    ```

## License

This project is licensed under the MIT License.