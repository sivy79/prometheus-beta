import requests
import socket
import urllib.parse

def is_website_online(url: str, timeout: float = 5.0) -> bool:
    """
    Check if a website is online by attempting to connect and get a response.

    Args:
        url (str): The URL of the website to check.
        timeout (float, optional): Connection timeout in seconds. Defaults to 5.0.

    Returns:
        bool: True if the website is online, False otherwise.

    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Validate input
    if not url or not isinstance(url, str):
        raise ValueError("URL must be a non-empty string")

    # Ensure the URL has a scheme
    if not urllib.parse.urlparse(url).scheme:
        url = f"https://{url}"

    try:
        # Attempt to resolve domain name
        parsed_url = urllib.parse.urlparse(url)
        socket.gethostbyname(parsed_url.netloc)

        # Attempt to get the website response
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        
        # Check if the response indicates a successful connection
        return response.status_code < 400

    except (requests.RequestException, socket.gaierror):
        # Catch connection errors, DNS lookup failures, etc.
        return False