class greedySelection:

	def getWordSet(self, seqStructure, wordLength, wordSetSize):
		indexScores = []
		wordSet = []
		bps = ['A','C','G','T']

		#Initial Probability for first optimal word in set
		prob = 1.0
		seq = ''
		for i in range(wordLength):
			prob *= max(seqStructure[i])
			seq += bps[seqStructure[i].index(max(seqStructure[i]))]
		indexScores.append([prob,0,seq])

		#shift window one position
		for i in range(len(seqStructure)-wordLength):
			index = i + wordLength
			seq = seq[1:]
			seq += bps[seqStructure[index].index(max(seqStructure[index]))]
			prob /= max(seqStructure[i])
			prob *= max(seqStructure[index])
			indexScores.append([prob,i+1,seq])

		#Sort and extract best words to be used as 
		indexScores.sort(reverse=True)

		#Collect Word Set
		for i in range(wordSetSize):
			wordSet.append([indexScores[i][2],indexScores[i][1]])

		#print wordSet
		#Return set of words
		return wordSet

