import random
import string
import time

from auth import *


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


# function that posts a status to twitter using the update_status from twitter api
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

# delete a twitter post
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

# whoami(usertest)

# create_random_id(self)
