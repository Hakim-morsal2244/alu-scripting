#!/usr/bin/python3

"""
Displays the titles of 10 hot posts listed for a subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    The function that fetches the Reddit API and prints the titles of the first 10 hot posts.
    """
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    response = get(url, headers=user_agent, params=params)
    if response.status_code != 200:
        print("None")
        return

    try:
        results = response.json()
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
