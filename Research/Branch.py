import compute_probability
import sys
import time
import pickle
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

def probSumRemaining(wordSet,index,numWords):
	probSum = 0
	for i in range(numWords):
		probSum += wordSet[index+i][2]

	return probSum


with open('branchData11.txt', 'rb') as f:
    wordSet = pickle.load(f)

print len(wordSet)
#print wordSet[0:10]
#sys.exit(0)
 
bps = ['A','C','G','T']
probScores = []


wordLength = 10
globalWordSetSize = 50
localWordSetSize = 6
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

#toggle word set, currently reading from file
if False:
	wordSet = []
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

			lowerBound = 1e-4
			if wordProb > lowerBound:
				wordSet.append([j,word,wordProb])


	#sort by wordProb
	wordSet.sort(reverse = True, key = lambda x: x[2])
	#print wordSet
	#add index to each element
	for i in range(len(wordSet)):
		#print 'here'
		wordSet[i].append(i)
		#index for keeping track of next word to add to solution
		#will have to reset whenever word is popped
		wordSet[i].append(i+1)

	t1 = time.time()
	total = t1-t0
	print 'processing time: ',total
	print len(wordSet)
	with open('branchData11.txt', 'wb') as f:
	    pickle.dump(wordSet, f)

	sys.exit(0)


#print wordSet[0:10]

print len(wordSet)
wordSet = wordSet[0:500]
print len(wordSet)


#sys.exit(0)
t_0 = time.time()

fullSolution = []

while(len(fullSolution) < globalWordSetSize):
	t0 = time.time()

	stackSize = min(globalWordSetSize-len(fullSolution),localWordSetSize)

	#################################################################################
	#Branch and Bound (via Stack)
	stack = []
	#final results
	bestScore = 0 #obtained from buildUp
	bestSet = None
	levelScore = []
	#if set is empty ever we need to know which word to add
	firstWordIndex = 0
	#The stack will hold the current solution (partial or complete)
	#add top word to stack
	#stack.append(wordSet[0])
	#levelScore.append(wordSet[0][2])

	#CALL TO GET PROB
	#testProb = probability.scan_words(probscores,stack)
	solution = False
	#get the current score
	if len(fullSolution) == 0:
		fullSolutionScore = 0
	else:
		fullSolutionScore = probability.scan_words(probscores,fullSolution[:])

	while(not solution):

		#if we have a full set
		if(len(stack) == stackSize):
			#get score
			solnScore = probability.scan_words(probscores,stack[:]+fullSolution[:])
			#check if its best
			if solnScore > bestScore:
				#update best score
				bestScore = solnScore
				bestSet = list(stack)

			#bring it back to wordSetSize-1
			stack.pop()
			levelScore.pop()

		else:
			#if the stack is empty, figure out which word should be added next (we will slowly move down the list)
			if(len(stack) == 0):
				#copy without reference
				element = wordSet[firstWordIndex][:]
				#print element
				#here the stack is empty
				#If the probability of the word times wordSetsize is bigger than best continue
				if (fullSolutionScore + probSumRemaining(wordSet,firstWordIndex,stackSize)) > bestScore:
					#add to stack
					stack.append(wordSet[firstWordIndex][:])
					#add word prob to levelScore list
					#get prob of stack and solution
					levelScore.append(probability.scan_words(probscores,stack[:]+fullSolution[:]))
					#increase emptySet index count
					firstWordIndex += 1
				else:
					#WE ARE DONE
					print bestScore
					print bestSet
					#sys.exit(0)
					solution = True

			#stack is non empty		
			else:
				#print 'here'
				#latest element added to set
				lastElement = stack[len(stack)-1]
				#index of next element to add according to bottom element
				elementIndex = lastElement[4]
				#increase index
				lastElement[4] += 1
				#element we will add next
				#candidate word
				element = wordSet[elementIndex][:]

				#if the current stack of n words and (100-n)*prob(element)
				#once its working add up next (100-n) word probs
				if (levelScore[len(levelScore)-1] + probSumRemaining(wordSet,elementIndex,(stackSize-len(stack)))) > bestScore:
					#add to stack
					stack.append(wordSet[elementIndex][:])
					#add set prob to levelScore list
					levelScore.append(probability.scan_words(probscores,stack[:]+fullSolution[:]))
				else:
					#If its not better than we have no reason to stay and therefore pop word
					stack.pop()
					levelScore.pop()

	fullSolution.extend(bestSet)

	for i in bestSet:
		i[4] = i[3]+1
		wordSet.remove(i)

	t1 = time.time()
	total = t1-t0
	print 'Local solution time: ',total	


print probability.scan_words(probscores,fullSolution[:])
#print wordSet[0:50]
		#so the next time we get to this position in tree we will pick the next word down the list
		#stack[len(stack)-1][4] += 1
print 'wordSet size: ',len(wordSet)
t_1 = time.time()
total = t_1-t_0
print 'Solution time: ',total

#Branch and Bound