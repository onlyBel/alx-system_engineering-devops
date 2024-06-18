#!/usr/bin/python3
"""
Query Reddit API to count occurrences of keywords in subreddit post titles.
"""

import requests

def count_words(subreddit, word_list, count_list=[], next_page=None):
    """
    Request subreddit posts recursively using pagination and count occurrences of keywords.
    """
    # Convert word_list to a list of dictionaries with count initialized to 0
    if not count_list:
        for word in word_list:
            count_list.append({'keyword': word, 'count': 0})

    # NETWORKING
    # Set a custom User-Agent header to identify the source of the request
    user_agent = '0x16-api_advanced-jmajetich'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # If a next_page is specified, add it as a parameter to the URL
    if next_page:
        url += '?after={}'.format(next_page)

    headers = {'User-Agent': user_agent}

    # Make a GET request to the Reddit API, avoiding redirects
    r = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (HTTP 200 status code)
    if r.status_code != 200:
        return

    # DATA PARSING
    # Load the response unit from JSON
    data = r.json()['data']

    # Extract the list of 'children' (posts) from the data
    posts = data['children']

    # Iterate through posts and count occurrences of keywords in titles
    for post in posts:
        title = post['data']['title']
        for item in count_list:
            title_lower = title.lower()
            title_list = title_lower.split()
            item['count'] += title_list.count(item['keyword'].lower())

    # Get the 'after' token for the next page
    next_page = data['after']

    # If there is a next page, recursively call the function
    if next_page is not None:
        return count_words(subreddit, word_list, count_list, next_page)
    else:
        # Sort the list of dictionaries by count and keyword
        sorted_list = sorted(count_list,
                             key=lambda word: (word['count'], word['keyword']),
                             reverse=True)
        keywords_matched = 0

        # Print keywords and their counts for keywords that have occurrences
        for word in sorted_list:
            if word['count'] > 0:
                print('{}: {}'.format(word['keyword'], word['count']))
                keywords_matched += 1
        return
