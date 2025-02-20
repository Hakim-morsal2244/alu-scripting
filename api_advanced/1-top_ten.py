import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    
    # Headers to avoid 403 error (Reddit API requires a User-Agent)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # Make the request and prevent redirection
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Get the list of posts from the JSON response
        posts = response.json().get('data', {}).get('children', [])
        
        # Print the titles of the first 10 posts
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        # If subreddit is invalid or not found, print None
        print(None)
