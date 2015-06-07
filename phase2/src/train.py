

trainData = open("tmp/segResultTrain.txt",'r')
stopwordData = open("input/stopword.txt",'r')
cw = open("tmp/cw.txt",'w')
cww = open("tmp/cww.txt",'w')

stopwordDict=dict()
wwDict=dict()

for everyStopword in stopwordData:

   rawEachWord = everyStopword.strip()
   # print(everyStopword.strip()+"-")

   if rawEachWord not in stopwordDict:
      stopwordDict[rawEachWord] = 0


   # print(stopwordDict[token[0]])


print(len(stopwordDict))
# print(stopwordDict)

# cw.write(str(stopwordDict.keys()))


w2Dict=dict()

for line in trainData:
    
    token = line.split('\n')

    wordList = token[0].split()

    # print(W2List)

    for everyWord in wordList:
      # print(everyWord)
      if everyWord in stopwordDict:
         stopwordDict[everyWord] += 1
      else:
        if everyWord in w2Dict:
         w2Dict[everyWord] += 1
        else: 
         w2Dict[everyWord] = 1

      # count(w1w2)-----------------
      if everyWord in stopwordDict:
        setWordList = list(set(wordList))
        if everyWord not in wwDict:
          wwDict[everyWord]=dict()
        for i in setWordList:
          if i != everyWord:
            # thisWordList = list(wwDict[everyWord])
            if i not in wwDict[everyWord]:
              wwDict[everyWord][i]=1
            else:
              wwDict[everyWord][i]+=1

# print(w2Dict.values())
# print(stopwordDict.values())
# print(wwDict.values())

#output-------------
for k,v in stopwordDict.items():
   cw.write(str(k)+" "+str(v)+"\n")
for k,v in w2Dict.items():
   cw.write(str(k)+" "+str(v)+"\n")

for k,v in wwDict.iteritems():
    for k2,v2 in v.items():
      cww.write(str(k)+" "+str(k2)+" "+str(v2)+"\n")
  