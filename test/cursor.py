import tweepy
from tweepy import Cursor

#UberVU tokens
ckey = 'eVP3L5l1vX6Q20qEWWJBelIfV'
csecret = '27VEuF4qErAGCishfleG5zLvBJ1AAmJ3IoVdYJ75xQQxxga9UG'
atoken = '3575504721-dIpxGbqa4crzDWhwKo16dV56L4lyYHHgi0qczhx'
asecret = 'IzalISFtV5JLLz7XszaFz8ajUPPZhaGMIoG86aTAuIjEC'

#@test_uv Authentication
# ckey = 'S3W51f9vpvWK2gRoLG9w9fz1l'
# csecret = 'vgJHFsxvy3t7mID2L4ZGL7dhymu1qvPnkycNFaQT7nnR9GR1vo'
# atoken = '760375819655151616-CNp2ujYnjZMBp5RalaM5ZzPexU6DEy3'
# asecret = 'CuK407eQiGxVJAyKqed5G9msEu0USsliVIaGYzTNekaYO'


#crazyl3gs token receive
# ckey = 'EcG2ogmD07Qus9NKweIqbhOlB'
# csecret = 'hNSzioCFHbudHM9IK01zm9bvcQXVCwBNJ1V8zel4snFgPctgeV'
# atoken = '24415614-LdZhU1T28K5GbZKS8k2pVusckZ3Aa1JEiTOeIVUdp'
# asecret = '2XehmQi33fNoKHuu0p0JQhNUGbp9zN4tDYklWe7v7UHie'

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
#    print response_list
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
