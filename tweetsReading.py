# -*-coding:utf-8 -*
import json

with open('exports/@yohan_leTweets','r') as data:
	tweets = json.load(data)
print(len(tweets))
# a = tweets[0]
# print(a)
for i in range(5):
	print(tweets[i].encode('utf-8'))


