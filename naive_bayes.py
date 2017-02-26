import csv

# opens .csv file and reads many tweets into arrays of individual tweets
def loadfile(filename):
	with open(filename) as f:
		for lines in f.readlines():
			bag = [lines.split()]
			words = [l.split(',')[0] for l in bag[0]]
			if words[0] == '#politics':
				polbag = lines
			elif words[0] == '#news':
				newsbag = lines
			elif words[0] == '#sports':
				sportbag = lines
			elif words[0] == '#celebrity':
				celebbag = lines
			else:
				print('Error: unrecognized category')

	return polbag,newsbag,celebbag,sportbag

def loadcsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset

# split tweets into training and test sets by ratio given my splitratio
def splitDataset(dataset, splitRatio):
	trainSize = int(len(dataset) * splitRatio)
	training = []
	testing = list(dataset)
	i = 0
	while i < trainSize:
		training.append(testing[i])
		testing.pop(i)
		i+=1
	return [training, testing]

# checks relevant wordfrequency in tweets
def separateByClass(tweets, baglist):
	summary=0
	wordlist = baglist.split(',')
	separated = {}
	for dataset in tweets:
		vector = ();
		for i in range(len(dataset)):
			vector = vector + tuple(dataset[i].split())
		for i in range(len(vector)):
			if (vector[i].lower() in wordlist):
				summary +=1
	return summary


# main function
if __name__ == '__main__':
	topics = ['news','politics','celebs','sports']
	polybag,newsbag,celebbag,sportbag = loadfile('bag.txt')
	for topic in topics:
		tweets = loadcsv(topic+".csv")
		splitRatio = 0.5
		training, testing = splitDataset(tweets, splitRatio)
		#inport all related adjectives and do comparison.
		politicfreq = separateByClass(training, polybag)
		newsfreq = separateByClass(training, newsbag)
		celebbag = separateByClass(training, celebbag)
		sportsbag = separateByClass(training, sportbag)

