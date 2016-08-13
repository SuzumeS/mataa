
from jsonHandler import *
from sys import argv
import re

def main():
	allHashtags = []
	fileName = argv[1]
	with open(fileName,'r') as data:
		tweets = json.load(data)
	hashtagRegex = r'#\w+[?.!]?'
	for tweet in tweets:
		matches = re.findall(hashtagRegex,tweet)
		if matches:
			for match in matches:
				allHashtags.append(str(match))

	print(len(allHashtags))
	print(len(set(allHashtags)))
	saveJSON(allHashtags, "allHashtags")

if __name__ == '__main__':
	main()
