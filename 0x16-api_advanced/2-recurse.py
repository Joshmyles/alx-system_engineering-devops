#!/usr/bin/python3
"""
Function to recursively query the Reddit API and return
a list containing the titles of all hot articles for a given subreddit. If no
results are found, returns None.

Usage:
    from recurse import recurse

    titles = recurse("python")
    print(titles)
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): list to store titles of hot articles (recursive).
        after (str): The "after" parameter for pagination (recursive).

    Returns:
        list: list of titles of hot articles, or None if no results
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url,
                headers=headers,
                params=params,
                allow_redirects=False
                )
        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)

        if not children:
            return hot_list if hot_list else None

        for child in children:
            hot_list.append(child.get('data', {}).get('title', None))

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.RequestException:
        return None
