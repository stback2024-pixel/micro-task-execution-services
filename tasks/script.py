#!/usr/bin/env python
# Simple web scraping service for hire
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python script.py URL')
        sys.exit(1)
    url = sys.argv[1]
    result = scrape_website(url)
    with open('output.html', 'w') as f:
        f.write(result)