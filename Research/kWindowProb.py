import math
import random
import itertools

class kWindowProb:

	global window
	global length
	length = 11
	global bpScore
	global bps
	bpScore = {'A':0, 'C':1, 'G':2, 'T':3}
	bps = ['A','C','G','T']

	global comboWord
	global newWords

	#last word selected was from combinatorial set
	comboWord = False
	newWord = []

	def __init__(self, sequence):
		#not all of these will need to be global maybe
		global seqStructure
		seqStructure = sequence


	def BuildSet(self,numWords,index,wordLength):
		global optimalProb
		global optimalWord
		global optimalWordProb
		global wordSet
		global wordSetProb
		global setScores
		global window
		global explored
		global comboWord

		#last word selected was from combinatorial set
		comboWord = False

		seqIndex = index

		optimalWordProb = 1.0
		optimalWord = ''
		wordSet = []
		wordSetProb = 0
		optimalProb = []
		setScores = []
		window = seqStructure[index:index+wordLength]
		explored = [[False for i in range(4)] for j in range(length)]

		#First Word
		for i in range(len(window)):
			#get column
			pos = window[i]
			#get the index of the most likely nucleotide
			index = pos.index(max(pos))
			#get the probabilty of the most likely nucleotide
			optimalWordProb *= pos[index]
			#get the nucleotide
			optimalWord += bps[index]
			#Keep track of best option at each position
			optimalProb.append(pos[index])
			#Update Explore Nucleotides
			explored[i][index] = True

		wordSet.append(optimalWord)
		wordSetProb += optimalWordProb

		setScores.append(optimalWordProb)

		info = self.bestNewNucleotide()
		

		#Collect remainder of set
		for i in range(numWords-1):
			newWord = self.getNewWord()
			wordSet.append(newWord)
			wordSetProb = self.wordScore(newWord)
			setScores.append(wordSetProb)

		data = []

		for i in range(len(wordSet)):
			data.append([seqIndex,wordSet[i],setScores[i]])

		return data




	def getNewWord(self):
		#decide whether combination of used nucleotides or optimal + unused nucleotide is best new word

		#get optimal word and score of already used nucleotides
		data = self.combinatorialWords()

		#position of best unused nucleotide
		data2 = self.bestNewNucleotide()

		#add combinatorial option of already explored nucleotides
		if data[1] > data2[1]:
			#print ''
			comboWord = True
			return data[0]
		else:
			explored[data2[2]][data2[3]] = True
			comboWord = False
			return data2[0]

 
	def bestNewNucleotide(self):
		bestScore = 0
		x = -1 
		y = -1

		for i in range(length):
			for j in range(4):
				#If this nucleotide has not been used before
				if not explored[i][j]:
					score = (optimalWordProb/optimalProb[i])*window[i][j]
					if score > bestScore:
						bestScore = score
						x = i
						y = j

		#format new word
		string = optimalWord[0:x] + bps[y] + optimalWord[x+1:]
		#print string

		return [string,bestScore,x,y]

		

	def combinatorialWords(self):
		#build bpList
		if not comboWord:
			bpList = []
			for i in range(length):
				posList = []
				for j in range(4):
					if explored[i][j]:
						posList.append(bps[j])
				bpList.append(posList)

			#generate all possible words that can be created by explored nucleotides
			combinatorialList = []
			for element in itertools.product(*bpList):
				combinatorialList.append(''.join(element))

			#filter out words that are already in the set
			newWords = [x for x in combinatorialList if x not in wordSet]

		maxScore = 0
		bestWord = ''
		for i in newWords:
			score = self.wordScore(i)

			if score > maxScore:
				maxScore = score
				bestWord = i

		if bestWord != '':
			newWords.remove(bestWord)

		return [bestWord,maxScore]


	#probability of given word
	def wordScore(self,kmer):
		prob = 1.0

		for i in range(length):
			char = kmer[i:i+1]
			prob *= window[i][bpScore[char]]

		return prob