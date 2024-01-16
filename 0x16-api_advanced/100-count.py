#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, after='', word_dct={}):
    """ queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    """

    if not word_dct:
        for word in word_list:
            if word.lower() not in word_dct:
                word_dct[word.lower()] = 0

    if after is None:
        wordct = sorted(word_dct.items(), key=lambda x: (-x[1], x[0]))
        for word in wordct:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dct.keys():
                word_dct[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, word_dct)
