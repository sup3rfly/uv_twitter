import tweepy

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
