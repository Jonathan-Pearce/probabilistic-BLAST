import compute_probability
import NewWord


def flipSet(wordSet):
		newSet = []
		for i in wordSet:
			newSet.append([i[1],i[0]])
		#print newSet
		return newSet

bps = ['A','C','G','T']
wordLength = 11
probScores = []
wordSetSize = 100
#########################################################################################################
#READ SEQUENCE
probscores = []
filename = 'SeqSet/sequence'+str(0)+'.txt'
#f = open('sequenceStructure.txt','r')
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))


newSeq = [[0.0,0.0,0.0,0.0] for j in range(len(probscores))]
for i in range(len(probscores)):
	newSeq[i][0] = probscores[i][0]
	newSeq[i][1] = newSeq[i][0] + probscores[i][1]
	newSeq[i][2] = newSeq[i][1] + probscores[i][2]
	newSeq[i][3] = 1	
#print probscores
#Probabilty Calcualation
exactProb = compute_probability.compute_probability()
newWord = NewWord.newWord(len(probscores),wordLength)
#########################################################################################################

#another time got: 0.584115813399

#0.580528386069
#solution = [['CAGCAGTTCGG', 104], ['CGGCAGTTCGG', 104], ['AAACTCCAGAT', 15], ['CCGCAGTTCGG', 104], ['AACAGCAGTTC', 102], ['AAACTCAAGAT', 15], ['GTTCGGGTAGT', 109], ['GATTAATGACA', 23], ['GTTCGGGTACT', 109], ['GATTAATGCCA', 23], ['AAACTGCAGAT', 15], ['GTTCGGCTAGT', 109], ['AAACTCCAGGT', 15], ['AACGGCAGTTC', 102], ['GTTCGGCTACT', 109], ['AACCGCAGTTC', 102], ['TCCCTGCCCGC', 77], ['AAACTACAGAT', 15], ['ATAACTCCAAG', 150], ['ACAGCGGTTCG', 103], ['ACAGCCGTTCG', 103], ['ACAACAGTTCG', 103], ['CAGCAGTTCGA', 104], ['ACACCAGTTCG', 103], ['AAACTTCAGAT', 15], ['CAGCAATTCGG', 104], ['GTCTATCACCT', 122], ['AAACTGAAGAT', 15], ['AACCTCCAGAT', 15], ['TCCCTGCCCAC', 77], ['AGTCCATAACT', 145], ['GCCACAGGGGC', 52], ['GGGACGTCCCT', 71], ['AAACACCAGAT', 15], ['AAACTAAAGAT', 15], ['AAACTCAAGGT', 15], ['AGTACATAACT', 145], ['GGTTAATGCCA', 23], ['GTTCGGCTCGT', 109], ['GTTCGGGTCGT', 109], ['GTTCGGATAGT', 109], ['GTTCGGGTCCT', 109], ['TCAGTGCATAA', 143], ['GGACAGCAGTT', 101], ['CAGTTCGAGTA', 107], ['AAACTGCAGGT', 15], ['GTTCGGATACT', 109], ['AAACTCCAAAT', 15], ['AACAGGGGCGC', 54], ['TCCATAAATCC', 147], ['TTATTTTCAGT', 137], ['ACACTCCAGAT', 15], ['GATTGATGACA', 23], ['AAACTTAAGAT', 15], ['AAACTACAGGT', 15], ['GTCGATCACCT', 122], ['TCAGTCGATAA', 143], ['AGGGGCGTCCC', 70], ['GGTTAATGACA', 23], ['CAGTTCAGGTA', 107], ['CTGGGCTTATT', 131], ['GTCTATCATCT', 122], ['AAACTCCTGAT', 15], ['AACCTCAAGAT', 15], ['ACGGCGGTTCG', 103], ['CACCTGGTCTT', 128], ['TTCAGTCCATA', 142], ['TGCATAACTCC', 147], ['CTGGGATTATT', 131], ['GTCTAGCACCT', 122], ['GTTCGGCTCCT', 109], ['GATTGATGCCA', 23], ['CAGGGGCTCTC', 56], ['TCCCTGCCCGT', 77], ['ATAAATCCAAG', 150], ['GATTAATGTCA', 23], ['GATTAATTACA', 23], ['CGGCAATTCGG', 104], ['AGCACTGAAAC', 8], ['CACAGGGGCGC', 54], ['CAGTTCAGCTA', 107], ['TCCATAACTCC', 147], ['ACGACAGTTCG', 103], ['ATCACTGAAAC', 8], ['TCAGTAGATAA', 143], ['ATCACTTAAAC', 8], ['GGACGGCAGTT', 101], ['CTGGTATTATT', 131], ['ACGCCAGTTCG', 103], ['TCGATAACTCC', 147], ['GACTGCAACAG', 48], ['AACCTGCAGAT', 15], ['ACCGCGGTTCG', 103], ['ACAGCATTTCG', 103], ['AAACACAAGAT', 15], ['GTCCATCACCT', 122], ['GATTAATTCCA', 23], ['TCCATATCTCC', 147], ['TTCAGTACATA', 142], ['GACTGCCACAG', 48]]

