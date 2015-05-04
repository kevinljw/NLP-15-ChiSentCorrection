#!/usr/bin/python
# -*- coding: utf-8 -*-

nGram = {}
nGramHashKeyList = []

line = open("input/240365_p1.train.txt",'r')
parsed = open("tmp/segResult.txt",'r')
rightNgram = open("tmp/rightParsed.txt",'w')
worngNgram = open("tmp/wrongParsed.txt",'w')
mixNgram = open("tmp/mixParsed.txt",'w')



for i in xrange(5924):#5924 2962
    data = line.readline()
    sentence = parsed.readline()
    token = data.split()
    mixNgram.write(str(token[0])+'\t'+str(token[1])+'\t'+sentence)
    if int(token[1]) is 0:
        rightNgram.write(str(token[0])+'\t'+str(token[1])+'\t'+sentence)
    else:
        wrongNgram.write(str(token[0])+'\t'+str(token[1])+'\t'+sentence)

