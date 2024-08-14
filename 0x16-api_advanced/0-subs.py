#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the number
of subscribers for a given subreddit. If the subreddit is invalid, the function
returns 0.

Usage:
    from number_of_subscribers import number_of_subscribers

    subscribers = number_of_subscribers("python")
    print(f"Subscribers: {subscribers}")
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers if the subreddit exists, otherwise 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
