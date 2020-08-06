import compute_probability
import kWindowProb
import time
import BuildUp


t0 = time.time()

#########################################################################################################
#READ SEQUENCE
probscores = []
filename = 'SeqSet2/sequence'+str(1)+'.txt'
#f = open('sequenceStructure.txt','r')
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
#########################################################################################################
#Probabilty Calcualation
probability = compute_probability.compute_probability()
#Build Set
buildSet = BuildUp.buildUp() 
#########################################################################################################
seqLength = len(probscores)
wordSetSize = 40
wordLength = 11
#DP Table 
words = []
##################################
windows = []
windowScore = 1.0
for i in range(wordLength):
	windowScore *= max(probscores[i])
windows.append([windowScore,0])

for i in range(wordLength,seqLength):
	windowScore /= max(probscores[i-wordLength])
	windowScore *= max(probscores[i])
	windows.append([windowScore,i-wordLength+1])

#print windows
windows.sort(reverse=True)

print windows
sys.exit(0)

windowOrder = []
for i in windows:
	windowOrder.append(i[1])
print windowOrder


score,wordSet = buildSet.buildup(probscores,100,wordLength)

indexes = []
for i in range(seqLength):
	indexes.append([0,i])
for i in wordSet:
	indexes[i[1]][0] += 1
#print indexes
indexes.sort(reverse=True)
#print indexes


indexOrder = []
indexAmount = []
for i in indexes:
	if i[0] != 0:
		indexOrder.append(i[1])
		indexAmount.append(min(int(2*i[0]),100))



#print indexOrder
#sys.exit(0)
#print indexAmount
#t0 = time.time()
###################################
window = kWindowProb.kWindowProb(probscores)
#Table is n x size of indexOrder
dpTable = [[[] for i in range(wordSetSize+1)] for j in range(len(indexOrder))]
#

t0 = time.time()

for i in range(len(indexOrder)):
	print i
	words.append(window.BuildSet(indexAmount[i],indexOrder[i],11))

t1 = time.time()
total = t1-t0
print 'Time to generate words',total

#intialize first column
#works because top index is always filled to full size
dpTable[0][0] = []
for i in range(1,wordSetSize+1):
	dpTable[0][i] = words[0][0:i]
	#print probability.scan_words(profile, dpTable[0][i])



for i in range(1,seqLength-wordLength+1):
#for i in range(1,numIndexes):
	#get top 100 words at position i
	print i

	for j in range(1,wordSetSize+1):
		maxProb = 0
		maxIndex = -1
		maxSet = []

		limit = j+1
		if j+1 > indexAmount[i]:
			limit = indexAmount[i]
		#print limit
		for k in range(limit):
			#take k from previous column
			#take j-k from current position
			testSet = dpTable[i-1][j-k] + words[i][0:k]
			#print len(testSet)
			#Evaluate set of size j
			testProb = probability.scan_words(probscores,testSet)

			#Check if best option
			if testProb > maxProb:
				maxProb = testProb
				maxIndex = k
				maxSet = testSet


		dpTable[i][j] = maxSet
	print probability.scan_words(probscores, dpTable[i][len(dpTable[0])-1])

	t1 = time.time()
	total = t1-t0
	print total



finalSet = dpTable[numIndexes-1][len(dpTable[0])-1]
print finalSet
print len(finalSet)
print probability.scan_words(probscores, finalSet)

t1 = time.time()
total = t1-t0
print 'Time to generate words'
print total
