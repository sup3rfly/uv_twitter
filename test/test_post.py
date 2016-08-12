import unittest
import tweepy
from IPython import embed

from basepost import post_status, create_random_id, destroy, whoami
from cursor import search_status
# from timeout import tmr


class TestPostMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.location = [26.0963, 44.4396] #bucharest location
        cls.usertest = '@test_uv'


    # Test if a simple message can be posted
    def test_post(self):
        self.totweet = unicode("test_post_test "+ create_random_id(self))
        tweet = post_status(self.totweet)
        self.assertEqual(self.totweet, tweet.text, "Didn't post!")

    # Test if a message exceeds 140 can not be posted
    def test_post_over140(self):
        self.totweet = unicode("123456789012" * 11 + create_random_id(self))
        tweet = post_status(self.totweet)
        self.assertRegexpMatches(tweet, "Status is over 140 characters","Status is over 140 characters.")

    # Test if a blank message can not be tested
    def test_post_0(self):
        self.totweet = u''
        tweet = post_status(self.totweet)
        print "test_post_0 resp: ", tweet
        self.assertRegexpMatches(tweet, "Missing required parameter: status.","Missing required parameter: status.")

    #TODO: check if twitter supports posting with special characters.
    def test_post_special_characters(self):
        self.assertTrue(True,True)

    # Test in_reply_to_status_id
    # TODO: Note:: This parameter will be ignored unless the author of the tweet this parameter references
    # is mentioned within the status text. Therefore, you must include @username, where username
    # is the author of the referenced tweet, within the update.
    def test_post_reply(self):
        random_id = create_random_id(self)

        self.totweet = unicode("Post to be replied to "+ random_id)
        tweet = post_status(self.totweet)
        self.tweet_reply = unicode("Reply to" + self.usertest + " " + random_id)

        tweet_reply = post_status(self.tweet_reply, in_reply_to_status_id=tweet.id)

        self.assertEqual(tweet.id, tweet_reply.in_reply_to_status_id, "Didn't reply to the correct status id!")

    # #TODO: This still needs some work to be done
    # # Test for a non existent in_reply_to_status_id
    # def test_post_reply_non_existent(self):
    #     random_id = create_random_id(self)
    #
    #     self.totweet = unicode("Post to be replied to "+ random_id)
    #     tweet = post_status(self.totweet)
    #     destroyed = destroy(tweet.id)
    #     self.assertEqual(destroyed,tweet.id)
    #
    #     print "aici2"
    #     self.tweet_reply = unicode("Reply to "+ random_id)
    #     tweet_reply = post_status(self.tweet_reply, in_reply_to_status_id=tweet.id)
    #
    #     print "Tweet reply type", type(tweet_reply)
    #     print "tweet_reply", tweet_reply.text
    #     # self.assertEqual(tweet.id, tweet_reply.in_reply_to_status_id, "Didn't reply to the correct status id!")
    #     self.assertRegexpMatches(tweet_reply, "Status is over 140 characters","Status is over 140 characters.")
    #

    # Test lat and long parameters in post
    def test_post_location(self):
        # location = [26.0963, 44.4396] #bucharest location
        self.totweet = unicode("test_post_test "+ create_random_id(self))
        tweet = post_status(self.totweet, lat=self.location[1], long=self.location[0])

        self.assertListEqual(self.location, tweet.coordinates['coordinates'], "Didn't post with the correct coordinates!")


    # Test in_reply_to_status_id and location
    def test_post_reply_location(self):

        self.location = TestPostMethods.location
        random_id = create_random_id(self)


        self.totweet = unicode("Post to be replied to "+ random_id)
        self.tweet_reply = unicode("Reply to" + self.usertest + " " + random_id)

        tweet = post_status(self.totweet)
        tweet_reply = post_status(self.tweet_reply, in_reply_to_status_id=tweet.id, lat=self.location[1], long=self.location[0])

        l1 = TestPostMethods.location
        l1.append(tweet.id)

        l2 = tweet_reply.coordinates['coordinates']
        l2.append(tweet_reply.in_reply_to_status_id)

        #compare the two lists with coordinates
        self.assertListEqual(l1, l2, "Location or in_reply_to_status_id are not correct")

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPostMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)