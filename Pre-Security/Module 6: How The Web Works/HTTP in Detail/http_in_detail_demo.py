"""
HTTP in Detail Demo

This script supports my TryHackMe HTTP in Detail notes by making
a basic HTTP GET request and displaying key parts of the response.
"""

import requests


def inspect_http_response(url):
    response = requests.get(url, timeout=10)

    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Server:", response.headers.get("Server"))
    print("Cookies:", response.cookies)
    print("\nResponse Preview:")
    print(response.text[:500])


if __name__ == "__main__":
    inspect_http_response("https://example.com")
