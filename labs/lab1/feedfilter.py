
import feedparser
import re

# Takes a filename of URL of a blog feed and classifies the entries
def read(feed,classifier):
  # Get feed entries and loop over them
  f=feedparser.parse(feed)
  for entry in f['entries']:
    print
    print '-----'

    # Print the contents of the entry
    print u'Title: '+entry['title']
    print u'Publisher: '+entry['publisher']
    print
    print entry['summary']
    
    # Combine all the text to create one item for the classifier
    fulltext='%s' % (entry['summary'])
    
    # Print the best guess at the current category
    print u'Guess: '+str(classifier.classify(fulltext))
    # Ask the user to specify the correct category and train on that
    cl=raw_input('Enter category: ')
    classifier.train(fulltext,cl)
    
# Takes a filename of URL of a blog feed and classifies the entries
def test(feed,classifier):
  # Get feed entries and loop over them
  f=feedparser.parse(feed)
  for entry in f['entries']:
    print
    print '-----'

    # Print the contents of the entry
    print u'Title: '+entry['title']
    print u'Publisher: '+entry['publisher']
    print
    print entry['summary']
    
    # Combine all the text to create one item for the classifier
    fulltext='%s' % (entry['summary'])
    
    # Print the best guess at the current category
    print u'Guess: '+str(classifier.classify(fulltext))