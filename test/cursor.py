import tweepy
from tweepy import Cursor

#UberVU tokens
ckey = 'eVP3L5l1vX6Q20qEWWJBelIfV'
csecret = '27VEuF4qErAGCishfleG5zLvBJ1AAmJ3IoVdYJ75xQQxxga9UG'
atoken = '3575504721-dIpxGbqa4crzDWhwKo16dV56L4lyYHHgi0qczhx'
asecret = 'IzalISFtV5JLLz7XszaFz8ajUPPZhaGMIoG86aTAuIjEC'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
auth.secure = True
api=tweepy.API(auth)


def search_status(query, lang=None, locale=None, count=None, until=None, items=None):
    response_list=[]

    # print "Searching ", query
    for status in Cursor(api.search, q=query, lang=lang, locale=locale, count=count, until=until).items(items):
        # print "Entered for loop"
        # print status.text.encode('utf-8')
        # print "Type:", status.text
        response_list.append(status)
    print response_list
    return response_list

def get_status_by_idd(idd):
    # status = api.user_timeline(id=id)
    for status in api.user_timeline():
        if status.id == idd:
            print status.text
            print status.id
            print status.lang
            print status


# get_status_by_idd(763333508303499264)

# search_status("Test", 763391457952567296)
