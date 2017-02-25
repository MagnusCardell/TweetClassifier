import random
import csv

# opens .csv file and reads single tweets into arrays
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

# split tweets into training and test sets
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	i = 0
	while i < trainSize:
		trainSet.append(copy[i])
		copy.pop(i)
		i=i+1
	return [trainSet, copy]

def separateByClass(tweets):
	separated = {}
	for dataset in tweets:
		vector = ();
		for i in range(len(dataset)):
			vector = vector + tuple(dataset[i].split())
		#print(len(vector))
		#print(vector)

		for i in range(len(vector)):
			#vector = dataset[i].split()
			if (vector[i] not in separated):
				separated[vector[i]] = 0
			separated[vector[i]]= separated[vector[i]]+ 1
	return separated

def posfraction(dataset, good):
	vector = dataset.split()
	return 88
# main function
if __name__ == '__main__':

	test = ['1','2','3','4','3','2','3','1','2']
	news = loadCsv("news.csv")
	politics = loadCsv("politics.csv")
	celebs = loadCsv("celebs.csv")
	sports = loadCsv("sports.csv")
	#manymore = loadCsv("tweets.csv")

	splitRatio = 0.5
	train, copy = splitDataset(news, splitRatio)
	#train = train.replace('the', '')
	#print(train)

	#separate = separateByClass(train)
	good= ['good', 'happy','nice','super','delightful', 'like']

	goodfraction = posfraction(train, good)
	print(goodfraction)

	#print(max(separate, key=separate.get))
	


	# i = 0
	# while i < (len(news)):
	# 	print(news[i])
	# 	i=i+1