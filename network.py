import random
import contextlib

import requests
from requests.exceptions import RequestException


class NetworkException(BaseException):
    """
    Exception type returned by functions within network module
    """
    pass


def get_content(url):
    """
    Attempts to get the content at `url` by making an html get request.
    If the content-type of response is some kind of html/xml, return the
    text content, otherwise return None.

    Args:
        url (str): url of the website

    Returns:
        bytes: content of the website

    Raises:
        NetworkException: If there is an error getting the website 
            content or the content is empty
    """

    headers = {
        'User-Agent': __get_user_agent()
    }

    try:
        response = requests.get(url, stream=True, headers=headers) 
        with contextlib.closing(response):
            if __successful_response(response) and response.content:
                c = response.content
                return response.content
            else:
                raise NetworkException(f'Error during request to {url}: ' + 
                                        'Request returned a non-200 status ' + 
                                        'code or empty content')

    except RequestException as e:
        raise NetworkException(f'Error during requests to {url}: {e}')


def __get_user_agent():
    """
    Get a common user agent that's gets placed in the header of the html get 
    request

    Returns:
        str: user agent
    """
    
    # Common user agents
    user_agents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 ' +
            '(KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like ' +
            'Gecko) Chrome/48.0.2564.109 Safari/537.36',
        'Mozilla/5.0 (iPad; CPU OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 ' +
            '(KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1'
    ]

    if len(user_agents) > 1:
        ran_index = random.randint(0, len(user_agents) - 1)
        return user_agents[ran_index]
    else:
        return user_agents[0]


def __successful_response(response):
    """
    Was the response successful and html

    Returns:
        bool: True if the response is html, False otherwise
    """
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)
