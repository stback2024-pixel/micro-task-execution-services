#!/usr/bin/env python
# Simple task executor service for hire - $1 per hour
import requests
from bs4 import BeautifulSoup

def simple_scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return str(soup.prettify())

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: python simple_task_executor.py URL')
    else:
        url = sys.argv[1]
        result = simple_scrape(url)
        print(result)