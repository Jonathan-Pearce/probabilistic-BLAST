import math
import random


class generateWordSet:

	def getPositionSet(self,size,length):
		words = []

		basepairs = open('sequence.txt').readline()
		probs = map(float,open('sequenceprob.txt').readline().split(' '))

		bpScore = {'A':0, 'C':1, 'G':2, 'T':3}
		bps = ['A','C','G','T']
		probscores = []

		#build the seqeunce
		for i in range(len(probs)):
			pos = bpScore[basepairs[i:i+1]] #find most likely nucleotide index
			score = probs[i] # score of most likely nucleotide
			altScore = (1-score)/3 # score of other 3 nucleotides
			scores = [altScore,altScore,altScore,altScore]
			scores[pos] = score
			probscores.append(scores) #add 4 scores to sequence profile

		#randomly acquire k words
		seqLength = len(probscores)
		#generate sample words
		for i in range(size):
			#randomly select positon in sequence
			pos = int(random.random() * (seqLength-length+1))
			sample = ''
			for j in range(length):
				rand = random.random()
				indexSum = 0
				for k in range(4):
					indexSum += probscores[pos+j][k]
					if indexSum > rand:
						sample += bps[k]
						break
			words.append([sample,pos])	

		return words		


	def genWordSet(self,size,length):	

		f = open('wordSet.txt','w') 

		nucleotides = ['A','C','G','T']

		for i in range(size):
			seq = ''
			for j in range(length):
				rand = (int)(random.random()*4) #get number between 0 and 3
				nucleotide = nucleotides[rand]
				seq += nucleotide
			if(i != size-1):
				f.write(seq+' ')
			else:
				f.write(seq)


	def genPositionWordSet(self,size,length):
		#file
		g = open('posWordSet.txt','w')
		words = getPositionSet(size,length)
		size = len(words)
		for i in range(size):
			if(i != size-1):			
				g.write(words[i][0]+' '+words[i][1]+'\n')
			else:
				g.write(words[i][0]+' '+words[i][1])