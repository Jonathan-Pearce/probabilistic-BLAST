import random

class randomSelection:

	def getWordSet(self, seqStructure, wordLength, wordSetSize):
		bps = ['A','C','G','T']
		wordSet = []
		length = len(seqStructure)

		for i in range(wordSetSize):
			index = int(random.random()*(length-wordLength))
			seqSample = ''

			for j in range(wordLength):
				total = 0
				rand = random.random()
				for k in range(4):
					total += seqStructure[index + j][k]
					if total > rand:
						seqSample += bps[k]
						break

			wordSet.append([seqSample,index])

		print wordSet

		return wordSet

