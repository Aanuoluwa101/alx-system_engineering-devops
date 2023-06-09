#!/usr/bin/python3
""" Total subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    headers = {'User-Agent': 'mercymercy'}
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # load response unit from json
    data = r.json()['data']
    # extract list of pages
    pages = data['children']
    # extract data from first page
    page_data = pages[0]['data']
    # return number of subreddit subs
    return page_data['subreddit_subscribers']
