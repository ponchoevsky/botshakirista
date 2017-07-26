import random
import tweepy

consumer_key = 'Idff72RvHeEJHxqArJgfbCgxG'
consumer_secret = 'SpQKAtugXF4D58VF0cXixLx4gBUjVUvJH77gigkAbWfKI1HIdt'
access_token = '889932917744349184-k1XnyPOy9jJ9XKGgCHknixBV3u2aJJ7'
access_token_secret = 'LJECETbdYuxI4fw3bYtz9BS5RrBCCpFjYh8j3jBMv1ZBX'

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

print tweet
try:
	api.update_status(status=tweet)
except tweepy.TweepError as e:
        print(e.reason)