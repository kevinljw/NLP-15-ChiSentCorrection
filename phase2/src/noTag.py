import jieba

trainData = open("input/p2.train.txt",'r')
noTag = open("tmp/segResultTrain.txt",'w')
jieba.load_userdict("input/stopword.txt")
# cw = open("tmp/cw.txt",'w')
# cww = open("tmp/cww.txt",'w')

for line in trainData:
    
    token = line.split('\t')

    right = token[2].split('\n')
    
    # # print(wrong)
    # print(right[0])
    words = jieba.cut(right[0], cut_all=False)
    for word in words:
      noTag.write(str(word.encode('UTF-8'))+" ")
    noTag.write("\n")

  