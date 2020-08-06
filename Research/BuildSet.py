import BuildUp
import time
import copy

#Objects
buildSet = BuildUp.buildUp() 
#Variables
numWords = 100
wordLength = 11
probscores = []
t0 = time.time()

#Code
filename = 'SeqSet/sequence'+str(19)+'.txt'
f = open(filename,'r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
#########################################################################################################
windows = []
windowScore = 1.0

for i in range(wordLength):
	windowScore *= max(probscores[i])
windows.append([windowScore,0])

for i in range(wordLength,len(probscores)):
	windowScore /= max(probscores[i-wordLength])
	windowScore *= max(probscores[i])
	windows.append([windowScore,i-wordLength+1])

#print windows
windows.sort(reverse=True)
#########################################################################################################
newSeq = [[0.0,0.0,0.0,0.0] for j in range(len(probscores))]

for i in range(len(probscores)):
	newSeq[i][0] = probscores[i][0]
	newSeq[i][1] = newSeq[i][0] + probscores[i][1]
	newSeq[i][2] = newSeq[i][1] + probscores[i][2]
	newSeq[i][3] = 1

#print newSeq
#print 'line break'
#print probscores
#sys.exit(0)

#########################################################################################################
#Build Set
score,wordSet = buildSet.buildup(probscores,numWords,wordLength,newSeq)

#Get end time
t1 = time.time()
total = t1-t0

print score
print wordSet
print total