#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints 
the titles of the first 10 hot posts listed for a given subreddit.
If the subreddit is invalid, it prints None.
"""

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    posts = response.json().get('data', {}).get('children', [])
    
    for post in posts:
        print(post['data']['title'])
