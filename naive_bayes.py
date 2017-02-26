#!/usr/bin/python
# -*- coding: utf-8 -*-
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
		dataset[i] = formattweet(dataset[i])
	return dataset

#remove unwanted words and formatting
def formattweet(dataset):
	datalist = [w.strip(".:,-'!?´") for s in dataset for w in s.split()]
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
	result = [" ".join(form)]
	return result

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
	return training, testing

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
		
		print"Prior Probability Table: \t P(Yes)",totalyes,"/",totallength
		print("News: \t Yes \t No" )
		print "\nNews \t",newsfreq,"\t tota"
