import jieba
import jieba.posseg

trainData = open("input/p2.train.txt",'r')
noTag = open("tmp/segResultTrainError.txt",'w')
jieba.load_userdict("input/redundant.txt")
# jieba.load_userdict("input/stopword.txt")
# cw = open("tmp/cw.txt",'w')
# cww = open("tmp/cww.txt",'w')

for line in trainData:
    
    token = line.split('\t')

    right = token[1].split('\n')
    
    # # print(wrong)
    # print(right[0])
    words = jieba.posseg.cut(right[0])
    for word in words:
      noTag.write(str(word.word.encode('UTF-8'))+" ")
    noTag.write("\n")

  