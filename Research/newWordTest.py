import math
import random
import GenerateSequenceSamples
import time

class newWord:

	global sequenceSet
	sequenceSet = []
	global dictionarySet
	dictionarySet = []
	global wordLength
	global dictionary
	dictionary = {}

	def __init__(self, seqlength,wLength):
		wordLength = wLength

	def smartWordSelection(self,seqProb,wordset):
		genSeq = GenerateSequenceSamples.generateSequenceSamples()		
		length = len(seqProb)
		#wordLength = len(wordset[0][0])
		wordLength = 11
		#Number of sample negative sequences we want
		n = 1000
		#Set of negative sequences


		t0 = time.time()
		#print len(sequenceSet)
		while len(sequenceSet) < n:
			#generate 1 sample sequence
			sequence = genSeq.getSample(seqProb)

			#keep sequence sample only if wordset is not in it
			negSequence = True
			for i in wordset:
				if i[0] in sequence:
					negSequence = False
					break

			if negSequence:
				sequenceSet.append(sequence)

				#process sequence here
				for i in range(length - wordLength):
					curWord = sequence[i:i+wordLength]
					if dictionary.has_key(curWord):
						count = dictionary[curWord]
						dictionary[curWord] = count + 1
					else:
						dictionary[curWord] = 1

		#print len(sequenceSet)
		t_0 = time.time()
		print t_0 - t0

		t0 = time.time()
		#process and count most popular word at each spot
		bestCount = -1
		bestWord = ''
		#find highest scoring word in set
		candidates = dictionary.keys()
		for j in candidates:
			if dictionary[j] > bestCount:
					bestWord = j
					bestCount = dictionary[j]
		
		t_0 = time.time()
		print t_0 - t0

		t0 = time.time()
		#Should check that there aren't many places and word with this count.... and randomly pick one
		#only delete samples that contain the newly selected word, otherwise keep remaining samples
		indexes = []
		for i in range(len(sequenceSet) -1, -1, -1):
			#At the index!
			if bestWord in sequenceSet[i]:
				#print 'here'
				
				for j in range(length - wordLength):
					curWord = sequenceSet[i][j:j+wordLength]
					
					if curWord == bestWord:
						indexes.append(j)

					if dictionary.has_key(curWord):
						count = dictionary[curWord]
						dictionary[curWord] = count - 1
					else:
						print 'error'

				del sequenceSet[i]

		#print len(indexes)
		index = max(set(indexes), key=indexes.count)	
		#print index	
		#return word with most hits
		t_0 = time.time()
		print t_0 - t0

		return [bestWord,index]
		