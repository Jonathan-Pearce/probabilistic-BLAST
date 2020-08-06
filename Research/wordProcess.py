import math  

bpScore = {'A':0, 'C':1, 'G':2, 'T':3}
bps = ['A','C','G','T']

seq = 'ACTGTG'
score = 0

for i in range(len(seq)):
	char = seq[i:i+1]
	score += int(bpScore[char]*math.pow(4,i))
print score

word = ''
i = 0
while score > 0:
	 char = score % 4
	 score -= char 
	 score /= 4
	 word += bps[char]

print word 
