import csv
from playwright.sync_api import sync_playwright

def initialize_browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    return browser, page

def scrape_listings(url):
    browser, page = initialize_browser()
    page.goto(url)
    listings = []
    for listing in page.query_selector_all('.listing'):
        title = listing.query_selector('.title').inner_text()
        price = listing.query_selector('.price').inner_text()
        location = listing.query_selector('.location').inner_text()
        description = listing.query_selector('.description').inner_text()
        listings.append({
            'title': title,
            'price': price,
            'location': location,
            'description': description
        })
    browser.close()
    return listings

def save_to_csv(data, output_file):
    keys = data[0].keys()
    with open(output_file, 'w', newline='') as output:
        dict_writer = csv.DictWriter(output, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def main(url, output_file):
    listings = scrape_listings(url)
    save_to_csv(listings, output_file)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Scrape real estate listings.')
    parser.add_argument('--url', required=True, help='URL of the property listings page to scrape')
    parser.add_argument('--output', required=True, help='Output CSV file')
    args = parser.parse_args()
    main(args.url, args.output)
