#!/usr/bin/python
# encoding: utf-8

import jieba
import jieba.posseg
import partofspeech
import bigram

testFile = open("input/noTagTest.txt",'r')
redundantFile = open('input/redundantAll.txt','r')
valueFile = open('tmp/value.txt','w')

partofspeech_object = partofspeech.PartOfSpeechBigram()
bigram_object = bigram.Bigram()

redundantCount = {}
weight = 0.8

for line in redundantFile:
	line = line.rstrip()
	words = jieba.posseg.cut(line)
	if line in redundantCount:
		redundantCount[line] += 1
	else:
		redundantCount[line] = 1

for line in testFile:
	line.decode('utf8')
	line = line.rstrip()
	words = jieba.posseg.cut(line)
	words_list = list(words)

	maxRatio = 0
	totalLength = 0

	valueList = []

	key1 = 'ss'
	key2 = words_list[0].flag
	key3 = words_list[1].flag
	ratio1 = partofspeech_object.findImproveRatio(key1, key2, key3)
	key1 = 'ss'
	key2 = words_list[0].word
	key3 = words_list[1].word
	ratio2 = bigram_object.findImproveRatio(key1, key2, key3)
	totalLength += len(words_list[0].word)
	occuranceRate = 1
	if words_list[0].word.encode('utf8') in redundantCount:
		occuranceRate += redundantCount[words_list[0].word.encode('utf8')]
	valueFile.write(str((ratio1)*occuranceRate)+' ')

	for i in xrange(len(words_list)-2):
		key1 = words_list[i].flag
		key2 = words_list[i+1].flag
		key3 = words_list[i+2].flag
		ratio1 = partofspeech_object.findImproveRatio(key1, key2, key3)
		key1 = words_list[i].word
		key2 = words_list[i+1].word
		key3 = words_list[i+2].word
		ratio2 = bigram_object.findImproveRatio(key1, key2, key3)
		totalLength += len(words_list[i+1].word)
		occuranceRate = 1
		if words_list[i+1].word.encode('utf8') in redundantCount:
			occuranceRate += redundantCount[words_list[i+1].word.encode('utf8')]
		valueFile.write(str((ratio1)*occuranceRate)+' ')

	key1 = words_list[len(words_list)-2].flag
	key2 = words_list[len(words_list)-1].flag
	key3 = 'se'
	ratio1 = partofspeech_object.findImproveRatio(key1, key2, key3)
	key1 = words_list[len(words_list)-2].word
	key2 = words_list[len(words_list)-1].word
	key3 = 'se'
	ratio2 = bigram_object.findImproveRatio(key1, key2, key3)
	totalLength += len(words_list[len(words_list)-1].word)
	occuranceRate = 1
	if words_list[len(words_list)-1].word.encode('utf8') in redundantCount:
		occuranceRate += redundantCount[words_list[len(words_list)-1].word.encode('utf8')]
	valueFile.write(str((ratio1)*occuranceRate)+'\n')
