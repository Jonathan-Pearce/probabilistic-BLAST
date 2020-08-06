import random

probscores = []
f = open('sequenceStructure.txt','r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))

index = [0,1,2,3]

newSequence = []


for i in probscores:	
	random.shuffle(index)
	
	col = []

	for j in range(4):
		col.append(i[index[j]])

	newSequence.append(col)


for i in range(len(newSequence)):
	string = str(newSequence[i][0])+','+str(newSequence[i][1])+','+str(newSequence[i][2])+','+str(newSequence[i][3])
	print string