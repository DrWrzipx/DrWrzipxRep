try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

def fetch_words():
    story = urlopen('https://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.split()
        for word in line_words:
            story_words.append(word)
    print_items(story_words)

def print_items(items):
    for item in items:
        print(item)

if __name__ == "__main__":
    fetch_words()
