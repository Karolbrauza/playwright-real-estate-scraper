# Real Estate Listings Scraper

This project is a simple web scraper that extracts real estate listings from property websites like Zillow or Realtor. The scraper uses Playwright to navigate the website and extract details such as property title, price, location, and description. The scraped data is then stored in a CSV file for further analysis.

## Installation and Dependencies

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Running the Scraper

To run the scraper, execute the following command:

```bash
python scraper.py --url <URL> --output <OUTPUT_FILE>
```

Replace `<URL>` with the URL of the property listings page you want to scrape, and `<OUTPUT_FILE>` with the name of the CSV file where the scraped data will be saved.
