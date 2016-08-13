

from jsonHandler import *
from sys import argv


def main():
	"""Take a file name as argv parameter and returns the cleaned data"""
	fileName = argv[1]
	tweets = loadJSON(fileName)

	#Unicite
	uniqueTweets = set(tweets)
	print(len(uniqueTweets))
	print("Excluded {} duplicate tweets".format(len(tweets)-len(uniqueTweets)))
	uniqueTweets = list(uniqueTweets)
	saveJSON(uniqueTweets, "uniqueTweets")

if __name__ == '__main__':
	main()
