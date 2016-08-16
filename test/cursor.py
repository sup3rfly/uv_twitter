import tweepy
from auth import *
from tweepy import Cursor

def search_status(query, lang=None, locale=None, count=None, until=None, items=None):
    response_list=[]

    # print "Searching ", query
    for status in Cursor(api.search, q=query, lang=lang, locale=locale, count=count, until=until).items(items):
        # print "Entered for loop"
        # print status.text.encode('utf-8')
        # print "Type:", status.text
        response_list.append(status)
#    print response_list
    return response_list

# search_status("Test", 763391457952567296)