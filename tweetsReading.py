# -*-coding:utf-8 -*
import json
from sys import argv



def main():
	fileName = argv[1]
	tweetNumber = argv[2]
	print fileName
	print tweetNumber
	with open(fileName,'r') as data:
		tweets = json.load(data)
	print(len(tweets))
	# a = tweets[0]
	# print(a)
	for i in range(int(argv[2])):
		print(tweets[i].encode('utf-8'))
		print(tweets[i+20].encode('utf-8'))
		print(tweets[i+40].encode('utf-8'))



if __name__ == '__main__':
	main()
