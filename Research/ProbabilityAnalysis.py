#For comparing the difference between complete probability and targetted probability

import GenerateSequence
import GenerateSequenceSamples
import GenerateWordSet
import WordSetProbability

####SETUP

# 0 - false
# 1 - true

#SEQUENCE GENERATION
sequenceLength = 200
if 1: #only 1 when we want sequence of new length
	#Sequence Generation
	seqGen = GenerateSequence.generateSequence()
	seqGen.generateSeq(sequenceLength)

#SEQUENCE SAMPLES
numSamples = 1000
if 1: #only 1 when we want new set of samples
	#Sequence Samples
	sampleSeqGen = GenerateSequenceSamples.generateSequenceSamples()
	sampleSeqGen.genSamples(numSamples)

#WORD SET
numWords = 100
wordLength = 10
if 1: #only 1 when we want more words or words of different length or both!
	#Create Word set
	wordSetGen = GenerateWordSet.generateWordSet()
	#wordSetGen.genWordSet()
	#wordSetGen.genPositionWordSet()
	wordSet = wordSetGen.getPositionSet(numWords,wordLength)
	#print wordSet

print 'Sequence Length: ', sequenceLength
print 'Number of Sequence Samples: ', numSamples
print 'Number of Words in Set: ', numWords
print 'Word Length: ', wordLength,'\n'

prob = WordSetProbability.wordSetProbability()

print 'Looking at locations of sampling only'
print prob.locationSpecificProbability(wordSet),'\n'

print 'Looking at entire sequence'
print prob.generalProbability(wordSet)