#!/usr/bin/python3
"""
This module provides a function to recursively query the Reddit API, parse the titles
of all hot articles, and print a sorted count of given keywords.

Usage:
    from count_words import count_words

    count_words("python", ["python", "javascript", "java"])
"""

import requests
import re
from collections import Counter

def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the titles.
        after (str): The "after" parameter for pagination (used in recursion).
        word_count (Counter): A Counter object to accumulate counts (used in recursion).

    Prints:
        A sorted count of keywords in descending order by count, and alphabetically if tied.
    """
    if word_count is None:
        word_count = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            title_words = re.findall(r'\b\w+\b', title)
            title_count = Counter(title_words)

            for word in word_list:
                word_count[word.lower()] += title_count[word.lower()]

        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")

    except requests.RequestException:
        return
