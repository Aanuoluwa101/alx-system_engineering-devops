#!/usr/bin/python3
"""Query Reddit API to determine subreddit's hot article count
"""

import requests


def recurse(subreddit, hot_list=[], next_page=None):
    """Request subreddit recursively using pagination
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    # if page specified, pass as parameter
    if next_page:
        url += '?after={}'.format(next_page)
    headers = {'User-Agent': '0x16-api_advanced-mercymercy'}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return None

    # load response unit from json
    data = r.json()['data']

    # extract list of pages
    posts = data['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    next_page = data['after']
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page)
    else:
        return hot_list
