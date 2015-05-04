#!/usr/bin/python
# -*- coding: utf-8 -*-

nGram = {}
nGramHashKeyList = []
line = open("input/240365_p1.train.txt",'r')
rightNgram = open("tmp/noTag.txt",'w')

for i in xrange(5924):#5924 2962
    data = line.readline()
    token = data.split()
    sentence = token[2:]
    word = sentence[0]
    wordS = word.decode('utf8')
    rightNgram.write(str(word)+'\n')

