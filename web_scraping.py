import requests
from bs4 import BeautifulSoup
import time
import csv

def scrape_article_content(article_url):
    time.sleep(1)  # Delay for responsible scraping
    response = requests.get(article_url)
    if response.status_code != 200:
        return None

    article_soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = article_soup.find_all("p", {"data-component": "paragraph"})
    paragraphs2 = article_soup.find_all("p", {"class": "article__body-text"})
    content = ' '.join([p.get_text() for p in paragraphs + paragraphs2])
    return content

def scrape_economist(topic, pages=10):
    base_url = "https://www.economist.com/search?q={}"
    articles = []

    for page in range(1, pages + 1):
        time.sleep(1)  # Delay for responsible scraping
        url = base_url.format(topic) + "&page=" + str(page)
        response = requests.get(url)
        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract links from <a> tags with class "_search-result"
        for link in soup.find_all("a", class_="_search-result"):
            article_url = link['href']

            content = scrape_article_content(article_url)
            articles.append({"link": article_url, "content": content})

    # Write data to a CSV file
    output_csv = topic + ".csv"
    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["link", "content"])
        writer.writeheader()
        for article in articles:
            writer.writerow(article)

    print(f"Data saved to {output_csv}")

# Scrape articles on a specific topic and save to CSV
scrape_economist("Palestine")