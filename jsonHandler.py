import json


def loadJSON(filename):
	with open(filename, 'r') as fileHandler:
		jsonData = json.load(fileHandler)
		return jsonData

def saveJSON(jsonData, fileName):
	with open(fileName, 'w') as fileHandler:
		json.dump(jsonData, fileHandler)
	print("JSON saved as {}.".format(fileName))


