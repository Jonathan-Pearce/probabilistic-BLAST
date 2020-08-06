import math
import random

seqLength = 10
wordLength = 4
numWords = 10

seq = []

#generate sequence
for i in range(seqLength):

	total = 1
	scores = []
	for j in range(3):
		rand = random.random()*total 
		scores.append(rand)
		total -= rand
	scores.append(total)
	seq.append(scores)

print seq

#compute optimal window rankings for each eligible index
#only need strings, don't need scores


#could just try window of wordLength + 1????

#Try all solutions and find best one
#see if it follows the rule

#use rankings and find best solution
#Then from each position with a word: remove word and a add a new off order word from any other column or itself to see if it works better
