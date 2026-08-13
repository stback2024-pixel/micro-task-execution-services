#!/usr/bin/env python3
# Simple task execution script for micro-freelance work.
import requests

def execute_task(task_url):
    # Example: Fetch a web page and return its content.
    response = requests.get(task_url)
    if response.status_code == 200:
        return response.text
    else:
        return 'Failed to fetch task.'

if __name__ == '__main__':
    # Dummy URL for demonstration.
    print(execute_task('https://example.com'))