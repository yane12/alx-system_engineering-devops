#!/usr/bin/python3
"""
Prototype: def number_of_subscribers(subreddit)
"""
import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'Python:alx-api-advanced:v0.1 (by /u/ohgay_ak4)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers', 0)
