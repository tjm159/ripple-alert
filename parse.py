import re

from bs4 import BeautifulSoup


class ParseException(BaseException):
    """
    Exception type returned by functions within parse
    """
    pass


def parse_content(content):
    """
    Attempts to parse the version from the html. This is specific to
    Ripple website design to download the file name. This must change
    if the Ripple site DOM changes.

    Args:
        content (bytes): website html content

    Returns:
        str: trellis version from the html content

    Raises:
        ParseException: If there is an error parsing the website content
    """
    html = BeautifulSoup(content, 'html.parser')
    for a in html.select('a'):
        href = a['href']
        match = re.search(r'(trellis-).+(.msi)$', href)
        if match:
            v = match.group(0)
            v = __remove_prefix(v, 'trellis-')
            v = __remove_suffix(v, '-x86.msi')
            return v
    raise ParseException('Error during parsing: Unable to find trellis href within the given content')


def __remove_prefix(text, prefix):
    """
    Removes the given prefix from the given text

    Args:
        text (str): text to be manipulated
        prefix (str): prefix to remove from text

    Returns:
        str: text with prefix removed
    """
    if text.startswith(prefix):
        return text[len(prefix):]
    return text 


def __remove_suffix(text, suffix):
    """
    Removes the given suffix from the given text

    Args:
        text (str): text to be manipulated
        suffix (str): suffix to remove from text

    Returns:
        str: text with suffix removed
    """
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text 