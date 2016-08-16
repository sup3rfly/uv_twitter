from auth import *
from tweepy import Cursor

#This function uses the api.search from Cursor tweepy class to retreive tweets. It receives query as mandatory parameter
# and lang, locale, count, until, items as optional
def search_status(query, lang=None, locale=None, count=None, until=None, items=None):
    response_list=[]

    for status in Cursor(api.search, q=query, lang=lang, locale=locale, count=count, until=until).items(items):
        response_list.append(status)

    return response_list