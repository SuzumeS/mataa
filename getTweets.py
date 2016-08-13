from sys import argv
import time
import json

from api import getAPI

REQUEST_DELAY = 5
MAX_REQUESTS = 150

def main():
	try:
		arg = argv[1]
		api = getAPI()
		tweetResults = []
		counter = 0
		tweetIndex = api.user_timeline(screen_name=arg, count=1)[0].id
		time.sleep(REQUEST_DELAY)
		for request in range(MAX_REQUESTS):
			print("----------Starting for loop----------")

			tweets = api.user_timeline(screen_name=arg, include_retweets=False, max_id = tweetIndex)
			for tweet in tweets:
				tweetResults.append(tweet.text)
				tweetIndex = tweet.id
				counter += 1
			print("----------Got {} tweets so far. Entering Delay".format(counter))
			time.sleep(REQUEST_DELAY)

		#print(tweetResults)
		print("EOS : Managed to get {} tweets.".format(len(tweetResults)))
	except IndexError:
		print("Program Missing Arg. Twitter Handle")
	except Exception as e:
		print("Program Failure. Error : {}".format(e))
	finally:
		with open('exports/{}Tweets'.format(arg),'w') as saveFile:
			json.dump(tweetResults, saveFile)

if __name__ == '__main__':
	main()

