#!/usr/bin/python
# encoding: utf-8

import jieba

class Bigram:
    def __init__(self):
        parsedFile = open("input/noTag.txt",'r')
        bigramFile = open("tmp/bigram_word.txt",'w')

        self.totalCount = 0
        self.biGram = {}
        biGramHashKeyList = []

        for line in parsedFile:
            line.decode('utf8')
            line = line.rstrip()
            words = jieba.cut(line)
            token = list(words)

            biGramHashKey = 'S '+token[0]
            if biGramHashKey not in biGramHashKeyList:
                biGramHashKeyList.append(biGramHashKey)
                self.biGram[biGramHashKey] = 0
            self.biGram[biGramHashKey] += 1
            self.totalCount += 1

            for i in xrange(len(token)-1):
                biGramHashKey = token[i]+' '+token[i+1]
                if biGramHashKey not in biGramHashKeyList:
                    biGramHashKeyList.append(biGramHashKey)
                    self.biGram[biGramHashKey] = 0
                self.biGram[biGramHashKey] += 1
                self.totalCount += 1

            biGramHashKey = token[len(token)-1]+' S'
            if biGramHashKey not in biGramHashKeyList:
                biGramHashKeyList.append(biGramHashKey)
                self.biGram[biGramHashKey] = 0
            self.biGram[biGramHashKey] += 1
            self.totalCount += 1

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