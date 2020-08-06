import NewWord
import compute_probability
import time

#wordSetSize = 150

setScores = []
setTimes = []

class buildUp:


	def flipSet(self,wordSet):
		newSet = []
		for i in wordSet:
			newSet.append([i[1],i[0]])
		#print newSet
		return newSet


	def buildup(self,probscores,size,wordLength,sumSeq):
		wordSet = []

		exactProb = compute_probability.compute_probability()
		newWord = NewWord.newWord(len(probscores),wordLength)

		for i in range(size):
			data = newWord.smartWordSelection(sumSeq,wordSet,i)
			wordSet.append(data)

		exactSetProb = exactProb.scan_words(probscores,self.flipSet(wordSet))

		return exactSetProb,wordSet

	



		
# exactSetProb = exactProb.scan_words(probscores,flipSet(wordSet))
# t1 = time.time()
# total = t1-t0
# setScores.append(exactSetProb)
# #print exactSetProb
# setTimes.append(total)
# #print total

# #print scores

# indexes = []

# for i in range(len(probscores)):
# 	indexes.append([0,i])

# for i in wordSet:
# 	indexes[i[1]][0] += 1

# #print indexes

# indexes.sort(reverse=True)

# print indexes

# for i in setScores:
# print i


# print 'end'
# print '******'
# print 'end'

# for i in setTimes:
# print i