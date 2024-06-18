#!/usr/bin/python3
"""
Query Reddit API to retrieve subreddit posts recursively using pagination.
"""

import requests

def recurse(subreddit, hot_list=[], next_page=None, count=0):
    """
    Request subreddit posts recursively using pagination.
    """
    # Set a custom User-Agent header to identify the source of the request
    user_agent = '0x16-api_advanced-jmajetich'

    # Construct the URL for the subreddit's JSON data
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # If a next_page is specified, add it as a parameter to the URL
    if next_page:
        url += f'?after={next_page}'

    # Include the custom User-Agent header in the request to avoid request limitations
    headers = {'User-Agent': user_agent}

    # Make a GET request to the Reddit API, avoiding redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (HTTP 200 status code)
    if response.status_code != 200:
        return None

    # Extract the 'data' section from the JSON response
    data = response.json()['data']

    # Extract the list of 'children' (posts) from the data
    posts = data['children']

    # Iterate through the posts and append titles to the hot_list
    for post in posts:
        count += 1
        hot_list.append(post['data']['title'])

    # Get the 'after' token for the next page
    next_page = data['after']

    # If there is a next page, recursively call the function
    if next_page is not None:
        return recurse(subreddit, hot_list, next_page, count)
    else:
        # Return the hot_list when there are no more pages
        return hot_list
