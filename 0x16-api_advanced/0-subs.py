#!/usr/bin/python3
"""
Query Reddit API to retrieve the subscriber count of a subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Request the number of subscribers for a subreddit from the Reddit API.

    Args:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the specified subreddit.
           Returns 0 if the subreddit or API endpoint is not found.
    """
    # Set a custom User-Agent header to identify the source of the request
    user_agent = '0x16-api_advanced-jmajetich'

    # Construct the URL for the subreddit's JSON data
    url = f'https://www.reddit.com/r/{subreddit}/json'

    # Include the custom User-Agent header in the request to avoid request limitations
    headers = {'User-Agent': user_agent}

    # Make a GET request to the Reddit API, avoiding redirects
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (HTTP 200 status code)
    if response.status_code != 200:
        # Return 0 if the subreddit or API endpoint is not found
        return 0

    # DATA PARSING
    # Extract the 'data' section from the JSON response
    data = response.json()['data']

    # Extract the list of 'children' (pages) from the data
    pages = data['children']

    # Extract the data from the first page
    first_page_data = pages[0]['data']

    # Return the number of subreddit subscribers from the first page
    return first_page_data['subreddit_subscribers']

# Example usage:
# subreddit = 'example'
# subscribers_count = number_of_subscribers(subreddit)
# print(f'The number of subscribers in r/{subreddit}: {subscribers_count}')
