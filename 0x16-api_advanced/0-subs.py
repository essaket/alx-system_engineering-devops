#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
  """returns total subs"""
  header = {"User-Agent": "Holberton"}
  url = "https://www.reddit.com/r/" + subreddit + "/about.json"
  try:
    r = requests.get(url, headers=header, allow_redirects=False)
    r.raise_for_status()  # Raise an exception for non-200 status codes
  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    return 0
  else:
    # Successful request processing
    return r.json().get("data", None).get("subscribers", None)

if __name__ == "__main__":
  pass
