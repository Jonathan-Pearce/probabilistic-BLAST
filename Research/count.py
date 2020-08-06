import compute_probability
import sys
import time
#import sys

#NOTES
######
#Consider 1 loop to get all words and then we don't have to generate words n times (memory vs speed)

def getProb(probScores,word,index):
	#print 'here'
	bpScore = {'A':0, 'C':1, 'G':2, 'T':3}
	score = 1.0
	for i in range(len(word)):
		score *= probScores[index+i][bpScore[word[i:i+1]]]
	return score

def to_base_4(n):
    s = ""
    while n:
        s = str(n % 4) + s
        n /= 4
    return s


bps = ['A','C','G','T']
wordLength = 10
probScores = []
wordSetSize = 2
#########################################################################################################
#READ SEQUENCE
probscores = []
filename = 'SeqSet/sequence'+str(0)+'.txt'
#f = open('sequenceStructure.txt','r')
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
#print probscores
#Probabilty Calcualation
probability = compute_probability.compute_probability()
#########################################################################################################
#wordSet = []
count = 0
#print 'here'
#print len(probscores)
#get each word at each position
t0 = time.time()

for i in range(4**wordLength):
	word = ''
	#convert to string
	base4 = to_base_4(i)

	#add extra zeroes if necessary
	string = ''
	if len(base4) < wordLength:
		diff = wordLength - len(base4)
		string = '0'*diff

	base4 = string + base4 	

	for k in range(wordLength):
		#print base4
		word += bps[int(base4[k:k+1])]

	for j in range(len(probscores)-wordLength):
		#get the probability of the word at position j
		wordProb = getProb(probscores,word,j)
		#can adjust lower bound if program is too slow, if > 0 then it is an approximation algorithm

		#1e-4 = 0.0001, error at most 1%
		#1e-3 = 0.001, error at most 10% (100 words)

		lowerBound = 0.01
		if wordProb > lowerBound:
			#wordSet.append([j,word,wordProb])
			count += 1


print count



