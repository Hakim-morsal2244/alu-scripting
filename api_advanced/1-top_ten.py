#!/usr/bin/python3
<<<<<<< HEAD
"""DOCS"""
=======
"""
Displays the titles of 10 hot posts listed for a subreddit
"""

>>>>>>> 189816bd57617a7921b1598df92b341c257b2b39
import requests


def top_ten(subreddit):
<<<<<<< HEAD
    """Docs"""
    reddit_url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    headers = headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])
    else:
        print(None)
=======
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    params = {'limit': 10}
    
    # Prevent following redirects
    response = requests.get(url, headers=user_agent, params=params, allow_redirects=False)
    
    # If the subreddit does not exist (404 error)
    if response.status_code == 404:
        print("None")
        return

    # If the response is successful
    if response.status_code == 200:
        try:
            results = response.json()
            hot_posts = results.get('data', {}).get('children', [])
            if not hot_posts:
                print("None")
                return

            # Print the titles of the first 10 hot posts
            for post in hot_posts:
                print(post.get('data', {}).get('title', "None"))
        except Exception:
            print("None")
    else:
        print("None")

>>>>>>> 189816bd57617a7921b1598df92b341c257b2b39
