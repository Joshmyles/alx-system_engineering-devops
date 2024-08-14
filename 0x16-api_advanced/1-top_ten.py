#!/usr/bin/python3
"""
Function to query the Reddit API and print the titles
of the first 10 hot posts for a subreddit. If the subreddit is invalid,
the function prints None.

Usage:
    from top_ten import top_ten

    top_ten("python")
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API, prints the titles of the first 10 hot posts
    for a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Prints:
        titles of first 10 hot posts, or None if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditApp/0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get('data', {}).get('title', None))
        else:
            print(None)
    except requests.RequestException:
        print(None)
