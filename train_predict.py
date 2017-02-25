import random
import csv

# opens .csv file and reads many tweets into arrays of individual tweets
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

# split tweets into training and test sets by ratio given my splitratio
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	i = 0
	while i < trainSize:
		trainSet.append(copy[i])
		copy.pop(i)
		i+=1
	return [trainSet, copy]

# checks relevant wordfrequency in tweets
def separateByClass(tweets, wordlist):
	summary=0
	separated = {}
	for dataset in tweets:
		vector = ();
		for i in range(len(dataset)):
			vector = vector + tuple(dataset[i].split())
		#print(len(vector))
		#print(vector)

		for i in range(len(vector)):
			#vector = dataset[i].split()
			if (vector[i] in wordlist):
				summary +=1
				print(vector[i])
	return summary


# main function
if __name__ == '__main__':
	topics = ['news','politics','celebs','sports']
	for topic in topics:
		tweets = loadCsv(topic+".csv")
		splitRatio = 0.5
		train, copy = splitDataset(tweets, splitRatio)
		#inport all related adjectives and do comparison.
		lines = csv.reader(open("related_"+topic+".csv", "rb"))
		for a in lines:
			wordlist = a
		frequency = separateByClass(train, wordlist)
		print(topic)
		print(frequency)


	# print(separateByClass(politics, political))
	# print(separateByClass(sports, political))
	# print(separateByClass(celebs, political))


#RETIREMENT functions

# politics = loadCsv("politics.csv")
# 	celebs = loadCsv("celebs.csv")
# 	sports = loadCsv("sports.csv")

#	test = ['1','2','3','4','3','2','3','1','2']
	#manymore = loadCsv("tweets.csv")

	#print(max(separate, key=separate.get))
	


	# i = 0
	# while i < (len(news)):
	# 	print(news[i])
	# 	i=i+1