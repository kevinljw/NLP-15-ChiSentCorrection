#encoding=utf-8

import jieba
import jieba.posseg

class PartOfSpeechBigram:
	def __init__(self):
		trainFile = open("input/noTag.txt",'r')
		bigramFile = open("tmp/bigram_partofspeech.txt",'w')

		self.totalCount = 0
		self.biGram = {}
		biGramHashKeyList = []

		for line in trainFile:
		    line.decode('utf8')
		    line = line.rstrip()
		    words = jieba.posseg.cut(line)
		    words_list = list(words)
		    #for word in words_list:
		    #    print word.word+' '+word.flag
		    biGramHashKey = 'ss '+words_list[0].flag
		    if biGramHashKey not in biGramHashKeyList:
		        biGramHashKeyList.append(biGramHashKey)
		        self.biGram[biGramHashKey] = 0
		    self.biGram[biGramHashKey] += 1
		    self.totalCount += 1

		    for i in xrange(len(words_list)-1):
		        biGramHashKey = words_list[i].flag+' '+words_list[i+1].flag
		        if biGramHashKey not in biGramHashKeyList:
		            biGramHashKeyList.append(biGramHashKey)
		            self.biGram[biGramHashKey] = 0
		        self.biGram[biGramHashKey] += 1
		        self.totalCount += 1

		    biGramHashKey = words_list[len(words_list)-1].flag+' se'
		    if biGramHashKey not in biGramHashKeyList:
		        biGramHashKeyList.append(biGramHashKey)
		        self.biGram[biGramHashKey] = 0
		    self.biGram[biGramHashKey] += 1
		    self.totalCount += 1

		bigramFile.write(str(self.totalCount)+'\n')
		for keys, values in self.biGram.items():
		    temp = keys
		    bigramFile.write(temp.encode('utf8')+' '+str(values)+'\n')

	def findImproveRatio(self, str1, str2, str3):
		pair1 = str1+' '+str2
		pair2 = str2+' '+str3
		pair3 = str1+' '+str3
		if pair1 in self.biGram:
			pair1Count = self.biGram[pair1]
		else:
			pair1Count = 0.1
		if pair2 in self.biGram:
			pair2Count = self.biGram[pair2]
		else:
			pair2Count = 0.1
		if pair3 in self.biGram:
			pair3Count = self.biGram[pair3]
		else:
			pair3Count = 0.1
		return (pair3Count*self.totalCount)/(pair1Count*pair2Count)
