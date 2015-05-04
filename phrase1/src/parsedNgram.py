#!/usr/bin/python
# -*- coding: utf-8 -*-



rightNgram = open("tmp/rightParsed.txt",'r')
wrongNgram = open("tmp/wrongParsed.txt",'r')

rightNgramOut = open("tmp/rightNgram.txt",'w')
wrongNgramOut = open("tmp/wrongNgram.txt",'w')

nGram = {}
nGramHashKeyList = []

for i in xrange(2962):#5924 2962
    data = rightNgram.readline()
    #print(data)
    token = data.split()
    #print(token)
    sentence = token[2:]

    #print(sentence)



    for j in xrange(len(sentence)):
        word = sentence[j].decode('utf8')
        nGramHashKey = word
        #print(nGramHashKey)
        if nGramHashKey not in nGramHashKeyList:
            nGramHashKeyList.append(nGramHashKey)
            nGram[nGramHashKey] = 0
        nGram[nGramHashKey]+=1

    #print(len(nGram))

#print(nGram)
#print(len(nGram))
#print(nGram)
#listSort = sorted(nGram, reverse=True, key=lambda key: list[key])


for keys, values in nGram.items():
    temp = keys
    #print(temp)
    rightNgramOut.write(temp.encode('utf8')+' '+str(values)+'\n')

nGram = {}
nGramHashKeyList = []

for i in xrange(2962):#5924 2962
    data = wrongNgram.readline()
    #print(data)
    token = data.split()
    #print(token)
    sentence = token[2:]

    #print(sentence)



    for j in xrange(len(sentence)):
        word = sentence[j].decode('utf8')
        nGramHashKey = word
        #print(nGramHashKey)
        if nGramHashKey not in nGramHashKeyList:
            nGramHashKeyList.append(nGramHashKey)
            nGram[nGramHashKey] = 0
        nGram[nGramHashKey]+=1

    #print(len(nGram))

#print(nGram)
#print(len(nGram))
#print(nGram)
#listSort = sorted(nGram, reverse=True, key=lambda key: list[key])


for keys, values in nGram.items():
    temp = keys
    #print(temp)
    wrongNgramOut.write(temp.encode('utf8')+' '+str(values)+'\n')