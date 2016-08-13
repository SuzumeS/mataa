import json
from jsonHandler import *
import re
from random import randint

class TweetGenerator:
	def __init__(self, sourceFile=None):
		self.rawTweets = []
		self.initialStates = []
		self.markovDictionary = {}
		if sourceFile:
			self.loadTweets(sourceFile)
			self.processTweets()
			self.saveTweetGen(sourceFile + "Markov")

	def loadTweets(self, fileName):
		"""Loads in saved Tweet JSON"""
		self.rawTweets = loadJSON(fileName)
	def processTweets(self):
		"""After loading, builds the Data Strcuture for generation"""
		endingCharacters = ["!","?","."]
		priorWord = None

		for tweet in self.rawTweets:
			for word in tweet.split() + [None]:
				if priorWord is None and not word is None:
					self.initialStates.append(word)
					priorWord = word
				elif word is None:
					self.updateDictionary(priorWord, "END_OF_SENTENCE")
					priorWord = None
				elif word[-1] in endingCharacters:
					self.updateDictionary(priorWord, word)
					self.updateDictionary(word, "END_OF_SENTENCE")
					priorWord = None
				else:
					self.updateDictionary(priorWord, word)
					priorWord = word

	def updateDictionary(self, priorWord, word):
		if priorWord in self.markovDictionary:
			self.markovDictionary[priorWord].append(word)
		else:
			self.markovDictionary.update({priorWord:[word]})			



	def loadTweetGen(self, fileName):
		"""This function allow us to reload an existing data strcuture, to avoid creating it each time"""
		allGenData = loadJSON(fileName)
		self.initialStates = allGenData['initialStates']
		self.markovDictionary = allGenData['markovDictionary']
		self.rawTweets = allGenData['rawTweets']
		print("{} Loaded".format(fileName))
	def saveTweetGen(self, fileName):
		"""Saves the data structure (so we can load it afterwards)"""
		allGenData = {'initialStates':self.initialStates,
		'markovDictionary':self.markovDictionary,
		'rawTweets':self.rawTweets}
		saveJSON(allGenData, fileName)
	def generateTweet(self):
		"""this return a new randomly generated tweet"""
		word = self.initialStates[randint(0, len(self.initialStates)-1)]
		tweet = [word]
		while word != "END_OF_SENTENCE":
			randomIndex = randint(0, len(self.markovDictionary[word])-1)
			word = self.markovDictionary[word][randomIndex]
			if not word == "END_OF_SENTENCE":
				tweet.append(word)
		return " ".join(tweet)