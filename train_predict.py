import csv

# opens .csv file and reads single tweets into arrays
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

# 
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) < trainSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	return [trainSet, copy]

# main function
if __name__ == '__main__':

	news = loadCsv("news.csv")
	politics = loadCsv("politics.csv")
	celebs = loadCsv("celebs.csv")
	sports = loadCsv("sports.csv")






	i = 0
	while i < (len(news)):
		print(news[i])
		i=i+1