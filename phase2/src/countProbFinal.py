__author__ = 'mac'
import operator
import numpy
cw = open("tmp/cw.txt",'r')
cww = open("tmp/cww.txt",'r')
#cw = open("cwP2.txt",'r')
#cww = open("cwwP2.txt",'r')
parsed = open("tmp/parsed.txt",'r')
value = open("tmp/value.txt",'r')
#value = open("valueT.txt",'r')
#ourAns = open("testDefined_ans.txt",'r')

#value = open("valueT.txt",'r')
#parsed = open("segResultTest.txt",'r')
#parsed = open("segResultTrainError2.txt",'r')

redundant = open("tmp/redundant.txt",'r')
redundantNum = open("tmp/redundantNum.txt",'r')

ans = open("tmp/ans.txt",'w')

sentenceLength = 200#2962

#alpha = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#beta = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
alpha = []
beta = []
gamma = []
k = 0
alpha.append(1.15)
beta.append(0.1)
gamma.append(1)
#a=0.1 b =1 test     a=0 b=1 train
for i in xrange(1):
    #alpha.append(k)
    #beta.append(k)
    #gamma.append(k)
    k+=0.001

cwGram = {}
cwGramSet = set()
cwwGram = {}
cwwGramSet = set()
redundantSet = set()
redundantGram = {}
valueGram = {}

for data in cw:#5924 2962
    #data = cw.readline()
    #print(data)
    token = data.split()
    #print(token)

    word = token[0]
    count = token[1]
    cwGramSet.add(word)
    cwGram[word] = count
    
#print(cwGram)

for line in cww:#5924 2962
    #data = cww.readline()
    #print(data)
    token = line.split()
    #print(token)

    word = token[0]
    word2 = token[1]
    twoWord = word+" "+word2
    count = token[2]
    cwwGramSet.add(twoWord)
    cwwGram[twoWord] = count

#print(cwwGram)

for data in redundant:#5924 2962
    #data = redundant.readline()
    token = data.split()
    #print(data)
    redundantSet.add(token[0])
#print(redundantSet)

for data in redundantNum:#5924 2962
    #data = redundantNum.readline()
    token = data.split()
    redundantGram[token[0]] = int(token[1])
i=0
for data in value:#5924 2962
    #data = value.readline()
    token = data.split()
    #print(token)
    valueGram[i] = []
    for j in xrange(len(token)):
        valueGram[i].append(str(token[j]))
    i+=1
#print(valueGram)
#print(valueGram[0][0])
#print(redundantSet)
maxAns = 0
for a in alpha:
    for b in beta:
        for g in gamma:
            print a, b, g
            same = 0
            i = 0
            count = 0
            parsed = open("parsedP.txt",'r')
            ourAns = open("testDefined_ans.txt",'r')
            #parsed = open("parsedPt.txt",'r')
            #ourAns = open("place.txt",'r')
            for data in parsed:#2962
                #data = parsed.readline()
                #print(i+1)
                #print(data[:len(data)-1])
                token = data.split()
                #print(token)

                redundantList = []
                #nonRedundantList = []
                #for j in xrange(len(token)):
                    #nonRedundantList.append(j)
                #print(redundantSet)
                #print(redundantList)
                for j in xrange(len(token)):
                    if token[j] in redundantSet:
                        #nonRedundantList.remove(j)
                        redundantList.append(j)
                        #print(token[j])
                #print(len(redundantList))
                #print(redundantList)
                wordMax = {}
                for j in redundantList:
                    #wordMax[j] = 0
                    maxProb = 0
                    if token[j] in cwGramSet:
                        A = int(cwGram[token[j]])
                    else:
                        A = 0
                    #for k in nonRedundantList:
                    for k in xrange(len(token)):
                        if k == j:
                            continue
                        if token[k] in cwGramSet:
                            B = int(cwGram[token[k]])
                        else:
                            B = 0

                        twoWordKey = token[j]+' '+token[k]
                        if twoWordKey in cwwGramSet:
                            C = int(cwwGram[twoWordKey])
                        else:
                            C = 0
                        #print A, B, C
                        prob = 0

                        if A+B-C != 0:
                            prob = float(C)/(A+B-C)
                        if prob != 0:
                            #print(token[j])
                            #prob = float(prob)**(1.15)/(redundantGram[token[j]])**(a)*2962/((float(valueGram[i][j])+1)**b)

                            prob = float(prob)**(a)/(redundantGram[token[j]])**(b)*2962/((float(valueGram[i][j])+1)**g)

                            #prob = float(prob)*(a)+(1-float(redundantGram[token[j]])/2962)*b+(1-1/(float(valueGram[i][j])+1))*g
                            #print(prob)
                            #prob = float(prob)/(redundantGram[token[j]])**(a)*2962/(numpy.log10(float(valueGram[i][j])+1))
                            #prob = float(prob)/(redundantGram[token[j]])**(a)*2962/((float(valueGram[i][j])+1)**(b))
                            #prob = float(prob)/(float(valueGram[i][j])**(0.7))
                            #prob = (1-float(redundantGram[token[j]])/2962)
                            #print(prob)

                        if prob>=maxProb:
                            #print(prob)
                            maxProb = prob



                    wordMax[j] = round(maxProb,4)
                #ans.write(data[:len(data)-1]+'\n')
                #print(wordMax)
                minProb = 100000
                for key, value in wordMax.items():
                    #print(value)

                    if value==minProb:
                        same +=1
                        #print(key)
                        #print(minKey)
                        #print(valueGram[i])

                        if float(valueGram[i][int(key)]) > float(valueGram[i][int(minKey)]):
                            minProb=value
                            minKey=key
                            minWord = token[minKey]

                    if value<minProb:
                        minProb=value
                        minKey=key
                        minWord = token[minKey]
                    #print key, value
                #print(minProb)
                #ans.write(str(i+1)+' '+str(key)+' '+str(value)+'\n')
                length = 0
                #print(minKey)
                for j in xrange(minKey):
                    if j >= len(token):

                        break
                    length += len(token[j])/3
                    #pri
                    #print(j)
                ans.write(str(length+1)+' '+str(length+len(minWord)/3)+"\n")#+str(minWord)+"\n")
                data = ourAns.readline()
                #print(data)
                token = data.split()
                #print(token)
                start = str(length+1)
                end = str(length+len(minWord)/3)
                if start == token[0] and end == token[1]:
                    count+=1
                #print(minWord)
                i+=1

            #print(same)

            #codeAns = open("ans.txt",'r')


            #ourAns = open("place.txt",'r')


            if (float(count)/sentenceLength)>=maxAns:
                maxAns = float(count)/sentenceLength
                maxA = a
                maxB = b
                maxg = g
            #print(float(count)/200)

#print(maxAns)
#print(maxA)
#print(maxB)
#print(maxg)