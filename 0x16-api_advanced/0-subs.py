#!/usr/bin/python3
"""Module looking for the number of subscribers to a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Search the number of subscribers to a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user = {'User-Agent': 'essaket'}
    response = requests.get(url, headers=user, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
