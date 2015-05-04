#!/usr/bin/python
# -*- coding: utf-8 -*-

nGram = {}
nGramHashKeyList = []
line = open("input/p1.test.txt",'r')
rightNgram = open("tmp/noTagTest.txt",'w')

for i in xrange(200):#5924 2962
    data = line.readline()
    token = data.split()
    sentence = token[1:]
    word = sentence[0]
    wordS = word.decode('utf8')
    rightNgram.write(str(word)+'\n')

