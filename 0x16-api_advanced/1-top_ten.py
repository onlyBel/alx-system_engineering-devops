#!/usr/bin/python3
"""
Query Reddit API to retrieve the top ten hot posts of a subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Request the top ten hot posts of a subreddit from the Reddit API.
    """
    # Set a custom User-Agent header to identify the source of the request
    user_agent = '0x16-api_advanced-jmajetich'

    # Construct the URL for the subreddit's JSON data, limiting to top ten hot posts
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    # Include the custom User-Agent header in the request to avoid request limitations
    headers = {'User-Agent': user_agent}

    # Make a GET request to the Reddit API, avoiding redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (HTTP 200 status code)
    if response.status_code != 200:
        # Print 'None' if the subreddit or API endpoint is not found
        print('None')
    else:
        # Extract the 'data' section from the JSON response
        data = response.json()['data']

        # Extract the list of 'children' (posts) from the data
        posts = data['children']

        # Print the titles of the top ten hot posts
        for post in posts:
            print(post['data']['title'])
