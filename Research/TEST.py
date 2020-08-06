import random

bpScore = {'A':0, 'T':1, 'C':2, 'G':3}
bps = ['A','T','C','G']

seq = [[1,0,0,0],[0.5,0,0.5,0],[0.1,0.8,0,0.1],[0,0,0,1],[0.5,0.2,0.2,0.1],[0.4,0.4,0.1,0.1],[0,0.25,0.75,0],[0.1,0.9,0,0],[0.1,0.4,0,0.5],[0.25,0.25,0.25,0.25],[0,0,0,1]]


for i in range(len(seq)):
	print sum(seq[i])


wordSet = [['ACTG', 0], ['ATGA', 1], ['AACT', 4], ['ACCT', 4], ['CTAG', 6], ['TAGG', 7]]

length = 4
n = 100000	
matches = 0

for i in range(n):
	sampleSeq = ''
	for j in seq:
		rand = random.random()
		colSum = 0
		for k in range(4):
			colSum += j[k]
			if rand < colSum:
				sampleSeq += bps[k]
				break
	
	#print sampleSeq

	#now we have sample sequence
	for i in wordSet:
		index = i[1]
		sample = sampleSeq[index:index+length]
		#print sample
		if sample == i[0]:
			matches += 1
			break

print matches*1.0/n



