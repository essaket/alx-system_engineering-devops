#!/usr/bin/python3
""" Number of subscribers """


from requests import get, session


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """
    username = 'HiSaysMoody'
    password = 'ALXtest1#'
    headers = {"User-Agent": "Mozilla/5.0"}
    se4 = session()
    se4.headers = headers
    user_pass_dict = {'user': username,
                      'passwd': password,
                      'api_type': 'json'}
    r = se4.post(r'https://www.reddit.com/api/login', data=user_pass_dict)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = se4.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    if "data" not in data:
        return 0
    if "subscribers" not in data["data"]:
        return 0
    return data["data"]["subscribers"]
