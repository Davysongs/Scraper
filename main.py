import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

# Read the Excel file
# the file name should be ''scrape-source.xlsx''
df = pd.read_excel('scrape-source.xlsx', header=None)

# Function to scrape data from a URL in the spreadsheet 
def scrape_data(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant MB 
        # For demonstration, just extracting all links
        links = [link.get('href') for link in soup.find_all('a')]

        return links
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []

# Dictionary to store scraped data
scraped_data = {}

# Iterate over each URL in the Excel file and scrape data
for index, row in df.iterrows():
    for url in row:
        if isinstance(url, str):
            scraped_data[url] = scrape_data(url)

# Save scraped data to JSON file
with open('scraped_data.json', 'w') as f:
    json.dump(scraped_data, f, indent=4)

print("Scraping completed. Data saved to scraped_data.json.")
