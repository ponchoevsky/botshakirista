import random
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


marx = open('manifiesto', 'r').read()
marx_words = marx.split()
marx_word = []

tweet = ""


while len(tweet) == 0:
	shakira_random_lines = random.choice(open("shakira").readlines())
	shakira_random_lines = shakira_random_lines[0:-1]
	shakira_words = shakira_random_lines.split()
	shakira_word = shakira_words[-1]

	if shakira_word in marx_words:
		pointer = marx_words.index(shakira_word)
		tweet += shakira_random_lines + " " + " ".join(marx_words[pointer+1:pointer+25])


tweet = tweet[0:136] + "..."

print (tweet)

try:
	api.update_status(status=tweet)
except tweepy.TweepError as e:
        print (e.reason)
