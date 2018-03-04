"""Retrieve and print words from a URL
Usage:
Python 2.7
"""

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL.
    Args:
        url: The URL of a UTF-8 text document
    
    Returns:
        A list of strings containing the words from
        the document.
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
    print_items(story_words)


def print_items(items):
    """Print items one per line.
    Args: 
        An iterable series of printable items
    """
    for item in items:
        print(item)

if __name__ == "__main__":
    web_side_address = 'https://sixty-north.com/c/t.txt'  # Url of example website document
    fetch_words(web_side_address)
