import unittest
import time
from datetime import datetime

import random
from basepost import post_status, update_language, create_random_id
from cursor import search_status
from timeout import tmr

class TestGetMethods(unittest.TestCase):

    # def setUp(self):
    #     print "Running setUpClass"
    #     # print "Current time: ", datetime.datetime.now().time()
    #     self.query = unicode(self.create_random_id())
    #     post_status("Tweet " + self.query)

    # Test if tweets can be retrieved by searching a string
    def test_search_hashtag(self):
        # print "A INTRAAAAT"
        found = False
        t = tmr()
    
        # self.query = unicode(create_random_id(self))
        self.query = create_random_id(self)
        self.query = self.query.encode('utf8')
        post_status("Tweet " + self.query)
    
        while t.timer():
            for status in search_status(self.query):
                if self.query in status.text:
                    found = True
                    break
            if found:
                break
        self.assertTrue(found,"Not found")
    
    
    # #TODO: get past the twitter api call limitations that can make the test pass since the search won't return anything
    # #TODO: there might be the same issue that the test fails since status.lang returns en instead of fr
    # # Test if tweets can be retrieved  in a specific language
    def test_search_locale(self):
        lang_en = "en"  #default user language
        lang_fr = "fr"
        found = False
        t = tmr()
        # print "\n1. language to update:", lang_fr
        #update user to use French language
        update_language(lang_fr)
    
        #post in new language
        self.query = "Test search locale " + unicode(create_random_id(self))
        tweet = post_status(self.query)
    
        #search in other language than it was previous posted, e.g. in english
        while t.timer():
            for status in search_status(self.query, locale=lang_en):
                # print "st:", status.text
                # print "sq:",self.query
                # print "\nStatus Lang: ", status.lang
                # print "\nStatus id: ", status.id
                # print "\nStatus text: ", status.text
                # print "\nQuery: ", self.query
                # print "status type", type(status)
    
                # if self.query in status.text:
                if self.query in status.text and status.lang==lang_en:
                    # print "here", status.lang
                    # print "status text", status.text
                    found = True
                    break
            if found:
                break
    
        update_language(lang_en)
        # found needs to be False
        # print found
        self.assertFalse(found,"Locale search failed, tweed supposed not to be found!")
    
    
    # #TODO: need some way to retreive the correct status language.
    def test_search_hashtag_lang_en(self):
        # query = "#genderbarriers"
        lang_en = "en"
        lang_fr = "fr"
        found = False
        t = tmr()
        # print "1. language to update:", lang_fr
    
        update_language(lang_fr)
    
        self.query = "Tweet " + unicode(create_random_id(self))
        tweet = post_status(self.query)
    
        # print "2. language of the tweet: ", tweet.lang
    
        while t.timer():
            for status in search_status(self.query):
                # print "st:", status.text
                # print "sq:",self.query
                # print "\nStatus Lang: ", status.lang
                # print "\nStatus id: ", status.id
                # print "\nStatus text: ", status.text
                # print "\nQuery: ", self.query
                # print "status type", type(status)
    
                if self.query in status.text and lang_fr==status.lang:
                # if self.query in status.text:
                #     print "here"
                    found = True
                    break
            if found:
                # "print not here"
                break
        # update_language(lang_en)
        # print "language back: ", tweet.lang
    
        # print "THE FOUND". found
        self.assertTrue(found,"Not Found")
    
    
    #TODO: retest this
    #NOTE: Count = formerly rpp in old Search API
    def test_search_count(self):
        #need a common string to search for
        random_id = create_random_id(self)
        # print type(random_id)
    
        found = False
        tweet = []
        tweets_no = random.randrange(1, 6)
        # print "\ntweets no: ", tweets_no
        t = tmr()
    
        #create a random no of tweets to "count" for
        for i in range(tweets_no):
            # print "i", i
            tweet.append(post_status(unicode("Test count "+ random_id + " " + str(time.time()))))
        #searching for the common string and counting the no of tweets
        while t.timer():
            l = len(search_status(random_id, count = tweets_no))
            if l:
            # if len(search_status(random_id, count = tweets_no)):
                found = True
                break
            if found:
                break
    
        self.assertTrue(found,"Not found")


    # TODO: test if the number of tweets to return per page can work with 100 which is the maximum according to the API
    def test_search_count_100(self):
        pass

    # TODO:  test if the number of tweets to return per page don't work with 100 which is the maximum according to the API
    def test_search_count_over100(self):
        pass

    # TODO: test if can return 0 tweets when searching
    # TODO: consult the api works with 0 set as count
    def test_search_count_0(self):
        pass

    #TODO: for some reason it doesn't retreive any tweets
    #est search until some date.
    def test_search_until(self):
        t = tmr()
        random_id = create_random_id(self)
        until = time.strftime("%Y-%m-%d")

        current_date = datetime.now()

        post_status(unicode("Test search until "+ random_id + " " + str(until)))
        found = False
        #searching for  tweets until the current date
        while t.timer():
            #TODO: find a way to make sure we can search for tweets before the current date. Using string "Test" for now
            tweet = search_status("Test", until=until, items=1)

            if  tweet:
                for status in tweet:
                    # print "created", status.created_at
                    #if the status creation date is bigger or equal than the current date or "until" then the test should fail

                    # print "\nfound ", status.text
                    # print "status date ", datetime.strptime(str(status.created_at), "%Y-%m-%d %H:%M:%S")
                    # print "until date", datetime.strptime(until,"%Y-%m-%d")
                    if datetime.strptime(str(status.created_at), "%Y-%m-%d %H:%M:%S") < datetime.strptime(until,"%Y-%m-%d"):
                        # print "entered here"
                        found = True
                        break
            else:
                # if no tweets returned, then fail
                self.assertFalse(False,"No tweets returned")
            if found:
                # "entered here as well"
                break
        # Fail if found tweets with current search date
        self.assertTrue(found,"Couldn't find any tweets")

# suite = unittest.TestLoader().loadTestsFromTestCase(TestGetMethods)
# unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGetMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