solution = [['CAGCAGTTCGG', 104], ['CGGCAGTTCGG', 104], ['AAACTCCAGAT', 15], ['CCGCAGTTCGG', 104], ['AACAGCAGTTC', 102], ['AAACTCAAGAT', 15], ['GTTCGGGTAGT', 109], ['GATTAATGACA', 23], ['GTTCGGGTACT', 109], ['GATTAATGCCA', 23], ['AAACTGCAGAT', 15], ['GTTCGGCTAGT', 109], ['AAACTCCAGGT', 15], ['AACGGCAGTTC', 102], ['GTTCGGCTACT', 109], ['AACCGCAGTTC', 102], ['TCCCTGCCCGC', 77], ['AAACTACAGAT', 15], ['ACAGCGGTTCG', 103], ['ACAGCCGTTCG', 103], ['ACAACAGTTCG', 103], ['ACACCAGTTCG', 103], ['AAACTTCAGAT', 15], ['CAGCAATTCGG', 104], ['GTCTATCACCT', 122], ['AAACTGAAGAT', 15], ['AACCTCCAGAT', 15], ['TCCCTGCCCAC', 77], ['AGTCCATAACT', 145], ['AAACACCAGAT', 15], ['AAACTAAAGAT', 15], ['AAACTCAAGGT', 15], ['GGTTAATGCCA', 23], ['GTTCGGCTCGT', 109], ['GTTCGGGTCGT', 109], ['GTTCGGATAGT', 109], ['GTTCGGGTCCT', 109], ['TCAGTGCATAA', 143], ['GGACAGCAGTT', 101], ['CAGTTCGAGTA', 107], ['AAACTGCAGGT', 15], ['GTTCGGATACT', 109], ['AAACTCCAAAT', 15], ['AACAGGGGCGC', 54], ['ACACTCCAGAT', 15], ['GATTGATGACA', 23], ['AAACTTAAGAT', 15], ['AAACTACAGGT', 15], ['GTCGATCACCT', 122], ['TCAGTCGATAA', 143], ['AGGGGCGTCCC', 70], ['GGTTAATGACA', 23], ['CAGTTCAGGTA', 107], ['CTGGGCTTATT', 131], ['GTCTATCATCT', 122], ['AAACTCCTGAT', 15], ['AACCTCAAGAT', 15], ['TTCAGTCCATA', 142], ['TGCATAACTCC', 147], ['CTGGGATTATT', 131], ['GTCTAGCACCT', 122], ['GTTCGGCTCCT', 109], ['GATTGATGCCA', 23], ['TCCCTGCCCGT', 77], ['ATAAATCCAAG', 150], ['GATTAATGTCA', 23], ['GATTAATTACA', 23], ['CGGCAATTCGG', 104], ['CACAGGGGCGC', 54], ['CAGTTCAGCTA', 107], ['TCCATAACTCC', 147], ['ATCACTGAAAC', 8], ['CTGGTATTATT', 131], ['TCGATAACTCC', 147], ['AACCTGCAGAT', 15], ['ACAGCATTTCG', 103], ['GTCCATCACCT', 122], ['GATTAATTCCA', 23], ['TTCAGTACATA', 142], ['GACTGCCACAG', 48], ['CAGTTCCGGTA', 107], ['AACGGCCGTTC', 102], ['GTCTATCAACT', 122], ['TCATTCCATAA', 143], ['GCAACAGGGGC', 52], ['CTGGTCTTATT', 131], ['GACAGCCACAG', 48], ['TACATAACTCC', 147], ['TGGATAACTCC', 147], ['TAGATAACTCC', 147], ['CAGTTCCGCTA', 107], ['AGGGACGTCCC', 70], ['CAGCAGTTCGA', 104], ['AACCGCGGTTC', 102], ['AAACTCAAAAT', 15], ['CAGGGGCTCTC', 56], ['ACGGCGGTTCG', 103], ['TCCCTGCCCAT', 77], ['GGACGGCAGTT', 101], ['TCCATATCTCC', 147]]

exactSetProb = exactProb.scan_words(probscores,flipSet(solution))
print exactSetProb
print len(solution)

topScore = 0
bestSet = None

for j in range(10):

	print j

	bestScore = 0
	element = None
	index = -1

	#decide which word to remove
	for i in range(100):
		copy = solution[:]

		del copy[i]

		exactSetProb = exactProb.scan_words(probscores,flipSet(copy))

		#we want to see which element contributes the least to the score
		if exactSetProb > bestScore:
			bestScore = exactSetProb
			element = solution[i][:]
			index = i

	#print element
	#sys.exit(0)

	partialSet = solution[:]
	del partialSet[index]

	# while True:
	# 	data = newWord.smartWordSelection(newSeq,partialSet,1)
	# 	if data[0] != element[0]:
	# 		print 'new word: ',data[0]
	# 		print 'old word: ',element[0]
	# 		partialSet.append(data)
	# 		break

	data = newWord.smartWordSelection(newSeq,partialSet,1)
	partialSet.append(data)

	#data = newWord.smartWordSelection(newSeq,partialSet,1)
	#partialSet.append(data)

	exactSetProb = exactProb.scan_words(probscores,flipSet(partialSet))
	print exactSetProb
	if exactSetProb > topScore:
		topScore = exactSetProb
		bestSet = partialSet[:]

	del solution[index]
	solution.append(data)


print topScore
print bestSet
print exactProb.scan_words(probscores,flipSet(bestSet))







