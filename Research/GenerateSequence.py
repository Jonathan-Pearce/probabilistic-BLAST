#Generate a probabalisitic sequence of desired length
import math
import random

class generateSequence:

	def generateSeq(self, length,fileName):
		file3 = open(fileName,'w')

		for i in range(length-1):
			file3.write(self.getColumnString2()+'\n')
		file3.write(self.getColumnString2())

	def getColumnString(self):
		total = 0
		scores = []
		for j in range(4):
			rand = random.random()
			scores.append(rand)
			total += rand
		#normalize
		newscores = [x / total for x in scores]
		string = str(newscores[0])+','+str(newscores[1])+','+str(newscores[2])+','+str(newscores[3])
		print 'here'
		return string

	def getColumnString2(self):
		total = 1
		scores = []

		for j in range(3):
			rand = random.random()*total 
			scores.append(rand)
			total -= rand

		scores.append(total)
		random.shuffle(scores)
		string = str(scores[0])+','+str(scores[1])+','+str(scores[2])+','+str(scores[3])
		print 'here now'
		return string