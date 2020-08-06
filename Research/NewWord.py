import math
import random
import GenerateSequenceSamples
import time
import NewWord


class newWord:

	def __init__(self, seqlength,wLength):
		global sequenceSet
		global dictionarySet
		global wordLength
		global topCounts
		global genSeq
		global indexWords
		sequenceSet = []
		dictionarySet = []
		topCounts = []
		genSeq = GenerateSequenceSamples.generateSequenceSamples()	
		indexWords = []	
		wordLength = wLength
		
		for i in range(seqlength-wordLength):
			dictionary = {}
			dictionarySet.append(dictionary)
			topCounts.append(0)
			indexWords.append([])

		

	def smartWordSelection(self,seqProb,wordset,index):
		length = len(seqProb)
		#wordLength = len(wordset[0][0])
		wordLength = 11
		#Number of sample negative sequences we want
		if index < 20:
			n = 10000
		else:
			n = 10000
		#Set of negative sequences
		newSequences = []

		#print index
		#t0 = time.time()

		while len(sequenceSet) < n:
			#print 'here'
			#generate 1 sample sequence
			#t0 = time.time()
			sequence = genSeq.getSample(seqProb)
			#t_0 = time.time()
			#print 'Time to generate Sequence: ',t_0 - t0

			#keep sequence sample only if wordset is not in it
			# negSequence = True
			# for i in range(len(indexWords)):
			# 	wordSeqIndex = sequence[i:i+wordLength]
			# 	for j in indexWords[i]:
			# 		if wordSeqIndex == j:
			# 			negSequence = False
			# 			break

			negSequence = True
			for i in wordset:
				if i[0] in sequence:
					negSequence = False
					break			

			if negSequence:
				#t0 = time.time()
				sequenceSet.append(sequence)
				#newSequences.append(sequence)

				#process sequence here
				#maybe speed this up
				for i in range(length - wordLength):
					#if we want to bother with the index then process
					curWord = sequence[i:i+wordLength]
					if dictionarySet[i].has_key(curWord):
						count = dictionarySet[i][curWord]
						dictionarySet[i][curWord] = count + 1
						if count + 1 > topCounts[i]:
							topCounts[i] = count + 1
					else:
						dictionarySet[i][curWord] = 1

				#t_0 = time.time()
				#print 'Time to process Sequence: ',t_0 - t0

		#t_0 = time.time()
		#print t_0 - t0
		#t0 = time.time()

		
		#process and count most popular word at each spot
		bestCount = -1
		bestWord = ''
		index = -1
		#find highest scoring word in set
		#for i in range(length - wordLength):
		#print topCounts
		i = topCounts.index(max(topCounts))

		candidates = dictionarySet[i].keys()
		for j in candidates:
			if dictionarySet[i][j] > bestCount:
					bestWord = j
					index = i
					bestCount = dictionarySet[i][j]

		indexWords[index].append(bestWord)

		#print bestWord
		#print index
		#t_0 = time.time()
		#print t_0 - t0
		#t0 = time.time()

		#Should check that there aren't many places and word with this count.... and randomly pick one
		#only delete samples that contain the newly selected word, otherwise keep remaining samples
		for i in range(len(sequenceSet) -1, -1, -1):
			#At the index!
			if bestWord == sequenceSet[i][index:index+wordLength]:
				for j in range(length - wordLength):
					curWord = sequenceSet[i][j:j+wordLength]
					count = dictionarySet[j][curWord]
					dictionarySet[j][curWord] = count - 1
					if topCounts[j] == count:
						topCounts[j] -= 1
				del sequenceSet[i]

		#return word with most hits
		#t_0 = time.time()
		#print t_0 - t0

		return [bestWord,index]



