#code for simulating  
import sys
import math
import random

class generateSequenceSamples:

	def genSamples(self,size):
		#file that will hold sequences samples
		f = open('sequenceSamples.txt','w') 
		#Open files
		basepairs = open('sequence.txt').readline()
		probs = map(float,open('sequenceprob.txt').readline().split(' '))
		probSeq = self.createProbSequence(basepairs,probs)
		self.createSamples(f,probSeq,size)


	def generateExampleSequences(self,size):
		#file that will hold sequences samples
		f = open('ExampleSequenceSamples.txt','w') 
		#Open files
		basepairs = open('ExampleSequence.txt').readline()
		probs = map(float,open('ExampleSequenceProb.txt').readline().split(' '))
		#print basepairs
		#print probs
		probSeq = self.createProbSequence(basepairs,probs)
		self.createSamples(f,probSeq,size)


	def generateExampleSequencesJ(self,size):
		probSeq = []
		with open('ExampleSequenceProbJasmine.txt') as f:
			for line in f:
				probs = map(float,line.split(','))
				probSeq.append(probs)
		#print probSeq
		f = open('ExampleSequenceSamplesJ.txt','w')
		self.createSamples(f,probSeq,size)


	def createProbSequence(self,basepairs,probs):
		bpScore = {'A':0, 'C':1, 'G':2, 'T':3}
		bps = ['A','C','G','T']
		probscores = []
		for i in range(len(probs)):
			pos = bpScore[basepairs[i:i+1]] #find most likely nucleotide index
			scores = []
			score = probs[i] # score of most likely nucleotide
			altScore = (1-score)/3 # score of other 3 nucleotides
			for j in range(4): #put 4 scores to together
				if j == pos: 
					scores.append(score)
				else:
					scores.append(altScore)
			probscores.append(scores) #add 4 scores to sequence profile
		return probscores



	#WE NEED
	def createSamples(self,fileName,probscores,numSamples):
		########################################################################
		f = open(fileName,'w') 

		for i in range(numSamples-1):			
			f.write(self.getSample(probscores)+'\n')
		f.write(self.getSample(probscores))

	
	def getSample(self,probscores):
		bps = ['A','C','G','T']
		size = len(probscores)
		sampleSeq = ''
		nuc = []

		for i in range(size):
			rand = random.random()
			indexSum = 0
			for j in range(4):
				#indexSum += probscores[i][j]
				if probscores[i][j] > rand:
					sampleSeq += bps[j]
					#nuc.append(bps[j])
					break
		#sampleSeq = ''.join(nuc)
		return sampleSeq

	#could just turn this into one method where if you want entire sequnece, index = 0, wlength = 200
	def getIndexSample(self,probscores,index,wordlength):
		bps = ['A','C','G','T']
		size = wordlength
		sampleSeq = ''

		for i in range(size):
			rand = random.random()
			indexSum = 0
			for j in range(4):
				#pick the right area
				indexSum += probscores[index+i-1][j]
				if indexSum > rand:
					sampleSeq += bps[j]
					break

		return sampleSeq

