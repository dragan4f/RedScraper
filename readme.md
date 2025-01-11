# Reddit Comment Scraper

This project scrapes comments from a Reddit user's profile using Selenium WebDriver and BeautifulSoup.

## Prerequisites

- Python 3.12
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

1. Run the script:

    ```sh
    python main.py
    ```

2. The script will scrape comments from the specified Reddit user's profile and print them.

## Configuration

- You can change the Reddit username in the [main.py](http://_vscodecontentref_/0) file by modifying the [username](http://_vscodecontentref_/1) variable.

## Dependencies

- `selenium`
- `beautifulsoup4`
- `webdriver-manager`

## License

This project is licensed under the MIT License.