import compute_probability
import random

def flipSet(wordSet):
		newSet = []
		for i in wordSet:
			newSet.append([i[1],i[0]])
		#print newSet
		return newSet


def getSample(probscores):
		bps = ['A','C','G','T']
		size = len(probscores)
		sampleSeq = ''
		nuc = []

		for i in range(size):
			rand = random.random()
			indexSum = 0
			for j in range(4):
				indexSum += probscores[i][j]
				if indexSum > rand:
					sampleSeq += bps[j]
					#nuc.append(bps[j])
					break
		#sampleSeq = ''.join(nuc)
		return sampleSeq


#current solution being tested
#0.578134855754
solution = [['GTCCAGTGCTT', 35], ['AACGACCTTCT', 132], ['GTCCAGTGCAT', 35], ['GCCCAGTGCTT', 35], ['GTCCAGTGCCT', 35], ['GCGCTCGCATA', 52], ['TGCCGAGGCGC', 45], ['TTAACCCGCAC', 175], ['CTCGCCGCACA', 122], ['GGCGTTGAGCG', 12], ['TGACGAGGCGC', 45], ['TCTTCGGATAA', 140], ['GCACCCGCCGG', 182], ['GCGCTCCCATA', 52], ['AACCACCTTCT', 132], ['CTCGCCGCTCA', 122], ['AACGCCCTTCT', 132], ['TTTCACCCGCA', 174], ['CCGTGCTGACA', 106], ['TTTAACCGGCA', 174], ['TGCAGAGGCGC', 45], ['GTCGAGTGCTT', 35], ['CTCGCGGCTCA', 122], ['TCCAGTGCTTG', 36], ['GCACCCGCGGG', 182], ['CTCGCGGCACA', 122], ['GCACCGGCCGG', 182], ['GGCGGTGAGCG', 12], ['TCTTCGCATAA', 140], ['TCTTCGGTTAA', 140], ['GCGCACGCATA', 52], ['TTTAACCAGCA', 174], ['TTAACCTGCAC', 175], ['GCCCAGTGCAT', 35], ['GTCCACTGCTT', 35], ['GCGCTCGAATA', 52], ['GTTGAGCGATG', 15], ['GTTGAGCGACG', 15], ['AACTACCTTCT', 132], ['TGAAGAGGCGC', 45], ['TTCACCGGCAC', 175], ['TCTTCGGCTAA', 140], ['GGTGAGCGATG', 15], ['GGCCTCCCCAC', 92], ['TGCCGGGGCGC', 45], ['GCGCTCGTATA', 52], ['GCCCCCCCACG', 93], ['GCACAACGACC', 128], ['GCACCGGCGGG', 182], ['GCGCTCCAATA', 52], ['CCGGGCTGACA', 106], ['GCGCTCACATA', 52], ['GGCCCCCCCCC', 92], ['GCTCAACGACC', 128], ['AACCCCCTTCT', 132], ['GCGCGCGCATA', 52], ['GCCCAGTGCCT', 35], ['AAGGACCTTCT', 132], ['TCCAGAGGCGC', 45], ['AACAACCTTCT', 132], ['CAGTGCTGACA', 106], ['TTTTACCCGCA', 174], ['TTTCACCTGCA', 174], ['GCGCACCCATA', 52], ['GTCCATTGCTT', 35], ['GCGTGGAGCGA', 13], ['GGCCTCCCCCC', 92], ['ACCGACCTTCT', 132], ['GCGCTCCTATA', 52], ['TCCCGAGGCGC', 45], ['CACGCCGCACA', 122], ['TCACGAGGCGC', 45], ['GCACCAGCCGG', 182], ['TTCACCAGCAC', 175], ['GTAGAGCGATG', 15], ['GCACCAGCGGG', 182], ['GTTGAGCGGCG', 15], ['GTTGAGCGGTG', 15], ['GTCGAGTGCAT', 35], ['GTCCTGTGCTT', 35], ['GGTGAGCGGTG', 15], ['TCTTCGCTTAA', 140], ['TGCGGAGGCGC', 45], ['CCGTGCTGATA', 106], ['CCAGTGCTTCC', 37], ['TGCCGACGCGC', 45], ['TGACGGGGCGC', 45], ['GCACCCGCCCG', 182], ['CCGTGCTGACC', 106], ['TCTTCGGGTAA', 140], ['ACCTTCTTCAG', 136], ['GTAGAGCGGTG', 15], ['GCGGGGAGCGA', 13], ['GTAGAGCGACG', 15], ['GGTGAGCGACG', 15], ['TGCAGGGGCGC', 45], ['GCCGAGTGCTT', 35], ['ATCGACCTTCT', 132], ['ACCTTTTTCGG', 136], ['GCGCTCGCCTA', 52]]


#get sequence
probscores = []
filename = 'SeqSet/sequence'+str(19)+'.txt'
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
################################################

#print probscores

#Jasmine's prob:
exactProb = compute_probability.compute_probability()
exactSetProb = exactProb.scan_words(probscores,flipSet(solution))
print exactSetProb


#n = 1,000,000
n=100000

numIndexHits = 0
numHits = 0

seqLength = len(probscores)
wordLength = len(solution[0][0])

for i in range(n):
	sample = getSample(probscores)

	generalHit = False
	indexHit = False

	#print sample

	# for j in range(seqLength-wordLength):

	# 	#move through sample
	# 	curWord = sample[j:j+wordLength]

	# 	for k in solution:
	# 		if k[0] == curWord and not generalHit:
	# 			numHits += 1
	# 			generalHit = True
				
	# 		if k[0] == curWord and k[1] == j and not indexHit:
	# 			numIndexHits += 1
	# 			indexHit = True
	
	for j in solution:
		if j[0] in sample:
			#print j[0]
			#print 
			numHits += 1
 			break

 	for j in solution:
 		if j[0] == sample[j[1]:j[1]+wordLength]:
 			numIndexHits += 1
 			break
 			



print (numHits*1.0)/n
print (numIndexHits*1.0)/n
