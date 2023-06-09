#!/usr/bin/python3
""" This module parses the title of all hot articles"""
import re
import requests


def count_words(subreddit, word_list, next_page=None, word_count={}):
    """parses the title of all hot articles,
       and prints a sorted count of given keywords"""

    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)

    if next_page:
        url += '?after={}'.format(next_page)

    user_agent = "mercymercy"
    headers = {'User-Agent': 'mercymercy'}

    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return
    word_list = [word.lower() for word in word_list]
    data = r.json()['data']
    children = data['children']

    for word in word_list:
        for child in children:
            title = child['data']['title']
            matches = re.findall(word, title, flags=re.IGNORECASE)

            if len(matches) != 0:
                if word in word_count:
                    word_count[word] += len(matches)
                else:
                    word_count[word] = len(matches)

    next_page = data['after']
    if next_page:
        count_words(subreddit, word_list, next_page, word_count)
    else:
        keys = sorted(list(word_count.keys()))
        for key in keys:
            print(key + ': ' + str(word_count[key]))
