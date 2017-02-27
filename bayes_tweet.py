#!/usr/bin/env python
# encoding: utf-8
import csv

# opens text file of words and save them into arrays
def loadwords(filename):
	with open(filename) as f:
		for lines in f.readlines():
			bag = lines.split()
			words = [l.split(',')[0] for l in bag]
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
	polybag,newsbag,celebbag,sportbag= loadwords('bag.txt')
	testlist = []
	sumset=0
	sumsetyes = 0
	totalp =0
	totaln =0
	totalc =0
	totals =0
	for topic in topics:
		tweets = loadfile(topic+".txt")
		training, test = splitDataset(tweets, 0.8)
		testlist.append(test)
		politicfreq,num = separateByClass(training, polybag)
		newsfreq,num = separateByClass(training, newsbag)
		celebfreq,num = separateByClass(training, celebbag)
		sportsfreq,num = separateByClass(training, sportbag)
		totalyes = politicfreq+newsfreq+celebfreq+sportsfreq
		totalp+=politicfreq
		totaln+=newsfreq
		totalc+=celebfreq
		totals+=sportsfreq
		sumsetyes +=totalyes
		sumset += num
		print("Prior Probabilities: P(yes)= ",totalyes,'/',num,"P(no)= ",num-totalyes,'/',num)
		print(topic,"\t Yes\t\tNo")
		print(polybag[1],"\t",politicfreq,'/',totalyes,"\t", totalyes-politicfreq,'/',totalyes)
		print(newsbag[1],"\t",newsfreq,'/',totalyes,"\t", totalyes-newsfreq,'/',totalyes)
		print(celebbag[1],"\t",celebfreq,'/',totalyes,"\t", totalyes-celebfreq,'/',totalyes)
		print(sportbag[1],"\t",sportsfreq,'/',totalyes,"\t", totalyes-sportsfreq,'/',totalyes)

	print(sumsetyes,sumset)
	probyes = sumsetyes/sumset
	print("Total Prior: P(yes)= ",sumsetyes,'/',sumset,"P(no)= ",sumset-sumsetyes,'/',sumset)
	print(topic,"\t Yes\t\tNo")
	print(polybag[1],"\t",totalp,'/',sumsetyes,"\t", sumsetyes-totalp,'/',sumsetyes)
	print(newsbag[1],"\t",totaln,'/',sumsetyes,"\t", sumsetyes-totaln,'/',sumsetyes)
	print(celebbag[1],"\t",totalc,'/',sumsetyes,"\t", sumsetyes-totalc,'/',sumsetyes)
	print(sportbag[1],"\t",totals,'/',sumsetyes,"\t", sumsetyes-totals,'/',sumsetyes)
	priorp=totalp
	priorn=totaln 
	priorc=totalc
	priors=totals
	priorsumset=sumset
	prioryes=sumsetyes
	i=1
	newsumsetyes=sumsetyes
	newsumset=sumset
	for tweets in testlist:
		for tweet in tweets:
			print("Testing tweet ",i)
			i+=1
			politicfreq1,num= separateByClass([tweet], polybag)
			newsfreq1,num= separateByClass([tweet], newsbag)
			celebfreq1,num= separateByClass([tweet], celebbag)
			sportsfreq1,num= separateByClass([tweet], sportbag)

			totalp+=politicfreq1
			totaln+=newsfreq1
			totalc+=celebfreq1
			totals+=sportsfreq1
			newsumsetyes+=politicfreq1+newsfreq1+celebfreq1+sportsfreq1
			newsumset+=num
			newprobyes=newsumsetyes/newsumset

			politprob = round((totalp/newsumsetyes*newprobyes),4)
			newsprob = round((totaln/newsumsetyes*newprobyes),4)
			celebprob = round((totalc/newsumsetyes*newprobyes),4)
			sportsprob = round((totals/newsumsetyes*newprobyes),4)


			print("P(political)= ",politprob*100,'%')
			print("P(news)= ",newsprob*100,'%')
			print("P(celebrity)= ",celebprob*100,'%')
			print("P(sports)= ",sportsprob*100,'%\n')

	print("Post test P(yes)= ",newsumsetyes,'/',newsumset,"P(no)= ",newsumset-newsumsetyes,'/',newsumset)
	print(topic,"\t Yes\t\tNo")
	print(polybag[1],"\t",totalp,'/',newsumsetyes,"\t", newsumsetyes-totalp,'/',newsumsetyes)
	print(newsbag[1],"\t",totaln,'/',newsumsetyes,"\t", newsumsetyes-totaln,'/',newsumsetyes)
	print(celebbag[1],"\t",totalc,'/',newsumsetyes,"\t", newsumsetyes-totalc,'/',newsumsetyes)
	print(sportbag[1],"\t",totals,'/',newsumsetyes,"\t", newsumsetyes-totals,'/',newsumsetyes)

	print("\n")
	print("Comparing prior probability with prediction: ")
	print("\t\t Prior \t\t Post")
	print("P(political)\t", round(((priorp/prioryes)*(prioryes/priorsumset)),4),"\t",round((totalp/prioryes)*newprobyes,4))
	print("P(news) \t", round(((priorn/prioryes)*(prioryes/priorsumset)),4),"\t",round((totaln/prioryes)*newprobyes,4))
	print("P(celeb)\t", round(((priorc/prioryes)*(prioryes/priorsumset)),4),"\t",round((totalc/prioryes)*newprobyes,4))
	print("P(sports)\t", round(((priors/prioryes)*(prioryes/priorsumset)),4),"\t\t",round((totals/prioryes)*newprobyes,4))
