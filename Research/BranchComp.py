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


#with open('branchData11.txt', 'rb') as f:
#    wordSet = pickle.load(f)

#print len(wordSet)
#print wordSet[0:10]
#sys.exit(0)
 


bps = ['A','C','G','T']
wordLength = 11
probScores = []
wordSetSize = 20
#########################################################################################################
#READ SEQUENCE
probscores = []
filename = 'SeqSet4/sequence'+str(1)+'.txt'
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
if True:
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
	#with open('branchData11.txt', 'wb') as f:
	#    pickle.dump(wordSet, f)

	#sys.exit(0)


#print wordSet[0:10]

print len(wordSet)

wordSet = wordSet[0:250]
print len(wordSet)

#sys.exit(0)

# #the idea here is to get the sum probability of the 100 words after each word
# nextkWords = [0]
# prob = 0
# #get top 100 words prob, minus the best word
# for i in range(1,wordSetSize+1):
# 	prob += wordSet[i][2]
# nextkWords.append(prob)

# #INDEX CHECK HERE
# for i in range(1,len(wordSet)):
# 	prob -= wordSet[i][2]
# 	#make sure we're still inbounds!
# 	if(i+wordSetSize+1 < len(wordSet)):
# 		prob += wordSet[i+wordSetSize+1] # +1 or nah??!?
# 	nextkWords.append(prob)

#########
#HERE we have our wordset which is all acceptable words, with their index and score
#The words are sorted by probability
#and we have a list of the sum of probability of the 100 words that follow each word to help prune!

# testList = []
# #call list to actually copy element without reference
# testList.append(wordSet[0][:])
# testList[0][4] += 1

# testList.append(wordSet[1][:])

# print testList
# print wordSet[0]


#sys.exit(0)
t0 = time.time()
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

iteration = 0

while(not solution):
	iteration += 1
	if iteration % 10000 == 0:
		print bestScore
	#print bestScore
	#print stack

	#if we have a full set
	if(len(stack) == wordSetSize):
		#get score
		solnScore = probability.scan_words(probscores,stack[:])
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
			if probSumRemaining(wordSet,firstWordIndex,wordSetSize) > bestScore:
				#add to stack
				stack.append(wordSet[firstWordIndex][:])
				#add word prob to levelScore list
				levelScore.append(element[2])
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
			if (levelScore[len(levelScore)-1] + probSumRemaining(wordSet,elementIndex,(wordSetSize-len(stack)))) > bestScore:
				#add to stack
				stack.append(wordSet[elementIndex][:])
				#add set prob to levelScore list
				levelScore.append(probability.scan_words(probscores,stack[:]))
			else:
				#If its not better than we have no reason to stay and therefore pop word
				stack.pop()
				levelScore.pop()


		#need to look at rank of last word
		#and to what index the following words have been explored
		#then take the next index


		#when we add a word just add a counter with the data that says index + 1
		#as we move along the counter will go up so we know which word to add when we get back to this level


		#index = stack[len(stack)-1][4]
		#stack.append([wordSet[index])

		#so the next time we get to this position in tree we will pick the next word down the list
		#stack[len(stack)-1][4] += 1
print 'wordSet size: ',len(wordSet)
t1 = time.time()
total = t1-t0
print 'Solution time: ',total

#Branch and Bound