#!/usr/bin/python3
"""
This script queries the Reddit API and returns the number of total
subscribers for a given subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the
        request fails or the subreddit does not exist.
    """
    try:
        response = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            allow_redirects=False,
            headers={"User-Agent": "your_username_bot-01"},
            timeout=60,
        )
        response.raise_for_status()
        return response.json().get("data", {}).get("subscribers", 0)
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return 0
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return 0

def main(subreddit):
    if not subreddit:
        print("Please provide a subreddit name.")
        return

    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit '{subreddit}' has {subscribers} subscribers.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script_name.py <subreddit>")
    else:
        main(sys.argv[1])
