try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
story = urlopen('https://www.python.org')
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)
print(story_words)
