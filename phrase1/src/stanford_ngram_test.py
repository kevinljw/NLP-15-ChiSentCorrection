# encoding: utf-8

import numpy as np

file_td = file('tmp/segResultTest.txt', 'r')            # training data
file_rn = file('tmp/rightNgram.txt', 'r')               # right bigram
file_wn = file('tmp/wrongNgram.txt', 'r')               # wrong bigram
file_pb = file('tmp/test_prob.txt', 'w')                # output probability
file_an = file('input/manual_labeled_answer.txt', 'r')    # answer labeled manually

NgramTableR = {}
NgramTableW = {}
NgramKeyR = []
NgramKeyW = []
countListR = []
countListW = []
KatzTableR = {}
KatzTableW = {}

total_right_ngram = 0
total_wrong_ngram = 0

def katz(c, table):
    if c == 0:
        cs = ((c+1) * float(table[c+1]) - c * (5+1) * float(table[5+1]) / table[1]) / (1 - (5+1) * float(table[5+1]) / table[1])
    elif c <= 5:
        cs = ((c+1) * float(table[c+1]) / table[c] - c * (5+1) * float(table[5+1]) / table[1]) / (1 - (5+1) * float(table[5+1]) / table[1])
    else:
        cs = float(c)
    return cs

# read right ngram and build katz table
for line in file_rn:
    line = line.decode('utf8')
    line = line.split(' ')
    word = line[0]
    count = int(line[1])
    total_right_ngram += count
    NgramTableR[word] = count
    if word not in NgramKeyR:
        NgramKeyR.append(word)
    if count not in countListR:
        countListR.append(count)
        KatzTableR[count] = 0
    KatzTableR[count] += 1

# read wrong ngram and build katz table
for line in file_wn:
    line = line.decode('utf8')
    line = line.split(' ')
    word = line[0]
    count = int(line[1])
    total_wrong_ngram += count
    NgramTableW[word] = count
    if word not in NgramKeyW:
        NgramKeyW.append(word)
    if count not in countListW:
        countListW.append(count)
        KatzTableW[count] = 0
    KatzTableW[count] += 1

print total_right_ngram
print total_wrong_ngram

for line in file_td:
    line = line.split('\n')
    sline = line[0].decode('utf8')
    tokens = sline.split(' ')
    label = file_an.readline()

    r_prob = 1
    for token in tokens:
        if token in NgramKeyR:
            r_prob *= katz(NgramTableR[token], KatzTableR) / total_right_ngram
        else:
            r_prob *= katz(0, KatzTableR) / total_right_ngram
    w_prob = 1
    for token in tokens:
        if token in NgramKeyW:
            w_prob *= katz(NgramTableW[token], KatzTableW) / total_wrong_ngram
        else:
            w_prob *= katz(0, KatzTableW) / total_wrong_ngram
    file_pb.write(label[0] + ' 1:' + str(np.log10(r_prob)) + ' 2:' + str(np.log10(w_prob)) + '\n')
