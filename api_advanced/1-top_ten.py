#!/usr/bin/python3

"""
Displays the titles of 10 hot posts listed for a subreddit
"""

from requests import get
import subprocess


def top_ten(subreddit):
    """
    The Function that fetches the Reddit API
    """
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params, allow_redirects=False)

    # Check for valid subreddit (status code 200)
    if response.status_code == 200:
        try:
            results = response.json()
            my_data = results.get('data').get('children')

            # Print titles of the top 10 posts
            for i in my_data:
                print(i.get('data').get('title'))

        except Exception:
            print("None")
    elif response.status_code == 404:
        # If subreddit does not exist, print None
        print("None")
    else:
        # Handle other errors (like 403, etc.)
        print("None")
