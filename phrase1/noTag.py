#!/usr/bin/python
# -*- coding: utf-8 -*-

nGram = {}
nGramHashKeyList = []
line = open("240365_p1.train.txt",'r')
rightNgram = open("noTag.txt",'w')

for i in xrange(5924):#5924 2962
    data = line.readline()
    #print(data)
    token = data.split()
    #print(token)
    sentence = token[2:]
    #print(sentence)
    word = sentence[0]
    wordS = word.decode('utf8')
    #print(word2[1])
    rightNgram.write(str(word)+'\n')

