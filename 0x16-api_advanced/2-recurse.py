#!/usr/bin/python3
"""l
ist containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], aft="", count=0):
    """Returns a list of titles of hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "aft": aft,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    aft = results.get("aft")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if aft is not None:
        return recurse(subreddit, hot_list, aft, count)
    return hot_list
