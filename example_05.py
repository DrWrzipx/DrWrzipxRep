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
    print_words(story_words)

def print_words(story_words):
    for word in story_words:
        print(word)

if __name__ == "__main__":
    fetch_words()
