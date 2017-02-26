#!/usr/bin/env python
# encoding: utf-8
import csv

# opens text file of words and save them into arrays
def loadwords(filename):
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

def loadfile(filename):
	with open(filename) as f:
		tweets= []
		for lines in f.readlines():
			tweet = formattweet(lines.split())
			tweets.append(tweet)
		return tweets

#remove unwanted words and formatting
def formattweet(dataset):
	datalist = [w.strip(".:,-'()!?´").replace('"','').lower()  for s in dataset for w in s.split()]
	remove = ['what','who','is','a','as','at','is','he', 'i','for',
		'then','they','that','this','one','two','three','four','five','six',
		'seven','eight','nine','ten','to','be','want',"its's",
		'so','the','before','after',"it's","he's",'her','in'
		'in','my','your','did','them','it','how','1','2','3','4',
		'5','6','7','8','9','0','am','me',"i'll",'on','in','if'
		'we','of','with','will','get','we','are',"we'd","isn't",
		'whilst','than',"they're",'and',"they're",'were''its',
		'if','was',"won't","where's",'an',"isn't"]
	form  = [word for word in datalist if word.lower() not in remove]
	return form

# split tweets into training and test sets by ratio given my splitratio
def splitDataset(dataset, splitratio):
	trainsize = int(len(dataset) * splitratio)

	training = []
	testing = dataset
	i=0
	for i in range(trainsize):
		training.append(dataset[i])
	for n in range(i+1):
		testing.pop(0)
	return training, testing

def separateByClass(tweets, baglist):
	summary=0
	num=0
	wordlist = baglist.split(',')
	for dataset in tweets:
		vector = ();
		for i in range(len(dataset)):
			vector = vector + tuple(dataset[i].split())
		for i in range(len(vector)):
			if (vector[i].lower() in wordlist):
				summary +=1
			num+=1
	return summary,num


if __name__ == '__main__':
	topics = ['news','politics','celebs','sports']
	testlist = []
	for topic in topics:
		tweets = loadfile(topic+".txt")
		training, test = splitDataset(tweets, 0.8s)
		polybag,newsbag,celebbag,sportbag = loadwords('bag.txt')
		politicfreq,num = separateByClass(training, polybag)
		newsfreq,num = separateByClass(training, newsbag)
		celebfreq,num = separateByClass(training, celebbag)
		sportsfreq,num = separateByClass(training, sportbag)
		totalyes = politicfreq+newsfreq+celebfreq+sportsfreq
		print "Prior Probabilities: P(yes)= ",totalyes,'/',num,"P(no)= ",num-totalyes,'/',num
		print topic,"\t Yes\tNo"
		print polybag[1],"\t",politicfreq,'/',totalyes,"\t", totalyes-politicfreq,'/',totalyes
		print newsbag[1],"\t",newsfreq,'/',totalyes,"\t", totalyes-newsfreq,'/',totalyes
		print celebbag[1],"\t",celebfreq,'/',totalyes,"\t", totalyes-celebfreq,'/',totalyes
		print sportbag[1],"\t",sportsfreq,'/',totalyes,"\t", totalyes-sportsfreq,'/',totalyes

	#for tweet in test:
	#	print(tweet)