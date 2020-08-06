import compute_probability
import kWindowProb
import time

wordLength = 11
seqLength = 40
wordSetSize = 40

t0 = time.time()

#########################################################################################################
#READ SEQUENCE
probscores = []
filename = 'SeqSet/sequence'+str(0)+'.txt'
#f = open('sequenceStructure.txt','r')
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
#########################################################################################################
#Probabilty Calcualation
probability = compute_probability.compute_probability()
#########################################################################################################
#DP Table 
words = []
window = kWindowProb.kWindowProb(probscores)

for i in range(seqLength-wordLength):
	words.append(window.BuildSet(50,i,11))


wordSet = []
for i in range(wordSetSize):
	bestScore = 0
	bestWord = ''
	index = -1

	for j in range(len(words)):
		if words[j][0][2] > bestScore:
			index = words[j][0][0]
			bestWord = words[j][0][1]
			bestScore = words[j][0][2]

	del words[index][0]
	wordSet.append([index,bestWord])

t1 = time.time()
total = t1-t0

print wordSet
print len(wordSet)
print probability.scan_words(probscores, wordSet)
print total
