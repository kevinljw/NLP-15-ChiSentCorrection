#encoding=utf-8
import jieba
import jieba.posseg

#redundant = open("testing.txt",'r')
redundant = open("input/p2.test.txt",'r')
#redundant = open("noTagWrong.txt",'r')
red = open("tmp/parsed.txt",'w')
#red = open("parsedPt.txt",'w')

reWords = set()
for data in redundant:#5924 2962
    #data = redundant.readline()
    #print(data)
    token = data.split()
    #print(token)
    sentence = token[1]
    #print(sentence)
    #sentence = token[2]
    #red.write(wrong+'\n')


    #sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
    print "Input：", sentence
    #words = jieba.cut(sentence, cut_all=False)
    words = jieba.posseg.cut(sentence)
    print "Output 精確模式 Full Mode："
    first = 1
    print(words)
    for word in words:
        if first == 1:
            red.write(word.word.encode('utf8'))
        else:
            red.write(' '+word.word.encode('utf8'))
        first = 0
        print word
    red.write('\n')