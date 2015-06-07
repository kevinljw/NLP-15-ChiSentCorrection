import jieba

trainData = open("input/p2.val.txt",'r')
noTag = open("tmp/segResultTest.txt",'w')
jieba.load_userdict("input/stopword.txt")

for line in trainData:
    
    token = line.split('\t')

    testingData = token[1].split('\n')
    
    # # print(wrong)
    # print(testingData[0])
    words = jieba.cut(testingData[0], cut_all=False)
    for word in words:
      # print word.encode('UTF-8')
      noTag.write(str(word.encode('UTF-8'))+" ")
    noTag.write("\n")

  