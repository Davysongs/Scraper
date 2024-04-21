# Web Scraping with BeautifulSoup

This project scrapes data from a list of URLs and stores the extracted information in a structured JSON format. It uses Python's BeautifulSoup library to parse HTML and extract relevant information such as titles, text, and links.

## Requirements

To run this project, ensure you have the following software installed:

- Python 3.x
- `pandas` library
- `requests` library
- `beautifulsoup4` library

You can install the required Python libraries using `pip`:

```bash
pip install pandas requests beautifulsoup4
```
## Project Structure

- `scrape-source.xlsx`: Excel file containing the list of URLs to scrape.
- `scrape.py`: Python script that performs the scraping.
- `scraped_data.json`: JSON file where the scraped data is stored.
- `readme.md`: This documentation file.

## How It Works

1. The script `scrape.py` reads the list of URLs from `scrape-source.xlsx`.
2. For each URL, it fetches the page content using the `requests` library and parses it with `BeautifulSoup`.
3. It extracts the following information from each URL:
   - Title of the page
   - All text content on the page
   - All hyperlinks on the page
4. The script stores this information in a structured JSON file (`scraped_data.json`).

## Usage Instructions

To run the scraping script:

1. Ensure that `scrape-source.xlsx` contains the list of URLs to scrape (without headers).
2. Execute `scrape.py` to start scraping:

```bash
python scrape.py
```

3. After the script completes, the scraped data will be available in `scraped_data.json`.

## Notes

- This project is intended for educational purposes and personal use. Be sure to respect website terms of service and robots.txt rules when scraping data.
- Consider rate-limiting or other strategies to avoid overwhelming websites with requests.
```

