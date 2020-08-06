import math
import random

class wordSetProbability:


    global sequences
    sequences = []

    def exampleLocationSpecificProbability(self,wordSet):
        fileName = 'ExampleSequenceSamples.txt'
        return self.targettedProbability(wordSet,)

    def exampleLocationSpecificProbabilityJ(self,wordSet):
        fileName = 'ExampleSequenceSamplesJ.txt'
        return self.targettedProbability(wordSet)


    def locationSpecificProbability(self,wordSet):
        fileName = 'sequenceSamples.txt'
        return self.targettedProbability(wordSet)

    #Probability of a given wordset and sequence
    #Each word in wordset has a specified location

    def readSequences(self,filename):
        #read sequence samples one by one
        with open(filename) as f:
            for line in f:
                sequences.append(line)

    def targettedProbability(self,wordSet):    
        totalSamples = 0
        matchedSamples = 0

        wordLength = len(wordSet[0][0])

        for j in sequences:
        	totalSamples += 1
        	for i in wordSet:
        		samplePos = i[1]
        		seqWord = j[samplePos:samplePos+wordLength]

        		if seqWord == i[0]:
        			matchedSamples += 1
         			break
        return 1.0*matchedSamples/totalSamples

    
    def generalProbability(self,wordSet):
        totalSamples = 0
        matchedSamples = 0
        #Look everywhere
        with open('sequenceSamples.txt') as f:
            for line in f:
            	totalSamples += 1
            	for i in wordSet:
            		if  i[0] in line:
            			matchedSamples += 1
             			break
        
        return 1.0*matchedSamples/totalSamples