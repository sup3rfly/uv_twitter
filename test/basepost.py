import time, datetime, string, random
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#UberVU tokens
ckey = 'eVP3L5l1vX6Q20qEWWJBelIfV'
csecret = '27VEuF4qErAGCishfleG5zLvBJ1AAmJ3IoVdYJ75xQQxxga9UG'
atoken = '3575504721-dIpxGbqa4crzDWhwKo16dV56L4lyYHHgi0qczhx'
asecret = 'IzalISFtV5JLLz7XszaFz8ajUPPZhaGMIoG86aTAuIjEC'

# Authentication
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
auth.secure = True
api=tweepy.API(auth)

usertest = api.get_user(screen_name = '@test_uv')

#function that creates a random id needed to have unique tweets
#TODO create custom rand function
def create_random_id(self):
    #default random
    random_id = '' + ''.join([random.choice(string.ascii_letters) for n in xrange(6)])
    random_id = unicode(random_id.lower())
    return random_id



#doesn't work as intended
def update_language(language):
    # api.update_profile(lang=language)
    # print "The language", language
    api.set_settings(lang=language)
    #TODO: not sure if there is a time limitation on how early the language is changed
    time.sleep(10)



def post_status(status, in_reply_to_status_id=None, lat=None, long=None):
    # print "\nEntered post_status\nStatus to post:", status
    try:
        # print "\nTweeting"
        tweet = api.update_status(status, in_reply_to_status_id=in_reply_to_status_id, lat=lat, long=long)
        # print "Tweeted\n",
        # time.sleep(30)

    except tweepy.TweepError as e:
        print "TweepError reason: ", e.reason
        return e.reason
    return tweet

def destroy(destroy_id):

    try:
        print "\nDestroying..."
        api.destroy_status(destroy_id)
        time.sleep(90) #wait a little for the server to kick in
        print "\nDestroyed"

    except tweepy.TweepError as e:
        print e.reason
        return e.reason
    print "aici"
    return destroy_id


def whoami(self):
    print self.screen_name
    return self.screen_name


#Search someting
# search_test('#Bucharest')


# random_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
# # Tweet something
# tweet = "@crazyl3gs " + random_string + " >>>" + datetime.datetime.now().time().isoformat()
# print "The tweet: "
# print tweet
# post_status(tweet)

# whoami(usertest)

# create_random_id(self)
