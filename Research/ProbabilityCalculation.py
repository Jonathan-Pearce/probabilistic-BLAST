import math 
import random
import GenerateSequenceSamples
import CalculateWordSetProbability


seqSamples = GenerateSequenceSamples.generateSequenceSamples()
seqSamples.generateExampleSequencesJ(1000000)

#0.6658
#wordSet = [['AGC',0],['CAG',2]] 

#0.273
#wordSet = [['AGC',0],['TAG',2]] 


#Read Example Data
wordSet = []

with open('ExampleWordSet.txt') as f:
	for line in f:
		parts = line.split(' ')
		wordSet.append([parts[0],int(parts[1])])


exampleProb = CalculateWordSetProbability.wordSetProbability()
print exampleProb.exampleLocationSpecificProbabilityJ(wordSet)


