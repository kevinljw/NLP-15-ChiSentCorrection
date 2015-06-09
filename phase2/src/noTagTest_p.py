import jieba
import jieba.posseg

trainData = open("input/p2.test.txt",'r')
noTag = open("tmp/segResultTest.txt",'w')
jieba.load_userdict("input/redundant.txt")
# jieba.load_userdict("input/stopword.txt")

for line in trainData:
    
    token = line.split('\t')

    testingData = token[1].split('\n')
    
    # # print(wrong)
    # print(testingData[0])
    words = jieba.posseg.cut(testingData[0])
    for word in words:
      # print word.encode('UTF-8')
      noTag.write(str(word.word.encode('UTF-8'))+" ")
    noTag.write("\n")

  