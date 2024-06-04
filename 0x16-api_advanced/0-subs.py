#!/usr/bin/python3
"""0-subs

Run ./0-main.py programming or ./0-main.py this_is_a_fake_subreddit for testing
"""

import requests


def number_of_subscribers(subreddit):
  """
  This function queries the Reddit API and returns the number of subscribers
  for a given subreddit.

  Args:
      subreddit: The name of the subreddit (without the 'r/').

  Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit
      is invalid.
  """
  # Base URL for subreddit information
  url = f"https://www.reddit.com/r/{subreddit}/about.json"

  # Set a custom User-Agent header to avoid throttling
  headers = {"User-Agent": "MyCoolScript (by /u/your_username)"}

  # Send a GET request without following redirects
  response = requests.get(url, headers=headers, allow_redirects=False)

  # Check for successful response (200 OK)
  if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Check if 'data' and 'subscribers' keys exist (valid subreddit)
    if 'data' in data and 'subscribers' in data['data']:
      return data['data']['subscribers']

  # Invalid subreddit or error, return 0 subscribers
  return 0
