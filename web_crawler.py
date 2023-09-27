import requests
from bs4 import BeautifulSoup
import csv


def get_urls(primary_category, secondary_category, geography, date_range):

    # Create a search query using the given parameters.
    search_query = f"{primary_category} {secondary_category} {geography} {date_range}"

    # Send a GET request to Google Search and parse the results.
    response = requests.get(f"https://www.google.com/search?q={search_query}")
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the URLs from the search results.
    urls = []
    for link in soup.findAll("a"):
        url = link.get("href")
        if url is not None and url.startswith("/url?q="):
            urls.append(url[7:])

    return urls


def write_urls_to_csv(urls, csv_file_path):

    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["URL"])
        for url in urls:
            writer.writerow([url])


def main():
    # Get the input parameters from the user.
    primary_category = input("Primary Category: ")
    secondary_category = input("Secondary Category: ")
    geography = input("Geography: ")
    date_range = input("Date Range: ")

    # Crawl the web to find URLs that match the given parameters.
    urls = get_urls(primary_category, secondary_category,
                    geography, date_range)

    # Write the URLs to a CSV file.
    csv_file_path = f"urls_{primary_category}_{secondary_category}_{geography}_{date_range}.csv"
    write_urls_to_csv(urls, csv_file_path)

    print(
        f"Successfully wrote {len(urls)} URLs to the CSV file {csv_file_path}.")


if __name__ == "__main__":
    main()
