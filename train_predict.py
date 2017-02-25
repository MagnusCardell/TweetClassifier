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

def separateByClass(tweets, emotion):
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
			if (vector[i] in emotion):
				summary +=1
	return summary


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
	good = ['good', 'happy','nice','super','delightful', 'like', 'inspiring']
	political = ['many', 'local', 'professional', 'most', 'american', 
	'few', 'prominent', 'conservative', 'british', 'democratic', 
	'corrupt', 'southern', 'liberal', 'republican', 'practical', 'french', 
	'national', 'indian', 'civilian','white', 'black', 'english', 
	'ambitious', 'individual', 'influential', 'powerful', 'senior', 
	'western', 'wing', 'northern', 'german', 'irish', 'successful', 
	'unscrupulous', 'japanese', 'african', 'male', 'european','active', 
	'radical', 'female', 'whig', 'moderate', 'contemporary', 'canadian', 
	'bourgeois', 'top', 'federal', 'provincial', 'minded', 'astute', 
	'crooked', 'muslim', 'russian', 'mexican', 'italian', 'experienced', 
	'seeking', 'progressive', 'petty', 'rival', 'west', 'younger', 'time',
	'responsible', 'eminent', 'israeli', 'colonial', 'able', 'known', 
	'communist', 'socialist', 'class', 'regional', 'mainstream', 
	#shrewd, greek, australian 
	
	#numGood = separateByClass(train, good)
	#print(numGood)
	print(separateByClass(news, political))
	print(separateByClass(politics, political))
	print(separateByClass(sports, political))
	print(separateByClass(celebs, political))

	#print(max(separate, key=separate.get))
	


	# i = 0
	# while i < (len(news)):
	# 	print(news[i])
	# 	i=i+1