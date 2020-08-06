import GenerateSequence

numSequence = 100
seqLength = 40

path = 'SeqSet4/'
name = 'sequence'

seqGen = GenerateSequence.generateSequence()


for i in range(numSequence):
	fileName = path + name + str(i) + '.txt'
	print fileName
	seqGen.generateSeq(seqLength,fileName)


#fileName = path + name + str(201) + '.txt'
	#print fileName
#seqGen.generateSeq(seqLength,fileName)
