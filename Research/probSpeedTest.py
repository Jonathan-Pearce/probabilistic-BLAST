import compute_probability
import time


#####READ SEQUENCE
probscores = []
f = open('sequenceStructure.txt','r')
lines = [line.rstrip('\n') for line in f]
for i in lines:
	probscores.append(map(float,i.split(',')))
#####CREATE PROFILE
profile = []
bps = ['A','C','G','T']
for i in probscores:
	dictionary = {}
	for j in range(4):
		dictionary[bps[j]] = i[j]
	#print dictionary
	profile.append(dictionary)



t0 = time.time()

exactProb = compute_probability.compute_probability()
wordSet = [[10, 'GAGGGGCGCCG'], [37, 'TGAACCGGCCC'], [29, 'TCTGCTTCTGA'], [29, 'TCTCCCTCTGA'], [29, 'TCTGCCTCTGA'], [31, 'TCCTTCTGAAC'], [10, 'GGGGGCCGCCG'], [36, 'CTGAACAGGGC'], [44, 'GGCCTTACTCC'], [146, 'GGAGGTATCTA'], [30, 'CTCCTTCTGAA'], [12, 'GAGCCGCCGGG'], [32, 'CCCTCTGAACC'], [39, 'ACTCGGGCCTT'], [42, 'CGGCCCTTACC'], [12, 'GGGCCGCCGGG'], [29, 'TATGCTTCTGA'], [37, 'TGAACGGGCCC'], [12, 'GGGGCGCCGGG'], [111, 'CCCAGTGGATA'], [146, 'GGAGGTATCTC'], [29, 'TATGCCTCTGA'], [29, 'TCTCCCTATGA'], [37, 'TGAATCGGCCC'], [46, 'CCTTACCCCGC'], [69, 'ATATGGCTCTT'], [29, 'TATCCTTCTGA'], [143, 'TCATGAGGTAT'], [29, 'TATCCCTCTGA'], [29, 'TCTGCCTATGA'], [30, 'CTCCTTATGAA'], [37, 'TGAACCGGGCC'], [44, 'GCCCTTACTCC'], [44, 'GCCCTAACCCC'], [100, 'CCACATTAGTT'], [44, 'GCCCTAACTCC'], [29, 'TCTGCCTGTGA'], [69, 'ATAAAGCTCTT'], [37, 'TGAACCGGCCA'], [105, 'TTAGTTCCTAG'], [12, 'GGGCCGCCGTG'], [124, 'CTCCGATTGAT'], [37, 'TGAACGGGGCC'], [114, 'AGTGGATAAGC'], [29, 'TCTGCTTATGA'], [30, 'CTCCTTGTGAA'], [29, 'TCTGCTTGTGA'], [37, 'TGAACCAGCCC'], [159, 'GAGGCACCTGA'], [31, 'TGCCTCTGAAC'], [146, 'GGAGGAATCTC'], [12, 'GCGCCGCCGGG'], [29, 'TCTCCATCTGA'], [74, 'GCTCGTTATGG'], [12, 'GTGCCGCCGTG'], [30, 'CTGCTTCTGAA'], [12, 'GGGCAGCCGGG'], [37, 'TGAACAGGCCC'], [29, 'TCTCCTTCTGA'], [120, 'TAGGCTCTGAT'], [37, 'TGAATGGGCCC'], [104, 'ATTTGTTCCCA'], [69, 'ATTTAGCTCTT'], [37, 'TGAACCTGGCC'], [12, 'GAGCCGCCGTG'], [119, 'ATAGGCTCCGA'], [12, 'GGGGCGCCGTG'], [73, 'AGCTCTTAAAG'], [29, 'ACTGCCTCTGA'], [29, 'TCTGCATCTGA'], [37, 'TGAACGGGCCA'], [29, 'TCTCCCTGTGA'], [29, 'TCTGCCTTTGA'], [146, 'GTAGGTATCTC'], [60, 'CTCACCTTGAT'], [146, 'GGAGGTTTCTC'], [74, 'GCTCGTAATGG'], [29, 'TCTCCCTTTGA'], [119, 'ATAAGCTCCGA'], [43, 'GGGCCTTACCC'], [12, 'GCGCCGCCGTG'], [12, 'GCGGCGCCGGG'], [37, 'TGAATCGGGCC'], [37, 'TGAATAGGCCC'], [140, 'CACTCAGGAGG'], [69, 'ATAAGGCTCTT'], [29, 'TCCGCTTCTGA'], [69, 'ATAAAGCTCGT'], [37, 'TGAACGTGCCC'], [38, 'GAATCTGGCCT'], [146, 'TGAGGTTTCTC'], [29, 'TACGCCTCTGA'], [30, 'CCGCCTCTGAA'], [12, 'GCGGCGCCGTG'], [146, 'GGAGGTATCAC'], [30, 'CTGACTCTGAA'], [36, 'CTGAACCAGGC'], [44, 'GGCATTACTCC'], [74, 'GCTCTTTACGG'], [146, 'GTAGGTATCTA']]
exactSetProb = exactProb.scan_words(probscores,wordSet)
print exactSetProb
exactSetProb = exactProb.scan_words(probscores,wordSet)
print exactSetProb



t1 = time.time()
total = t1-t0
print total